# ================================================================
# updater.ps1  —  Server-First Edition v4.0
# Heberge sur GitHub, telecharge frais a chaque execution
# Usage : powershell -File updater.ps1 -BaseUrl "https://raw.githubusercontent.com/USER/REPO/BRANCH"
# Compatible Windows 7 SP1 / 8 / 8.1 / 10 / 11
# ================================================================
param(
    [Parameter(Mandatory = $true)][string]$BaseUrl
)

# ----------------------------------------------------------------
# TLS 1.2 — obligatoire pour GitHub sur Windows 7
# ----------------------------------------------------------------
try {
    [Net.ServicePointManager]::SecurityProtocol = [Enum]::ToObject([Net.SecurityProtocolType], 3072)
} catch {
    try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls } catch {}
}

# ----------------------------------------------------------------
# Detection des capacites runtime
# ----------------------------------------------------------------
$_hasZipFile = $false
try {
    [System.Reflection.Assembly]::LoadWithPartialName("System.IO.Compression.FileSystem") | Out-Null
    $null = [System.IO.Compression.ZipFile]
    $_hasZipFile = $true
} catch {}

$_useModernTask = ($null -ne (Get-Command Register-ScheduledTask -ErrorAction SilentlyContinue))

# ----------------------------------------------------------------
# Chemins de base (avant lecture config — utilises par le logger)
# ----------------------------------------------------------------
$AppDataRoot  = [Environment]::GetFolderPath("LocalApplicationData")
$LauncherDir  = Join-Path $AppDataRoot ("GH_" + ($BaseUrl -split "/" | Select-Object -Last 2 | Select-Object -First 1))
$AppliedPath  = Join-Path $LauncherDir "applied.json"

# Log bootstrap (chemin provisoire, mis a jour apres lecture config)
$script:LogDir = $LauncherDir
if (-not (Test-Path $script:LogDir)) { New-Item -ItemType Directory -Path $script:LogDir -Force | Out-Null }

# ----------------------------------------------------------------
# Helpers reseau
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
# Logging (semaine ISO, fallback annee-mois sur PS 2.0)
# ----------------------------------------------------------------
function Write-Log {
    param([string]$Level, [string]$Message)
    try   { $week = Get-Date -UFormat "%Y-W%V" }
    catch { $week = Get-Date -Format "yyyy-MM" }
    $line = "[" + (Get-Date -Format "yyyy-MM-dd HH:mm:ss") + "] [$Level] $Message"
    $logFile = Join-Path $script:LogDir ("update_" + $week + ".log")
    if (-not (Test-Path $script:LogDir)) { New-Item -ItemType Directory -Path $script:LogDir -Force | Out-Null }
    Add-Content -Path $logFile -Value $line -Encoding UTF8
    if ($null -ne $script:LogKeepWeeks -and $script:LogKeepWeeks -gt 0) {
        Get-ChildItem $script:LogDir -Filter "update_*.log" -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending |
            Select-Object -Skip $script:LogKeepWeeks |
            Remove-Item -Force -ErrorAction SilentlyContinue
    }
}

# ----------------------------------------------------------------
# Lecture config.json depuis GitHub
# ----------------------------------------------------------------
function Read-ServerConfig {
    param([string]$Url)
    try {
        $wc  = New-NoCacheWebClient
        $raw = $wc.DownloadString($Url + "?nc=" + (Get-UnixMs)).Trim()
        $wc.Dispose()

        # ConvertFrom-Json (PS 3+) avec fallback JavaScriptSerializer (PS 2 / .NET 3.5)
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
            zip_path          = [string]$obj.zip_path
            app_folder        = [string]$obj.app_folder
            python_exe        = [string]$obj.python_exe
            setup_script      = [string]$obj.setup_script
            task_name         = if ($obj.task_name)         { [string]$obj.task_name }         else { "GH_AutoUpdate" }
            task_interval_min = if ($obj.task_interval_min) { [int]$obj.task_interval_min }    else { 60 }
            log_keep_weeks    = if ($obj.log_keep_weeks)    { [int]$obj.log_keep_weeks }        else { 2 }
            retry_max         = if ($obj.retry_max)         { [int]$obj.retry_max }             else { 5 }
            retry_delays_sec  = $delays
            update_enabled    = if ($null -ne $obj.update_enabled)    { [bool]$obj.update_enabled }    else { $true }
            kill_before_update = if ($null -ne $obj.kill_before_update) { [bool]$obj.kill_before_update } else { $false }
            kill_process_name  = if ($obj.kill_process_name) { [string]$obj.kill_process_name } else { "" }
            restart_after      = if ($null -ne $obj.restart_after)    { [bool]$obj.restart_after }    else { $false }
            restart_exe        = if ($obj.restart_exe)      { [string]$obj.restart_exe }        else { "" }
            min_free_mb        = if ($obj.min_free_mb)      { [int]$obj.min_free_mb }           else { 100 }
            rollback_enabled   = if ($null -ne $obj.rollback_enabled) { [bool]$obj.rollback_enabled } else { $false }
            backup_versions    = if ($obj.backup_versions)  { [int]$obj.backup_versions }       else { 2 }
            notify_on_success  = if ($null -ne $obj.notify_on_success) { [bool]$obj.notify_on_success } else { $false }
            notify_on_error    = if ($null -ne $obj.notify_on_error)   { [bool]$obj.notify_on_error }   else { $false }
            webhook_url        = if ($obj.webhook_url)      { [string]$obj.webhook_url }        else { "" }
            extra_files        = $extra
        }
    } catch {
        return $null
    }
}

# ----------------------------------------------------------------
# Lecture / sauvegarde applied.json
# ----------------------------------------------------------------
function Read-AppliedState {
    param([string]$Path)
    if (-not (Test-Path $Path)) { return $null }
    try {
        $raw = Get-Content $Path -Raw
        $obj = $raw | ConvertFrom-Json
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
    # ConvertTo-Json (PS 3+) avec fallback JavaScriptSerializer
    try {
        $json = $state | ConvertTo-Json
    } catch {
        Add-Type -AssemblyName System.Web.Extensions -ErrorAction Stop
        $jss  = New-Object System.Web.Script.Serialization.JavaScriptSerializer
        $json = $jss.Serialize($state)
    }
    Set-Content -Path $Path -Value $json -Encoding UTF8
}

# ----------------------------------------------------------------
# Enregistrement / recreation de la tache planifiee
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
        [System.IO.File]::WriteAllText($xmlPath, @"
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
    <Hidden>true</Hidden><ExecutionTimeLimit>PT30M</ExecutionTimeLimit>
    <StartWhenAvailable>true</StartWhenAvailable><Enabled>true</Enabled>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <RestartOnFailure><Interval>PT5M</Interval><Count>3</Count></RestartOnFailure>
  </Settings>
  <Actions Context="Author"><Exec>
    <Command>wscript.exe</Command><Arguments>"$LauncherPath"</Arguments>
  </Exec></Actions>
</Task>
"@, [System.Text.Encoding]::Unicode)
        & schtasks.exe /Create /F /TN $TaskName /XML $xmlPath 2>&1 | Out-Null
        Remove-Item $xmlPath -Force -ErrorAction SilentlyContinue
    }
}

# ----------------------------------------------------------------
# Reconciliation infrastructure
# Compare config desiree (GitHub) vs etat applique (applied.json)
# Applique les changements structurels avant toute MAJ de version
# ----------------------------------------------------------------
function Invoke-Reconciliation {
    param([hashtable]$Cfg, $Applied)

    $launcherVBS = Join-Path $LauncherDir "Launcher.vbs"

    # --- app_folder a change
    if ($null -ne $Applied -and $Applied.app_folder -ne "" -and $Applied.app_folder -ne $Cfg.app_folder) {
        Write-Log "INFO" ("app_folder change : " + $Applied.app_folder + " -> " + $Cfg.app_folder)
        $oldRoot = Join-Path $AppDataRoot $Applied.app_folder
        $newRoot = Join-Path $AppDataRoot $Cfg.app_folder

        if (Test-Path $oldRoot) {
            if (-not (Test-Path $newRoot)) {
                try {
                    Move-Item -Path $oldRoot -Destination $newRoot -Force
                    Write-Log "INFO" ("Dossier deplace : " + $oldRoot + " -> " + $newRoot)
                } catch {
                    Write-Log "WARN" ("Move-Item echoue, tentative robocopy : " + $_.Exception.Message)
                    New-Item -ItemType Directory -Path $newRoot -Force | Out-Null
                    & robocopy $oldRoot $newRoot /E /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1 | Out-Null
                    if ($LASTEXITCODE -lt 8) {
                        Remove-Item $oldRoot -Recurse -Force -ErrorAction SilentlyContinue
                        Write-Log "INFO" "Deplacement via robocopy OK"
                    } else {
                        Write-Log "ERROR" "Echec deplacement dossier"
                    }
                }
            } else {
                Write-Log "INFO" ("Nouveau dossier existe deja — suppression ancien : " + $oldRoot)
                Remove-Item $oldRoot -Recurse -Force -ErrorAction SilentlyContinue
            }
        }

        # Mettre a jour les chemins de script
        $script:RootDir      = $newRoot
        $script:ProjectDir   = Join-Path $newRoot "project"
        $script:LogDir       = Join-Path $newRoot "logs"
        $script:BackupDir    = Join-Path $newRoot "backups"
        $script:LocalVerFile = Join-Path $newRoot "version.txt"
    }

    # --- Tache planifiee : nom ou intervalle a change
    $taskChanged = (
        $null -ne $Applied -and (
            ($Applied.task_name -ne "" -and $Applied.task_name -ne $Cfg.task_name) -or
            ($Applied.task_interval_min -gt 0 -and $Applied.task_interval_min -ne $Cfg.task_interval_min)
        )
    )

    if ($taskChanged) {
        Write-Log "INFO" ("Tache modifiee : " + $Applied.task_name + " (" + $Applied.task_interval_min + "min) -> " + $Cfg.task_name + " (" + $Cfg.task_interval_min + "min)")
        if ($Applied.task_name -ne "" -and $Applied.task_name -ne $Cfg.task_name) {
            & schtasks.exe /Delete /TN $Applied.task_name /F 2>&1 | Out-Null
            Write-Log "INFO" ("Ancienne tache supprimee : " + $Applied.task_name)
        }
        Register-UpdaterTask -TaskName $Cfg.task_name -IntervalMin $Cfg.task_interval_min -LauncherPath $launcherVBS
        Write-Log "INFO" ("Nouvelle tache enregistree : " + $Cfg.task_name + " toutes les " + $Cfg.task_interval_min + " min")
    }

    # Reconstruire les chemins derives (cas normal ou apres renommage)
    $script:RootDir      = Join-Path $AppDataRoot $Cfg.app_folder
    $script:ProjectDir   = Join-Path $script:RootDir "project"
    $script:LogDir       = Join-Path $script:RootDir "logs"
    $script:BackupDir    = Join-Path $script:RootDir "backups"
    $script:LocalVerFile = Join-Path $script:RootDir "version.txt"
    $script:LogKeepWeeks = $Cfg.log_keep_weeks

    foreach ($d in @($script:RootDir, $script:ProjectDir, $script:LogDir)) {
        if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
    }
}

# ----------------------------------------------------------------
# Gestion des versions / rollback
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
        Write-Log "INFO" ("Backup OK : version " + $localVer)
    } else {
        Write-Log "WARN" ("Backup echoue pour version " + $localVer)
    }

    # Purger les backups en exces
    $allBackups = @(Get-ChildItem $script:BackupDir -Directory -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending)
    if ($allBackups.Count -gt $Cfg.backup_versions) {
        $allBackups | Select-Object -Skip $Cfg.backup_versions | ForEach-Object {
            Remove-Item $_.FullName -Recurse -Force -ErrorAction SilentlyContinue
            Write-Log "INFO" ("Backup purge : " + $_.Name)
        }
    }
}

function Invoke-Rollback {
    param([hashtable]$Cfg)
    if (-not $Cfg.rollback_enabled) { return $false }
    if (-not (Test-Path $script:BackupDir)) { Write-Log "WARN" "Aucun backup disponible"; return $false }

    $latest = Get-ChildItem $script:BackupDir -Directory -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
    if ($null -eq $latest) { Write-Log "WARN" "Dossier backup vide"; return $false }

    Write-Log "INFO" ("Rollback vers : " + $latest.Name)
    & robocopy $latest.FullName $script:ProjectDir /E /PURGE /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1 | Out-Null
    if ($LASTEXITCODE -lt 8) {
        Set-Content -Path $script:LocalVerFile -Value $latest.Name -Encoding UTF8
        Write-Log "INFO" ("Rollback reussi : " + $latest.Name)
        return $true
    }
    Write-Log "ERROR" "Rollback echoue"
    return $false
}

# ----------------------------------------------------------------
# Notification webhook (Slack / Teams / Discord / custom)
# ----------------------------------------------------------------
function Send-Notification {
    param([hashtable]$Cfg, [string]$Status, [string]$Message)

    if ($Cfg.webhook_url -eq "") { return }
    if ($Status -eq "SUCCESS" -and -not $Cfg.notify_on_success) { return }
    if ($Status -eq "ERROR"   -and -not $Cfg.notify_on_error)   { return }

    try {
        $body = '{"text":"[AutoUpdate ' + $Cfg.app_folder + '] ' + $Status + ' — ' + $Message.Replace('"','\"') + '"}'
        $wc   = New-NoCacheWebClient
        $wc.Headers.Add("Content-Type", "application/json")
        $wc.UploadString($Cfg.webhook_url, "POST", $body) | Out-Null
        $wc.Dispose()
        Write-Log "INFO" ("Notification " + $Status + " envoyee")
    } catch {
        Write-Log "WARN" ("Notification echouee : " + $_.Exception.Message)
    }
}

# ----------------------------------------------------------------
# Verification espace disque libre
# ----------------------------------------------------------------
function Test-DiskSpace {
    param([int]$MinFreeMb)
    try {
        $drive = [System.IO.Path]::GetPathRoot($script:RootDir)
        $disk  = Get-PSDrive ($drive.TrimEnd('\').TrimEnd(':')) -ErrorAction SilentlyContinue
        if ($null -eq $disk) { return $true }
        $freeMb = [math]::Round($disk.Free / 1MB, 0)
        if ($freeMb -lt $MinFreeMb) {
            Write-Log "ERROR" ("Espace insuffisant : " + $freeMb + " MB libres, minimum requis : " + $MinFreeMb + " MB")
            return $false
        }
        return $true
    } catch {
        return $true
    }
}

# ----------------------------------------------------------------
# Telechargement avec retry
# ----------------------------------------------------------------
function Download-WithRetry {
    param([string]$Url, [string]$Dest, [int]$MaxRetries, [array]$Delays)
    for ($i = 1; $i -le $MaxRetries; $i++) {
        Write-Log "INFO" ("Telechargement tentative " + $i + "/" + $MaxRetries)
        try {
            $wc = New-NoCacheWebClient
            $wc.DownloadFile($Url, $Dest)
            $wc.Dispose()
            if ((Test-Path $Dest) -and (Get-Item $Dest).Length -gt 1024) {
                Write-Log "INFO" ("OK — " + [math]::Round((Get-Item $Dest).Length / 1KB, 1) + " KB")
                return $true
            }
            Write-Log "WARN" "Fichier trop petit — possible 404"
        } catch {
            Write-Log "WARN" ("Erreur reseau tentative " + $i + " : " + $_.Exception.Message)
        }
        if ($i -lt $MaxRetries) {
            $wait = if ($i - 1 -lt $Delays.Count) { $Delays[$i - 1] } else { 120 }
            Write-Log "INFO" ("Nouvel essai dans " + $wait + " secondes")
            Start-Sleep -Seconds $wait
        }
    }
    Write-Log "ERROR" ("Telechargement echoue apres " + $MaxRetries + " tentatives")
    return $false
}

# ----------------------------------------------------------------
# Extraction ZIP
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
        Write-Log "ERROR" ("Extraction : " + $_.Exception.Message)
        return $false
    }
}

# ----------------------------------------------------------------
# Detection du dossier racine dans le ZIP
# ----------------------------------------------------------------
function Resolve-ExtractRoot {
    param([string]$Path)
    $canon = (Resolve-Path $Path).Path
    $items = @(Get-ChildItem $canon -ErrorAction SilentlyContinue)
    if ($items.Count -eq 1 -and $items[0].PSIsContainer) {
        Write-Log "INFO" ("Wrapper detecte : " + $items[0].Name + " — suppression")
        return (Resolve-Path $items[0].FullName).Path
    }
    return $canon
}

# ----------------------------------------------------------------
# Copie des fichiers vers ProjectDir
# ----------------------------------------------------------------
function Copy-ProjectFiles {
    param([string]$Src, [string]$Dest)
    try {
        if (-not (Test-Path $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }
        & robocopy $Src $Dest /E /PURGE /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1 | Out-Null
        if ($LASTEXITCODE -lt 8) {
            Write-Log "INFO" ("Copie OK robocopy (exit " + $LASTEXITCODE + ")")
            return $true
        }
        Write-Log "WARN" ("robocopy exit " + $LASTEXITCODE + " — fallback Copy-Item")
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
        Write-Log "INFO" "Copie OK (Copy-Item fallback)"
        return $true
    } catch {
        try { Pop-Location } catch {}
        Write-Log "ERROR" ("Copie : " + $_.Exception.Message)
        return $false
    }
}

# ----------------------------------------------------------------
# Telechargement des fichiers supplementaires
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
            Write-Log "INFO" ("Fichier extra : " + $url)
            $dlOk = Download-WithRetry -Url $url -Dest $destFull -MaxRetries $Cfg.retry_max -Delays $Cfg.retry_delays_sec
            if (-not $dlOk) { Write-Log "WARN" ("Fichier extra echoue : " + $url); $ok = $false }
        } catch {
            Write-Log "WARN" ("Erreur extra_files : " + $_.Exception.Message)
            $ok = $false
        }
    }
    return $ok
}

# ----------------------------------------------------------------
# Arret du processus applicatif avant MAJ
# ----------------------------------------------------------------
function Stop-AppProcess {
    param([hashtable]$Cfg)
    if (-not $Cfg.kill_before_update -or $Cfg.kill_process_name -eq "") { return }
    try {
        $procs = Get-Process -Name ($Cfg.kill_process_name -replace "\.exe$","") -ErrorAction SilentlyContinue
        if ($procs) {
            $procs | Stop-Process -Force -ErrorAction SilentlyContinue
            Write-Log "INFO" ("Processus arrete : " + $Cfg.kill_process_name)
            Start-Sleep -Seconds 2
        }
    } catch {
        Write-Log "WARN" ("Stop-AppProcess : " + $_.Exception.Message)
    }
}

# ----------------------------------------------------------------
# Demarrage de l'application apres MAJ
# ----------------------------------------------------------------
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
            Write-Log "INFO" ("Application redemarree : " + $exePath)
        } else {
            Write-Log "WARN" ("restart_exe introuvable : " + $exePath)
        }
    } catch {
        Write-Log "WARN" ("Start-AppProcess : " + $_.Exception.Message)
    }
}

# ----------------------------------------------------------------
# Execution de setup.py
# ----------------------------------------------------------------
function Invoke-SetupScript {
    param([hashtable]$Cfg)
    $pyPath    = Join-Path $script:ProjectDir $Cfg.python_exe
    $setupPath = Join-Path $script:ProjectDir $Cfg.setup_script
    if (-not (Test-Path $pyPath)) {
        Write-Log "ERROR" ("Python introuvable : " + $pyPath)
        return $false
    }
    if (-not (Test-Path $setupPath)) {
        Write-Log "ERROR" ("setup.py introuvable : " + $setupPath)
        return $false
    }
    try {
        Write-Log "INFO" ("Execution : " + $Cfg.python_exe + " " + $Cfg.setup_script)
        $psi                  = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName         = $pyPath
        $psi.Arguments        = '"' + $setupPath + '"'
        $psi.WorkingDirectory = $script:ProjectDir
        $psi.WindowStyle      = [Diagnostics.ProcessWindowStyle]::Hidden
        $psi.CreateNoWindow   = $true
        $psi.UseShellExecute  = $false
        $proc = [Diagnostics.Process]::Start($psi)
        $proc.WaitForExit()
        Write-Log "INFO" ("setup.py exit code : " + $proc.ExitCode)
        if ($proc.ExitCode -ne 0) {
            Write-Log "WARN" ("setup.py code non-zero : " + $proc.ExitCode)
        }
        return $true
    } catch {
        Write-Log "ERROR" ("Lancement Python : " + $_.Exception.Message)
        return $false
    }
}

# ----------------------------------------------------------------
# Lecture version distante avec retry
# ----------------------------------------------------------------
function Get-RemoteVersion {
    param([string]$VerUrl, [int]$MaxRetries, [array]$Delays)
    for ($i = 1; $i -le $MaxRetries; $i++) {
        try {
            $wc  = New-NoCacheWebClient
            $raw = $wc.DownloadString($VerUrl + "?nc=" + (Get-UnixMs)).Trim()
            $wc.Dispose()
            if ($raw.Length -gt 0) {
                Write-Log "INFO" ("Version distante : " + $raw)
                return $raw
            }
            Write-Log "WARN" "version.txt vide"
        } catch {
            Write-Log "WARN" ("Fetch version tentative " + $i + " : " + $_.Exception.Message)
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
        Write-Log "INFO" "Premiere installation (pas de version.txt local)"
        return $null
    }
    $v = (Get-Content $script:LocalVerFile -Raw).Trim()
    Write-Log "INFO" ("Version locale : " + $v)
    return $v
}

# ================================================================
# LOGIQUE PRINCIPALE
# ================================================================
Write-Log "INFO" "====== UPDATER START (v4.0) BaseUrl: $BaseUrl ======"

# --- 1. Lire la config serveur
$cfg = Read-ServerConfig -Url ($BaseUrl + "/config.json")
if ($null -eq $cfg) {
    Write-Log "ERROR" "Impossible de lire config.json"
    exit 1
}
Write-Log "INFO" ("Config chargee : " + $cfg.app_folder + " / tache : " + $cfg.task_name)

# --- 2. Lire l'etat applique localement
$applied = Read-AppliedState -Path $AppliedPath

# --- 3. Reconcilier l'infrastructure (renommage dossier, recreation tache)
Invoke-Reconciliation -Cfg $cfg -Applied $applied

# --- 4. Verifier si les MAJ sont activees
if (-not $cfg.update_enabled) {
    Write-Log "INFO" "update_enabled=false — cycle ignore"
    exit 0
}

# --- 5. Verifier l'espace disque
if (-not (Test-DiskSpace -MinFreeMb $cfg.min_free_mb)) {
    Send-Notification -Cfg $cfg -Status "ERROR" -Message ("Espace disque insuffisant sur " + $script:RootDir)
    exit 1
}

# --- 6. Comparer les versions
$verUrl    = $BaseUrl + "/version.txt"
$remoteVer = Get-RemoteVersion -VerUrl $verUrl -MaxRetries $cfg.retry_max -Delays $cfg.retry_delays_sec
$localVer  = Get-LocalVersion

if ($null -eq $remoteVer) {
    Write-Log "WARN" "Version distante inaccessible — cycle ignore"
    exit 0
}

if ($remoteVer -eq $localVer) {
    Write-Log "INFO" ("Deja a jour : " + $localVer)
    exit 0
}

Write-Log "INFO" ("Mise a jour : " + $localVer + " -> " + $remoteVer)

# --- 7. Backup de la version actuelle
Backup-CurrentVersion -Cfg $cfg

# --- 8. Arreter l'application si demande
Stop-AppProcess -Cfg $cfg

# --- 9. Telecharger et installer
$TempDir     = Join-Path $env:TEMP ("GH_Update_" + $cfg.app_folder)
$ZipPath     = Join-Path $TempDir "download.zip"
$ExtractPath = Join-Path $TempDir "extracted"

if (Test-Path $TempDir) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue }
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

$zipUrl = $BaseUrl + "/" + $cfg.zip_path

if (-not (Download-WithRetry -Url $zipUrl -Dest $ZipPath -MaxRetries $cfg.retry_max -Delays $cfg.retry_delays_sec)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Send-Notification -Cfg $cfg -Status "ERROR" -Message "Echec telechargement ZIP"
    exit 1
}

if (-not (Expand-Archive-Compat -ZipFile $ZipPath -OutPath $ExtractPath)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Send-Notification -Cfg $cfg -Status "ERROR" -Message "Echec extraction ZIP"
    exit 1
}

$realSource = Resolve-ExtractRoot -Path $ExtractPath

if (-not (Copy-ProjectFiles -Src $realSource -Dest $script:ProjectDir)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "INFO" "Tentative de rollback..."
    if (Invoke-Rollback -Cfg $cfg) {
        Send-Notification -Cfg $cfg -Status "ERROR" -Message ("Copie echouee — rollback effectue vers " + $localVer)
    } else {
        Send-Notification -Cfg $cfg -Status "ERROR" -Message "Copie echouee — rollback impossible"
    }
    exit 1
}

Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
Write-Log "INFO" "Dossier temp nettoye"

# --- 10. Telecharger les fichiers supplementaires
Get-ExtraFiles -Cfg $cfg | Out-Null

# --- 11. Executer setup.py
if (-not (Invoke-SetupScript -Cfg $cfg)) {
    Write-Log "ERROR" "setup.py a echoue"
    Write-Log "INFO" "Tentative de rollback..."
    if (Invoke-Rollback -Cfg $cfg) {
        Invoke-SetupScript -Cfg $cfg | Out-Null
        Send-Notification -Cfg $cfg -Status "ERROR" -Message ("setup.py echoue — rollback effectue vers " + $localVer)
    } else {
        Send-Notification -Cfg $cfg -Status "ERROR" -Message "setup.py echoue — rollback impossible"
    }
    exit 1
}

# --- 12. Sauvegarder la nouvelle version et l'etat applique
Set-Content -Path $script:LocalVerFile -Value $remoteVer -Encoding UTF8
Save-AppliedState -Path $AppliedPath -Cfg $cfg -Version $remoteVer
Write-Log "INFO" ("Version sauvegardee : " + $remoteVer)

# --- 13. Redemarrer l'application si demande
Start-AppProcess -Cfg $cfg

Send-Notification -Cfg $cfg -Status "SUCCESS" -Message ("Mise a jour reussie : " + $localVer + " -> " + $remoteVer)
Write-Log "INFO" "====== UPDATE SUCCESS : $remoteVer ======"
exit 0