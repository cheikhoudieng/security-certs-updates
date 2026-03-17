# ================================================================
# updater.ps1  --  Server-First Edition v4.0
# Hosted on GitHub, downloaded fresh on every run
# Usage: powershell -File updater.ps1 -BaseUrl "https://raw.githubusercontent.com/USER/REPO/BRANCH"
# Compatible: Windows 7 SP1 / 8 / 8.1 / 10 / 11
# ================================================================
param(
    [Parameter(Mandatory = $true)][string]$BaseUrl
)

# ----------------------------------------------------------------
# TLS 1.2 -- required for GitHub on Windows 7
# ----------------------------------------------------------------
try {
    [Net.ServicePointManager]::SecurityProtocol = [Enum]::ToObject([Net.SecurityProtocolType], 3072)
} catch {
    try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls } catch {}
}

# ----------------------------------------------------------------
# Runtime capability detection
# ----------------------------------------------------------------
$_hasZipFile = $false
try {
    [System.Reflection.Assembly]::LoadWithPartialName("System.IO.Compression.FileSystem") | Out-Null
    $null = [System.IO.Compression.ZipFile]
    $_hasZipFile = $true
} catch {}

$_useModernTask = ($null -ne (Get-Command Register-ScheduledTask -ErrorAction SilentlyContinue))

# ----------------------------------------------------------------
# Base paths (before config is read -- used by the logger)
# ----------------------------------------------------------------
$AppDataRoot = [Environment]::GetFolderPath("LocalApplicationData")
$LauncherDir = Join-Path $AppDataRoot ("GH_" + ($BaseUrl -split "/" | Select-Object -Last 2 | Select-Object -First 1))
$AppliedPath = Join-Path $LauncherDir "applied.json"

$script:LogDir       = $LauncherDir
$script:LogKeepWeeks = 2

if (-not (Test-Path $script:LogDir)) { New-Item -ItemType Directory -Path $script:LogDir -Force | Out-Null }

# ----------------------------------------------------------------
# Network helpers
# ----------------------------------------------------------------
function New-NoCacheWebClient {
    $wc = New-Object System.Net.WebClient
    try { $wc.CachePolicy = New-Object System.Net.Cache.RequestCachePolicy([System.Net.Cache.RequestCacheLevel]::NoCacheNoStore) } catch {}
    $wc.Headers.Add("User-Agent",    "PowerShell-AutoUpdate/4.0")
    $wc.Headers.Add("Cache-Control", "no-cache, no-store, must-revalidate")
    $wc.Headers.Add("Pragma",        "no-cache")
    return $wc
}

function Get-UnixMs {
    return [long](([datetime]::UtcNow) - [datetime]"1970-01-01").TotalMilliseconds
}

# ----------------------------------------------------------------
# Logging (ISO week, fallback to year-month on PS 2.0)
# ----------------------------------------------------------------
function Write-Log {
    param([string]$Level, [string]$Message)
    try   { $week = Get-Date -UFormat "%Y-W%V" }
    catch { $week = Get-Date -Format "yyyy-MM" }
    $line    = "[" + (Get-Date -Format "yyyy-MM-dd HH:mm:ss") + "] [$Level] $Message"
    $logFile = Join-Path $script:LogDir ("update_" + $week + ".log")
    if (-not (Test-Path $script:LogDir)) { New-Item -ItemType Directory -Path $script:LogDir -Force | Out-Null }
    Add-Content -Path $logFile -Value $line -Encoding UTF8
    if ($script:LogKeepWeeks -gt 0) {
        Get-ChildItem $script:LogDir -Filter "update_*.log" -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending |
            Select-Object -Skip $script:LogKeepWeeks |
            Remove-Item -Force -ErrorAction SilentlyContinue
    }
}

# ----------------------------------------------------------------
# Read config.json from GitHub
# ----------------------------------------------------------------
function Read-ServerConfig {
    param([string]$Url)
    try {
        $wc  = New-NoCacheWebClient
        $raw = $wc.DownloadString($Url + "?nc=" + (Get-UnixMs)).Trim()
        $wc.Dispose()

        # ConvertFrom-Json (PS 3+) with fallback JavaScriptSerializer (PS 2 / .NET 3.5)
        try {
            $obj = $raw | ConvertFrom-Json
        } catch {
            Add-Type -AssemblyName System.Web.Extensions -ErrorAction Stop
            $jss = New-Object System.Web.Script.Serialization.JavaScriptSerializer
            $obj = $jss.DeserializeObject($raw)
        }

        $delays = @(5, 15, 30, 60, 120)
        if ($null -ne $obj.retry_delays_sec) {
            try { $delays = @($obj.retry_delays_sec) } catch {}
        }

        $extra = @()
        if ($null -ne $obj.extra_files) {
            try { $extra = @($obj.extra_files) } catch {}
        }

        return @{
            zip_path           = [string]$obj.zip_path
            app_folder         = [string]$obj.app_folder
            python_exe         = [string]$obj.python_exe
            setup_script       = [string]$obj.setup_script
            task_name          = if ($obj.task_name)          { [string]$obj.task_name }          else { "GH_AutoUpdate" }
            task_interval_min  = if ($obj.task_interval_min)  { [int]$obj.task_interval_min }     else { 60 }
            log_keep_weeks     = if ($obj.log_keep_weeks)     { [int]$obj.log_keep_weeks }        else { 2 }
            retry_max          = if ($obj.retry_max)          { [int]$obj.retry_max }             else { 5 }
            retry_delays_sec   = $delays
            update_enabled     = if ($null -ne $obj.update_enabled)     { [bool]$obj.update_enabled }     else { $true }
            kill_before_update = if ($null -ne $obj.kill_before_update) { [bool]$obj.kill_before_update } else { $false }
            kill_process_name  = if ($obj.kill_process_name)  { [string]$obj.kill_process_name }  else { "" }
            restart_after      = if ($null -ne $obj.restart_after)      { [bool]$obj.restart_after }      else { $false }
            restart_exe        = if ($obj.restart_exe)        { [string]$obj.restart_exe }        else { "" }
            min_free_mb        = if ($obj.min_free_mb)        { [int]$obj.min_free_mb }           else { 100 }
            rollback_enabled   = if ($null -ne $obj.rollback_enabled)   { [bool]$obj.rollback_enabled }   else { $false }
            backup_versions    = if ($obj.backup_versions)    { [int]$obj.backup_versions }       else { 2 }
            notify_on_success  = if ($null -ne $obj.notify_on_success)  { [bool]$obj.notify_on_success }  else { $false }
            notify_on_error    = if ($null -ne $obj.notify_on_error)    { [bool]$obj.notify_on_error }    else { $false }
            webhook_url        = if ($obj.webhook_url)        { [string]$obj.webhook_url }        else { "" }
            extra_files        = $extra
        }
    } catch {
        return $null
    }
}

# ----------------------------------------------------------------
# Read / write applied.json
# ----------------------------------------------------------------
function Read-AppliedState {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return $null }
    try {
        $obj = (Get-Content $Path -Raw) | ConvertFrom-Json
        return @{
            app_folder        = [string]$obj.app_folder
            task_name         = [string]$obj.task_name
            task_interval_min = [int]$obj.task_interval_min
            python_exe        = [string]$obj.python_exe
            version           = [string]$obj.version
        }
    } catch { return $null }
}

function Save-AppliedState {
    param([string]$Path, [hashtable]$Cfg, [string]$Version)
    $state = [ordered]@{
        app_folder        = $Cfg.app_folder
        task_name         = $Cfg.task_name
        task_interval_min = $Cfg.task_interval_min
        python_exe        = $Cfg.python_exe
        version           = $Version
    }
    try {
        $json = $state | ConvertTo-Json
    } catch {
        Add-Type -AssemblyName System.Web.Extensions -ErrorAction Stop
        $json = (New-Object System.Web.Script.Serialization.JavaScriptSerializer).Serialize($state)
    }
    Set-Content -Path $Path -Value $json -Encoding UTF8
}

# ----------------------------------------------------------------
# Register / recreate the scheduled task
# ----------------------------------------------------------------
function Register-UpdaterTask {
    param([string]$TaskName, [int]$IntervalMin, [string]$LauncherPath)

    if ($_useModernTask) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false -ErrorAction SilentlyContinue
        Register-ScheduledTask `
            -TaskName  $TaskName `
            -Action    (New-ScheduledTaskAction -Execute "wscript.exe" -Argument ('"' + $LauncherPath + '"')) `
            -Trigger   (New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes $IntervalMin)) `
            -Settings  (New-ScheduledTaskSettingsSet -ExecutionTimeLimit (New-TimeSpan -Minutes 30) -StartWhenAvailable -MultipleInstances IgnoreNew -Hidden -RestartCount 3 -RestartInterval (New-TimeSpan -Minutes 5)) `
            -Principal (New-ScheduledTaskPrincipal -UserId ([Environment]::UserName) -LogonType Interactive -RunLevel Limited) `
            -Force | Out-Null
    } else {
        & schtasks.exe /Delete /TN $TaskName /F 2>&1 | Out-Null
        $xmlPath   = Join-Path $env:TEMP ("task_" + $TaskName + ".xml")
        $startTime = (Get-Date).AddMinutes(1).ToString("yyyy-MM-ddTHH:mm:ss")
        $userName  = [Environment]::UserDomainName + "\" + [Environment]::UserName
        $interval  = "PT" + $IntervalMin + "M"
        [System.IO.File]::WriteAllText($xmlPath, (@"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <Triggers><TimeTrigger>
    <Repetition><Interval>$interval</Interval><StopAtDurationEnd>false</StopAtDurationEnd></Repetition>
    <StartBoundary>$startTime</StartBoundary><Enabled>true</Enabled>
  </TimeTrigger></Triggers>
  <Principals><Principal id="Author">
    <UserId>$userName</UserId><LogonType>InteractiveToken</LogonType><RunLevel>LeastPrivilege</RunLevel>
  </Principal></Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <Hidden>true</Hidden><ExecutionTimeLimit>PT30M</ExecutionTimeLimit>
    <StartWhenAvailable>true</StartWhenAvailable><Enabled>true</Enabled>
    <RestartOnFailure><Interval>PT5M</Interval><Count>3</Count></RestartOnFailure>
  </Settings>
  <Actions Context="Author"><Exec>
    <Command>wscript.exe</Command><Arguments>"$LauncherPath"</Arguments>
  </Exec></Actions>
</Task>
"@), [System.Text.Encoding]::Unicode)
        & schtasks.exe /Create /F /TN $TaskName /XML $xmlPath 2>&1 | Out-Null
        Remove-Item $xmlPath -Force -ErrorAction SilentlyContinue
    }
}

# ----------------------------------------------------------------
# Infrastructure reconciliation
# Compares desired state (GitHub config) vs applied state (applied.json)
# Applies structural changes before any version update
# ----------------------------------------------------------------
function Invoke-Reconciliation {
    param([hashtable]$Cfg, $Applied)

    $launcherVBS = Join-Path $LauncherDir "Launcher.vbs"

    # --- app_folder renamed
    if ($null -ne $Applied -and $Applied.app_folder -ne "" -and $Applied.app_folder -ne $Cfg.app_folder) {
        Write-Log "INFO" ("app_folder changed: " + $Applied.app_folder + " -> " + $Cfg.app_folder)
        $oldRoot = Join-Path $AppDataRoot $Applied.app_folder
        $newRoot = Join-Path $AppDataRoot $Cfg.app_folder

        if (Test-Path $oldRoot) {
            if (-not (Test-Path $newRoot)) {
                try {
                    Move-Item -Path $oldRoot -Destination $newRoot -Force
                    Write-Log "INFO" ("Folder moved: " + $oldRoot + " -> " + $newRoot)
                } catch {
                    Write-Log "WARN" ("Move-Item failed, trying robocopy: " + $_.Exception.Message)
                    New-Item -ItemType Directory -Path $newRoot -Force | Out-Null
                    & robocopy $oldRoot $newRoot /E /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1 | Out-Null
                    if ($LASTEXITCODE -lt 8) {
                        Remove-Item $oldRoot -Recurse -Force -ErrorAction SilentlyContinue
                        Write-Log "INFO" "Folder moved via robocopy"
                    } else {
                        Write-Log "ERROR" "Folder move failed"
                    }
                }
            } else {
                Write-Log "INFO" ("New folder already exists -- removing old: " + $oldRoot)
                Remove-Item $oldRoot -Recurse -Force -ErrorAction SilentlyContinue
            }
        }
    }

    # --- Rebuild derived paths (normal run or after rename)
    $script:RootDir      = Join-Path $AppDataRoot $Cfg.app_folder
    $script:ProjectDir   = Join-Path $script:RootDir "project"
    $script:LogDir       = Join-Path $script:RootDir "logs"
    $script:BackupDir    = Join-Path $script:RootDir "backups"
    $script:LocalVerFile = Join-Path $script:RootDir "version.txt"
    $script:LogKeepWeeks = $Cfg.log_keep_weeks

    foreach ($d in @($script:RootDir, $script:ProjectDir, $script:LogDir)) {
        if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
    }

    # --- Scheduled task: name or interval changed
    $taskChanged = (
        $null -ne $Applied -and (
            ($Applied.task_name         -ne "" -and $Applied.task_name         -ne $Cfg.task_name) -or
            ($Applied.task_interval_min -gt 0  -and $Applied.task_interval_min -ne $Cfg.task_interval_min)
        )
    )

    if ($taskChanged) {
        Write-Log "INFO" ("Task changed: " + $Applied.task_name + " (" + $Applied.task_interval_min + "min) -> " + $Cfg.task_name + " (" + $Cfg.task_interval_min + "min)")
        if ($Applied.task_name -ne "" -and $Applied.task_name -ne $Cfg.task_name) {
            & schtasks.exe /Delete /TN $Applied.task_name /F 2>&1 | Out-Null
            Write-Log "INFO" ("Old task removed: " + $Applied.task_name)
        }
        Register-UpdaterTask -TaskName $Cfg.task_name -IntervalMin $Cfg.task_interval_min -LauncherPath $launcherVBS
        Write-Log "INFO" ("New task registered: " + $Cfg.task_name + " every " + $Cfg.task_interval_min + " min")
    }
}

# ----------------------------------------------------------------
# Backup management
# ----------------------------------------------------------------
function Backup-CurrentVersion {
    param([hashtable]$Cfg)
    if (-not $Cfg.rollback_enabled) { return }
    if (-not (Test-Path $script:ProjectDir)) { return }
    $localVer = ""
    if (Test-Path $script:LocalVerFile) { $localVer = (Get-Content $script:LocalVerFile -Raw).Trim() }
    if ($localVer -eq "") { return }
    if (-not (Test-Path $script:BackupDir)) { New-Item -ItemType Directory -Path $script:BackupDir -Force | Out-Null }
    $backupPath = Join-Path $script:BackupDir $localVer
    if (Test-Path $backupPath) { Remove-Item $backupPath -Recurse -Force -ErrorAction SilentlyContinue }
    & robocopy $script:ProjectDir $backupPath /E /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1 | Out-Null
    if ($LASTEXITCODE -lt 8) {
        Write-Log "INFO" ("Backup OK: version " + $localVer)
    } else {
        Write-Log "WARN" ("Backup failed for version " + $localVer)
    }
    # Purge excess backups
    $allBackups = @(Get-ChildItem $script:BackupDir -Directory -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending)
    if ($allBackups.Count -gt $Cfg.backup_versions) {
        $allBackups | Select-Object -Skip $Cfg.backup_versions | ForEach-Object {
            Remove-Item $_.FullName -Recurse -Force -ErrorAction SilentlyContinue
            Write-Log "INFO" ("Backup purged: " + $_.Name)
        }
    }
}

function Invoke-Rollback {
    param([hashtable]$Cfg)
    if (-not $Cfg.rollback_enabled) { return $false }
    if (-not (Test-Path $script:BackupDir)) { Write-Log "WARN" "No backup available"; return $false }
    $latest = Get-ChildItem $script:BackupDir -Directory -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($null -eq $latest) { Write-Log "WARN" "Backup folder is empty"; return $false }
    Write-Log "INFO" ("Rolling back to: " + $latest.Name)
    & robocopy $latest.FullName $script:ProjectDir /E /PURGE /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1 | Out-Null
    if ($LASTEXITCODE -lt 8) {
        Set-Content -Path $script:LocalVerFile -Value $latest.Name -Encoding UTF8
        Write-Log "INFO" ("Rollback succeeded: " + $latest.Name)
        return $true
    }
    Write-Log "ERROR" "Rollback failed"
    return $false
}

# ----------------------------------------------------------------
# Webhook notification (Slack / Teams / Discord / custom)
# ----------------------------------------------------------------
function Send-Notification {
    param([hashtable]$Cfg, [string]$Status, [string]$Message)
    if ($Cfg.webhook_url -eq "") { return }
    if ($Status -eq "SUCCESS" -and -not $Cfg.notify_on_success) { return }
    if ($Status -eq "ERROR"   -and -not $Cfg.notify_on_error)   { return }
    try {
        $body = '{"text":"[AutoUpdate ' + $Cfg.app_folder + '] ' + $Status + ' -- ' + $Message.Replace('"','\"') + '"}'
        $wc   = New-NoCacheWebClient
        $wc.Headers.Add("Content-Type", "application/json")
        $wc.UploadString($Cfg.webhook_url, "POST", $body) | Out-Null
        $wc.Dispose()
        Write-Log "INFO" ("Notification sent: " + $Status)
    } catch {
        Write-Log "WARN" ("Notification failed: " + $_.Exception.Message)
    }
}

# ----------------------------------------------------------------
# Disk space check
# ----------------------------------------------------------------
function Test-DiskSpace {
    param([int]$MinFreeMb)
    try {
        $drive  = [System.IO.Path]::GetPathRoot($script:RootDir)
        $disk   = Get-PSDrive ($drive.TrimEnd('\').TrimEnd(':')) -ErrorAction SilentlyContinue
        if ($null -eq $disk) { return $true }
        $freeMb = [math]::Round($disk.Free / 1MB, 0)
        if ($freeMb -lt $MinFreeMb) {
            Write-Log "ERROR" ("Insufficient disk space: " + $freeMb + " MB free, minimum required: " + $MinFreeMb + " MB")
            return $false
        }
        return $true
    } catch { return $true }
}

# ----------------------------------------------------------------
# Download with retry
# ----------------------------------------------------------------
function Download-WithRetry {
    param([string]$Url, [string]$Dest, [int]$MaxRetries, [array]$Delays)
    for ($i = 1; $i -le $MaxRetries; $i++) {
        Write-Log "INFO" ("Download attempt " + $i + "/" + $MaxRetries)
        try {
            $wc = New-NoCacheWebClient
            $wc.DownloadFile($Url, $Dest)
            $wc.Dispose()
            if ((Test-Path $Dest) -and (Get-Item $Dest).Length -gt 1024) {
                Write-Log "INFO" ("Download OK -- " + [math]::Round((Get-Item $Dest).Length / 1KB, 1) + " KB")
                return $true
            }
            Write-Log "WARN" "File too small -- possible 404"
        } catch {
            Write-Log "WARN" ("Network error attempt " + $i + ": " + $_.Exception.Message)
        }
        if ($i -lt $MaxRetries) {
            $wait = if ($i - 1 -lt $Delays.Count) { $Delays[$i - 1] } else { 120 }
            Write-Log "INFO" ("Retrying in " + $wait + " seconds...")
            Start-Sleep -Seconds $wait
        }
    }
    Write-Log "ERROR" ("Download failed after " + $MaxRetries + " attempts")
    return $false
}

# ----------------------------------------------------------------
# ZIP extraction
# ----------------------------------------------------------------
function Expand-Archive-Compat {
    param([string]$ZipFile, [string]$OutPath)
    try {
        if (Test-Path $OutPath) { Remove-Item $OutPath -Recurse -Force }
        New-Item -ItemType Directory -Path $OutPath -Force | Out-Null
        if ($_hasZipFile) {
            [System.IO.Compression.ZipFile]::ExtractToDirectory($ZipFile, $OutPath)
            Write-Log "INFO" "Extraction OK (.NET ZipFile)"
        } else {
            $shell  = New-Object -ComObject Shell.Application
            $destNS = $shell.NameSpace($OutPath)
            $destNS.CopyHere($shell.NameSpace($ZipFile).Items(), 0x14)
            $deadline = (Get-Date).AddMinutes(5)
            do { Start-Sleep -Milliseconds 500 } while (
                (Get-ChildItem $OutPath -Recurse -File -ErrorAction SilentlyContinue).Count -eq 0 -and
                (Get-Date) -lt $deadline
            )
            Start-Sleep -Seconds 2
            try { [Runtime.InteropServices.Marshal]::ReleaseComObject($shell) | Out-Null } catch {}
            Write-Log "INFO" "Extraction OK (Shell.Application)"
        }
        return $true
    } catch {
        Write-Log "ERROR" ("Extraction failed: " + $_.Exception.Message)
        return $false
    }
}

# ----------------------------------------------------------------
# Detect root folder inside ZIP
# ----------------------------------------------------------------
function Resolve-ExtractRoot {
    param([string]$Path)
    $canon = (Resolve-Path $Path).Path
    $items = @(Get-ChildItem $canon -ErrorAction SilentlyContinue)
    if ($items.Count -eq 1 -and $items[0].PSIsContainer) {
        Write-Log "INFO" ("Wrapper folder detected: " + $items[0].Name + " -- unwrapping")
        return (Resolve-Path $items[0].FullName).Path
    }
    return $canon
}

# ----------------------------------------------------------------
# Copy files to ProjectDir
# ----------------------------------------------------------------
function Copy-ProjectFiles {
    param([string]$Src, [string]$Dest)
    try {
        if (-not (Test-Path $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }
        & robocopy $Src $Dest /E /PURGE /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1 | Out-Null
        if ($LASTEXITCODE -lt 8) {
            Write-Log "INFO" ("Copy OK robocopy (exit " + $LASTEXITCODE + ")")
            return $true
        }
        Write-Log "WARN" ("robocopy exit " + $LASTEXITCODE + " -- falling back to Copy-Item")
        Push-Location $Src
        Get-ChildItem -Recurse | ForEach-Object {
            $rel    = (Resolve-Path -Relative $_.FullName).TrimStart(".\\/")
            $target = Join-Path $Dest $rel
            if ($_.PSIsContainer) {
                if (-not (Test-Path $target)) { New-Item -ItemType Directory -Path $target -Force | Out-Null }
            } else {
                $td = Split-Path $target -Parent
                if (-not (Test-Path $td)) { New-Item -ItemType Directory -Path $td -Force | Out-Null }
                Copy-Item $_.FullName -Destination $target -Force
            }
        }
        Pop-Location
        Write-Log "INFO" "Copy OK (Copy-Item fallback)"
        return $true
    } catch {
        try { Pop-Location } catch {}
        Write-Log "ERROR" ("Copy failed: " + $_.Exception.Message)
        return $false
    }
}

# ----------------------------------------------------------------
# Download extra files
# ----------------------------------------------------------------
function Get-ExtraFiles {
    param([hashtable]$Cfg)
    if ($Cfg.extra_files.Count -eq 0) { return $true }
    $ok = $true
    foreach ($entry in $Cfg.extra_files) {
        try {
            $url  = [string]$entry.url
            $dest = [string]$entry.dest
            if ($url -eq "" -or $dest -eq "") { continue }
            $destFull = if ([System.IO.Path]::IsPathRooted($dest)) { $dest } else { Join-Path $script:ProjectDir $dest }
            $destDir  = Split-Path $destFull -Parent
            if (-not (Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir -Force | Out-Null }
            Write-Log "INFO" ("Extra file: " + $url)
            if (-not (Download-WithRetry -Url $url -Dest $destFull -MaxRetries $Cfg.retry_max -Delays $Cfg.retry_delays_sec)) {
                Write-Log "WARN" ("Extra file failed: " + $url)
                $ok = $false
            }
        } catch {
            Write-Log "WARN" ("extra_files error: " + $_.Exception.Message)
            $ok = $false
        }
    }
    return $ok
}

# ----------------------------------------------------------------
# Stop / start the application process
# ----------------------------------------------------------------
function Stop-AppProcess {
    param([hashtable]$Cfg)
    if (-not $Cfg.kill_before_update -or $Cfg.kill_process_name -eq "") { return }
    try {
        $procs = Get-Process -Name ($Cfg.kill_process_name -replace "\.exe$","") -ErrorAction SilentlyContinue
        if ($procs) {
            $procs | Stop-Process -Force -ErrorAction SilentlyContinue
            Write-Log "INFO" ("Process stopped: " + $Cfg.kill_process_name)
            Start-Sleep -Seconds 2
        }
    } catch {
        Write-Log "WARN" ("Stop-AppProcess: " + $_.Exception.Message)
    }
}

function Start-AppProcess {
    param([hashtable]$Cfg)
    if (-not $Cfg.restart_after -or $Cfg.restart_exe -eq "") { return }
    try {
        $exePath = if ([System.IO.Path]::IsPathRooted($Cfg.restart_exe)) {
            $Cfg.restart_exe
        } else {
            Join-Path $script:ProjectDir $Cfg.restart_exe
        }
        if (Test-Path $exePath) {
            Start-Process -FilePath $exePath -WorkingDirectory $script:ProjectDir -WindowStyle Normal
            Write-Log "INFO" ("Application restarted: " + $exePath)
        } else {
            Write-Log "WARN" ("restart_exe not found: " + $exePath)
        }
    } catch {
        Write-Log "WARN" ("Start-AppProcess: " + $_.Exception.Message)
    }
}

# ----------------------------------------------------------------
# Run setup.py
# ----------------------------------------------------------------
function Invoke-SetupScript {
    param([hashtable]$Cfg)
    $pyPath    = Join-Path $script:ProjectDir $Cfg.python_exe
    $setupPath = Join-Path $script:ProjectDir $Cfg.setup_script
    if (-not (Test-Path $pyPath)) {
        Write-Log "ERROR" ("Python not found: " + $pyPath)
        return $false
    }
    if (-not (Test-Path $setupPath)) {
        Write-Log "ERROR" ("setup script not found: " + $setupPath)
        return $false
    }
    try {
        Write-Log "INFO" ("Running: " + $Cfg.python_exe + " " + $Cfg.setup_script)
        $psi                  = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName         = $pyPath
        $psi.Arguments        = '"' + $setupPath + '"'
        $psi.WorkingDirectory = $script:ProjectDir
        $psi.WindowStyle      = [Diagnostics.ProcessWindowStyle]::Hidden
        $psi.CreateNoWindow   = $true
        $psi.UseShellExecute  = $false
        $proc = [Diagnostics.Process]::Start($psi)
        $proc.WaitForExit()
        Write-Log "INFO" ("setup.py exit code: " + $proc.ExitCode)
        if ($proc.ExitCode -ne 0) {
            Write-Log "WARN" ("setup.py non-zero exit: " + $proc.ExitCode)
        }
        return $true
    } catch {
        Write-Log "ERROR" ("Could not launch Python: " + $_.Exception.Message)
        return $false
    }
}

# ----------------------------------------------------------------
# Version checks
# ----------------------------------------------------------------
function Get-RemoteVersion {
    param([string]$VerUrl, [int]$MaxRetries, [array]$Delays)
    for ($i = 1; $i -le $MaxRetries; $i++) {
        try {
            $wc  = New-NoCacheWebClient
            $raw = $wc.DownloadString($VerUrl + "?nc=" + (Get-UnixMs)).Trim()
            $wc.Dispose()
            if ($raw.Length -gt 0) {
                Write-Log "INFO" ("Remote version: " + $raw)
                return $raw
            }
            Write-Log "WARN" "version.txt is empty"
        } catch {
            Write-Log "WARN" ("Version fetch attempt " + $i + ": " + $_.Exception.Message)
        }
        if ($i -lt $MaxRetries) {
            $wait = if ($i - 1 -lt $Delays.Count) { $Delays[$i - 1] } else { 30 }
            Start-Sleep -Seconds $wait
        }
    }
    return $null
}

function Get-LocalVersion {
    if (-not (Test-Path $script:LocalVerFile)) {
        Write-Log "INFO" "First install (no local version.txt)"
        return $null
    }
    $v = (Get-Content $script:LocalVerFile -Raw).Trim()
    Write-Log "INFO" ("Local version: " + $v)
    return $v
}

# ================================================================
# MAIN LOGIC
# ================================================================
Write-Log "INFO" "====== UPDATER START (v4.0) BaseUrl: $BaseUrl ======"

# 1. Read server config
$cfg = Read-ServerConfig -Url ($BaseUrl + "/config.json")
if ($null -eq $cfg) {
    Write-Log "ERROR" "Cannot read config.json -- aborting"
    exit 1
}
Write-Log "INFO" ("Config loaded: app_folder=" + $cfg.app_folder + " task=" + $cfg.task_name)

# 2. Read applied state
$applied = Read-AppliedState -Path $AppliedPath

# 3. Reconcile infrastructure (folder rename, task recreation)
Invoke-Reconciliation -Cfg $cfg -Applied $applied

# 4. Check if updates are enabled
if (-not $cfg.update_enabled) {
    Write-Log "INFO" "update_enabled=false -- cycle skipped"
    exit 0
}

# 5. Check disk space
if (-not (Test-DiskSpace -MinFreeMb $cfg.min_free_mb)) {
    Send-Notification -Cfg $cfg -Status "ERROR" -Message ("Insufficient disk space on " + $script:RootDir)
    exit 1
}

# 6. Compare versions
$verUrl    = $BaseUrl + "/version.txt"
$remoteVer = Get-RemoteVersion -VerUrl $verUrl -MaxRetries $cfg.retry_max -Delays $cfg.retry_delays_sec
$localVer  = Get-LocalVersion

if ($null -eq $remoteVer) {
    Write-Log "WARN" "Remote version unreachable -- cycle skipped"
    exit 0
}

if ($remoteVer -eq $localVer) {
    Write-Log "INFO" ("Already up to date: " + $localVer)
    exit 0
}

Write-Log "INFO" ("Update: " + $localVer + " -> " + $remoteVer)

# 7. Backup current version
Backup-CurrentVersion -Cfg $cfg

# 8. Stop app if requested
Stop-AppProcess -Cfg $cfg

# 9. Download and install
$TempDir     = Join-Path $env:TEMP ("GH_Update_" + $cfg.app_folder)
$ZipPath     = Join-Path $TempDir "download.zip"
$ExtractPath = Join-Path $TempDir "extracted"

if (Test-Path $TempDir) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue }
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

if (-not (Download-WithRetry -Url ($BaseUrl + "/" + $cfg.zip_path) -Dest $ZipPath -MaxRetries $cfg.retry_max -Delays $cfg.retry_delays_sec)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Send-Notification -Cfg $cfg -Status "ERROR" -Message "ZIP download failed"
    exit 1
}

if (-not (Expand-Archive-Compat -ZipFile $ZipPath -OutPath $ExtractPath)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Send-Notification -Cfg $cfg -Status "ERROR" -Message "ZIP extraction failed"
    exit 1
}

$realSource = Resolve-ExtractRoot -Path $ExtractPath

if (-not (Copy-ProjectFiles -Src $realSource -Dest $script:ProjectDir)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "INFO" "Copy failed -- attempting rollback..."
    if (Invoke-Rollback -Cfg $cfg) {
        Send-Notification -Cfg $cfg -Status "ERROR" -Message ("Copy failed -- rolled back to " + $localVer)
    } else {
        Send-Notification -Cfg $cfg -Status "ERROR" -Message "Copy failed -- rollback not possible"
    }
    exit 1
}

Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
Write-Log "INFO" "Temp folder cleaned"

# 10. Download extra files
Get-ExtraFiles -Cfg $cfg | Out-Null

# 11. Run setup.py
if (-not (Invoke-SetupScript -Cfg $cfg)) {
    Write-Log "ERROR" "setup.py failed -- attempting rollback..."
    if (Invoke-Rollback -Cfg $cfg) {
        Invoke-SetupScript -Cfg $cfg | Out-Null
        Send-Notification -Cfg $cfg -Status "ERROR" -Message ("setup.py failed -- rolled back to " + $localVer)
    } else {
        Send-Notification -Cfg $cfg -Status "ERROR" -Message "setup.py failed -- rollback not possible"
    }
    exit 1
}

# 12. Save new version and applied state
Set-Content -Path $script:LocalVerFile -Value $remoteVer -Encoding UTF8
Save-AppliedState -Path $AppliedPath -Cfg $cfg -Version $remoteVer
Write-Log "INFO" ("Version saved: " + $remoteVer)

# 13. Restart app if requested
Start-AppProcess -Cfg $cfg

Send-Notification -Cfg $cfg -Status "SUCCESS" -Message ("Update successful: " + $localVer + " -> " + $remoteVer)
Write-Log "INFO" "====== UPDATE SUCCESS: $remoteVer ======"
exit 0