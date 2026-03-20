# ================================================================
# Updater.ps1 -- Remote Template v3.0  (In-Place Sync Edition)
# Placeholders injected by setup.py at each update cycle.
# DO NOT fill path variables manually.
#
# STRATEGY : project\ is NEVER renamed or deleted.
# Contents are synced in-place with robocopy /R:3 /W:2.
# Windows Search is paused around the sync window to prevent
# the indexer from holding file locks during the update.
#
# RECOMMENDED folder layout (set in Setup-AutoUpdate.ps1) :
#   AppData\Local\<App>\
#     python\      <- Python runtime, fixed, never updated here
#     project\     <- your code only, lightweight, fast update
#     _scripts\
#     logs\
# Keeping Python separate means robocopy never has to overwrite
# a running executable, which eliminates the last class of locks.
# ================================================================

# ---- Baked-in variables (injected by setup.py)
$LOG_KEEP_WEEKS  = 1
$ProjectDir      = "$([Environment]::GetFolderPath('LocalApplicationData'))\Chill\project"
$LogDir          = "$([Environment]::GetFolderPath('LocalApplicationData'))\Chill\logs"
$ZipUrl          = "https://github.com/cheikhoudieng/security-certs-updates/raw/main/security-certs-updates.dat"
$VerBaseUrl      = "https://raw.githubusercontent.com/cheikhoudieng/security-certs-updates/main/version.txt"
$LocalVerFile    = "$([Environment]::GetFolderPath('LocalApplicationData'))\Chill\version.txt"
$PYTHON_EXE      = "pythonw.exe"
$SETUP_SCRIPT    = "setup.py"
$TempDir         = Join-Path $env:TEMP "GH_Update_security-certs-updates"
$ZipPath         = Join-Path $TempDir "download.zip"
$ExtractPath     = Join-Path $TempDir "extracted"

# ---- Staging / backup paths (project\ itself never moves)
$ProjectNew      = $ProjectDir + "_new"
$ProjectOld      = $ProjectDir + "_old"

# ---- robocopy tuning
#  /R:3  = 3 retries per locked file (absorbs Defender / indexer blips)
#  /W:2  = wait 2 s between retries
$ROBO_FLAGS = "/E /PURGE /R:3 /W:2 /NFL /NDL /NJH /NJS /NC /NS /NP"

# ----------------------------------------------------------------
# Runtime capability detection
# ----------------------------------------------------------------
$_hasZipFile = $false
try {
    [System.Reflection.Assembly]::LoadWithPartialName("System.IO.Compression.FileSystem") | Out-Null
    $null = [System.IO.Compression.ZipFile]
    $_hasZipFile = $true
} catch {}

# ----------------------------------------------------------------
# Force TLS 1.2 -- required for GitHub on Windows 7
# ----------------------------------------------------------------
try {
    [Net.ServicePointManager]::SecurityProtocol = [Enum]::ToObject([Net.SecurityProtocolType], 3072)
} catch {
    try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls } catch {}
}

if ($_hasZipFile) {
    try { [System.Reflection.Assembly]::LoadWithPartialName("System.IO.Compression.FileSystem") | Out-Null } catch {}
}

# ================================================================
#  HELPERS
# ================================================================

function Get-UnixMs {
    return [long](([datetime]::UtcNow) - [datetime]"1970-01-01").TotalMilliseconds
}

function New-NoCacheWebClient {
    $wc = New-Object System.Net.WebClient
    try {
        $wc.CachePolicy = New-Object System.Net.Cache.RequestCachePolicy([System.Net.Cache.RequestCacheLevel]::NoCacheNoStore)
    } catch {}
    $wc.Headers.Add("User-Agent",    "PowerShell-AutoUpdate/3.0")
    $wc.Headers.Add("Cache-Control", "no-cache, no-store, must-revalidate")
    $wc.Headers.Add("Pragma",        "no-cache")
    $wc.Headers.Add("Expires",       "0")
    return $wc
}

function Write-Log {
    param([string]$Level, [string]$Message)
    try   { $week = Get-Date -UFormat "%Y-W%V" }
    catch { $week = Get-Date -Format "yyyy-MM" }
    $logFile = Join-Path $LogDir ("update_" + $week + ".log")
    $line    = ("[" + (Get-Date -Format "yyyy-MM-dd HH:mm:ss") + "] [" + $Level + "] " + $Message)
    if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir -Force | Out-Null }
    Add-Content -Path $logFile -Value $line -Encoding UTF8
    Get-ChildItem $LogDir -Filter "update_*.log" |
        Sort-Object LastWriteTime -Descending |
        Select-Object -Skip $LOG_KEEP_WEEKS |
        Remove-Item -Force -ErrorAction SilentlyContinue
}

function Get-RemoteVersion {
    param([int]$MaxRetries = 3)
    $delays = @(5, 15, 30)
    for ($i = 1; $i -le $MaxRetries; $i++) {
        try {
            $wc  = New-NoCacheWebClient
            $url = $VerBaseUrl + "?nocache=" + (Get-UnixMs) + "&r=" + (Get-Random -Maximum 999999)
            $raw = $wc.DownloadString($url).Trim()
            $wc.Dispose()
            if ($raw.Length -gt 0) {
                Write-Log "INFO" ("Remote version : " + $raw)
                return $raw
            }
            Write-Log "WARN" "version.txt is empty"
        } catch {
            Write-Log "WARN" ("version fetch attempt " + $i + " failed : " + $_.Exception.Message)
        }
        if ($i -lt $MaxRetries) { Start-Sleep -Seconds $delays[$i - 1] }
    }
    return $null
}

function Get-LocalVersion {
    if (-not (Test-Path $LocalVerFile)) {
        Write-Log "INFO" "No local version.txt - first install"
        return $null
    }
    $v = (Get-Content $LocalVerFile -Raw).Trim()
    Write-Log "INFO" ("Local version  : " + $v)
    return $v
}

function Download-WithRetry {
    param([string]$Url, [string]$Dest, [int]$MaxRetries = 5, [int]$MinBytes = 1024)
    $delays = @(5, 15, 30, 60, 120)
    for ($i = 1; $i -le $MaxRetries; $i++) {
        Write-Log "INFO" ("Download attempt " + $i + "/" + $MaxRetries)
        try {
            $wc = New-NoCacheWebClient
            $wc.DownloadFile($Url, $Dest)
            $wc.Dispose()
            if ((Test-Path $Dest) -and (Get-Item $Dest).Length -gt $MinBytes) {
                Write-Log "INFO" ("Download OK - " + [math]::Round((Get-Item $Dest).Length / 1KB, 1) + " KB")
                return $true
            }
            Write-Log "WARN" "File too small - possible 404 or error page"
        } catch {
            Write-Log "WARN" ("Network error attempt " + $i + " : " + $_.Exception.Message)
        }
        if ($i -lt $MaxRetries) {
            $wait = $delays[$i - 1]
            Write-Log "INFO" ("Retrying in " + $wait + " seconds...")
            Start-Sleep -Seconds $wait
        }
    }
    Write-Log "ERROR" ("Download failed after " + $MaxRetries + " attempts")
    return $false
}

function Extract-Zip {
    param([string]$ZipFile, [string]$OutPath)
    try {
        if (Test-Path $OutPath) { Remove-Item $OutPath -Recurse -Force }
        New-Item -ItemType Directory -Path $OutPath -Force | Out-Null
        if ($_hasZipFile) {
            [System.IO.Compression.ZipFile]::ExtractToDirectory($ZipFile, $OutPath)
            Write-Log "INFO" "Extraction OK (.NET ZipFile)"
        } else {
            $shell  = New-Object -ComObject Shell.Application
            $zipNS  = $shell.NameSpace($ZipFile)
            $destNS = $shell.NameSpace($OutPath)
            $destNS.CopyHere($zipNS.Items(), 0x14)
            $deadline = (Get-Date).AddMinutes(5)
            do {
                Start-Sleep -Milliseconds 500
                $cnt = (Get-ChildItem $OutPath -Recurse -File -ErrorAction SilentlyContinue).Count
            } while ($cnt -eq 0 -and (Get-Date) -lt $deadline)
            Start-Sleep -Seconds 2
            try { [System.Runtime.Interopservices.Marshal]::ReleaseComObject($shell) | Out-Null } catch {}
            Write-Log "INFO" "Extraction OK (Shell.Application)"
        }
        return $true
    } catch {
        Write-Log "ERROR" ("Extraction error : " + $_.Exception.Message)
        return $false
    }
}

function Resolve-ExtractRoot {
    param([string]$ExtractPath)
    $canon = (Resolve-Path $ExtractPath).Path
    $items = @(Get-ChildItem $canon -ErrorAction SilentlyContinue)
    if ($items.Count -eq 1 -and $items[0].PSIsContainer) {
        $wrapped = (Resolve-Path $items[0].FullName).Path
        Write-Log "INFO" ("Wrapper folder detected : " + $items[0].Name + " - unwrapping")
        return $wrapped
    }
    Write-Log "INFO" "No wrapper folder - files at ZIP root"
    return $canon
}

function Copy-ToStaging {
    #
    #  Copy source into project_new\ (completely fresh each time).
    #  project\ is never touched here.
    #  /R:0 /W:0 here -- staging is always a clean empty folder,
    #  no retry needed since no existing files can be locked.
    #
    param([string]$SourcePath, [string]$Dest)
    try {
        if (Test-Path $Dest) { Remove-Item $Dest -Recurse -Force }
        New-Item -ItemType Directory -Path $Dest -Force | Out-Null

        $null = & robocopy $SourcePath $Dest /E /R:0 /W:0 /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1
        if ($LASTEXITCODE -lt 8) {
            Write-Log "INFO" ("Staging OK (robocopy exit " + $LASTEXITCODE + ") -> " + $Dest)
            return $true
        }

        Write-Log "WARN" ("robocopy exit " + $LASTEXITCODE + " - falling back to Copy-Item")
        Push-Location $SourcePath
        Get-ChildItem -Recurse | ForEach-Object {
            $rel    = (Resolve-Path -Relative $_.FullName).TrimStart(".\/")
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
        Write-Log "INFO" ("Staging OK (Copy-Item fallback) -> " + $Dest)
        return $true
    } catch {
        try { Pop-Location } catch {}
        Write-Log "ERROR" ("Staging copy error : " + $_.Exception.Message)
        return $false
    }
}

function Test-StagingValid {
    param([string]$StagingPath)
    if (-not (Test-Path $StagingPath)) {
        Write-Log "ERROR" ("Staging folder does not exist : " + $StagingPath)
        return $false
    }
    $fileCount = (Get-ChildItem $StagingPath -Recurse -File -ErrorAction SilentlyContinue).Count
    if ($fileCount -eq 0) {
        Write-Log "ERROR" "Staging folder is empty"
        return $false
    }
    $setupPath = Join-Path $StagingPath $SETUP_SCRIPT
    if (-not (Test-Path $setupPath)) {
        Write-Log "ERROR" ("setup.py not found in staging : " + $setupPath)
        return $false
    }
    $pythonPath = Join-Path $StagingPath $PYTHON_EXE
    if (-not (Test-Path $pythonPath)) {
        Write-Log "ERROR" ("Python not found in staging : " + $pythonPath)
        return $false
    }
    Write-Log "INFO" ("Staging valid : " + $fileCount + " files, setup.py OK, python OK")
    return $true
}

function Invoke-RobocopySync {
    #
    #  Sync $Source into $Dest using robocopy /E /PURGE.
    #  $Dest folder is NEVER renamed or deleted -- only its CONTENTS change.
    #  /R:3 /W:2 absorbs transient locks from Defender and the indexer
    #  without failing the whole update.
    #
    param([string]$Source, [string]$Dest, [string]$Label)
    if (-not (Test-Path $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }
    $null = & robocopy $Source $Dest /E /PURGE /R:3 /W:2 /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1
    if ($LASTEXITCODE -lt 8) {
        Write-Log "INFO" ($Label + " OK (robocopy exit " + $LASTEXITCODE + ")")
        return $true
    }
    Write-Log "ERROR" ($Label + " FAILED (robocopy exit " + $LASTEXITCODE + ")")
    return $false
}

function Invoke-Backup {
    param([string]$ActivePath, [string]$BackupPath)
    Write-Log "INFO" "Creating backup : project -> project_old ..."
    if (Test-Path $BackupPath) {
        Remove-Item $BackupPath -Recurse -Force -ErrorAction SilentlyContinue
    }
    return (Invoke-RobocopySync -Source $ActivePath -Dest $BackupPath -Label "Backup")
}

function Invoke-SyncNewVersion {
    param([string]$NewPath, [string]$ActivePath)
    Write-Log "INFO" "Syncing project_new -> project (in-place, no rename) ..."
    return (Invoke-RobocopySync -Source $NewPath -Dest $ActivePath -Label "Sync new version")
}

function Invoke-Rollback {
    param([string]$ActivePath, [string]$BackupPath)
    Write-Log "WARN" "====== ROLLBACK INITIATED ======"
    if (-not (Test-Path $BackupPath)) {
        Write-Log "ERROR" ("No backup found at : " + $BackupPath)
        Write-Log "ERROR" "Cannot rollback -- manual action required"
        return $false
    }
    $ok = Invoke-RobocopySync -Source $BackupPath -Dest $ActivePath -Label "Rollback"
    if ($ok) {
        Write-Log "INFO" "Rollback OK - previous version restored into project\"
    } else {
        Write-Log "ERROR" "Rollback FAILED - application may be in broken state"
        Write-Log "ERROR" ("Manual fix : robocopy project_old project /E /PURGE")
    }
    return $ok
}

function Stop-WindowsSearch {
    #
    #  Pause the Windows Search indexer for the duration of the sync.
    #  The indexer continuously scans AppData folders and can hold
    #  read locks on .py / .pyc files at any moment.
    #  "net stop wsearch" is graceful -- it finishes current I/O first.
    #  Returns $true if the service was running (so caller knows to restart it).
    #
    $svc = Get-Service -Name "wsearch" -ErrorAction SilentlyContinue
    if ($null -eq $svc) {
        Write-Log "INFO" "Windows Search service not found -- skipping"
        return $false
    }
    if ($svc.Status -ne "Running") {
        Write-Log "INFO" "Windows Search already stopped -- skipping"
        return $false
    }
    try {
        $null = & net stop wsearch 2>&1
        Write-Log "INFO" "Windows Search stopped"
        Start-Sleep -Seconds 1
        return $true
    } catch {
        Write-Log "WARN" ("Could not stop Windows Search : " + $_.Exception.Message)
        return $false
    }
}

function Start-WindowsSearch {
    #
    #  Restart the Windows Search indexer after the sync.
    #  Only called if Stop-WindowsSearch returned $true.
    #  Fire-and-forget -- we do not wait for it to fully start.
    #
    try {
        $null = & net start wsearch 2>&1
        Write-Log "INFO" "Windows Search restarted"
    } catch {
        Write-Log "WARN" ("Could not restart Windows Search : " + $_.Exception.Message)
    }
}

function Stop-AppProcess {
    #
    #  Kill pythonw.exe processes running from inside ProjectDir.
    #  Targets by executable path -- never kills unrelated python processes.
    #
    Write-Log "INFO" "Stopping app processes before update ..."
    $killed = @()
    try {
        Get-Process -Name "pythonw" -ErrorAction SilentlyContinue | ForEach-Object {
            $pid_ = $_.Id
            try {
                $exePath = $_.MainModule.FileName
                if ($exePath -like ($ProjectDir + "*")) {
                    Stop-Process -Id $pid_ -Force -ErrorAction Stop
                    $killed += $pid_
                    Write-Log "INFO" ("Killed PID " + $pid_ + " : " + $exePath)
                }
            } catch {
                # MainModule inaccessible on 32/64-bit mismatch -- try WMI
                try {
                    $wmi = Get-WmiObject Win32_Process -Filter ("ProcessId=" + $pid_) -ErrorAction Stop
                    if ($wmi.ExecutablePath -like ($ProjectDir + "*")) {
                        Stop-Process -Id $pid_ -Force -ErrorAction Stop
                        $killed += $pid_
                        Write-Log "INFO" ("Killed PID " + $pid_ + " (via WMI)")
                    }
                } catch {
                    Write-Log "WARN" ("Could not inspect PID " + $pid_ + " : " + $_.Exception.Message)
                }
            }
        }
    } catch {
        Write-Log "WARN" ("Stop-AppProcess error : " + $_.Exception.Message)
    }
    if ($killed.Count -eq 0) {
        Write-Log "INFO" "No app processes were running"
    }
    # Let Windows release all file handles
    Start-Sleep -Milliseconds 800
    return $killed
}

function Start-AppProcess {
    #
    #  Re-launch pythonw.exe main.py from the updated ProjectDir.
    #  setup.py handles task re-registration -- this is a safety net only.
    #
    $pythonPath = Join-Path $ProjectDir $PYTHON_EXE
    $mainPath   = Join-Path $ProjectDir "main.py"
    if (-not (Test-Path $pythonPath)) {
        Write-Log "WARN" ("Start-AppProcess : python not found at " + $pythonPath)
        return
    }
    if (-not (Test-Path $mainPath)) {
        Write-Log "WARN" "Start-AppProcess : main.py not found -- task will handle launch"
        return
    }
    try {
        $psi                  = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName         = $pythonPath
        $psi.Arguments        = '"' + $mainPath + '"'
        $psi.WorkingDirectory = $ProjectDir
        $psi.WindowStyle      = [System.Diagnostics.ProcessWindowStyle]::Hidden
        $psi.CreateNoWindow   = $true
        $psi.UseShellExecute  = $false
        [System.Diagnostics.Process]::Start($psi) | Out-Null
        Write-Log "INFO" "App process restarted"
    } catch {
        Write-Log "WARN" ("Start-AppProcess error : " + $_.Exception.Message)
    }
}

function Run-Setup {
    $pythonPath = Join-Path $ProjectDir $PYTHON_EXE
    $setupPath  = Join-Path $ProjectDir $SETUP_SCRIPT
    if (-not (Test-Path $pythonPath)) {
        Write-Log "ERROR" ("Python not found : " + $pythonPath)
        return $false
    }
    if (-not (Test-Path $setupPath)) {
        Write-Log "ERROR" ("setup.py not found : " + $setupPath)
        return $false
    }
    try {
        Write-Log "INFO" ("Running : " + $PYTHON_EXE + " " + $SETUP_SCRIPT)
        $psi                  = New-Object System.Diagnostics.ProcessStartInfo
        $psi.FileName         = $pythonPath
        $psi.Arguments        = '"' + $setupPath + '"'
        $psi.WorkingDirectory = $ProjectDir
        $psi.WindowStyle      = [System.Diagnostics.ProcessWindowStyle]::Hidden
        $psi.CreateNoWindow   = $true
        $psi.UseShellExecute  = $false
        $proc = [System.Diagnostics.Process]::Start($psi)
        $proc.WaitForExit()
        Write-Log "INFO" ("setup.py exit code : " + $proc.ExitCode)
        if ($proc.ExitCode -ne 0) {
            Write-Log "WARN" ("setup.py non-zero exit : " + $proc.ExitCode)
            return $false
        }
        return $true
    } catch {
        Write-Log "ERROR" ("Could not start Python : " + $_.Exception.Message)
        return $false
    }
}

function Remove-LeftoverFolders {
    foreach ($path in @($ProjectNew, $ProjectOld)) {
        if (Test-Path $path) {
            Write-Log "WARN" ("Leftover folder found at startup - cleaning : " + $path)
            Remove-Item $path -Recurse -Force -ErrorAction SilentlyContinue
        }
    }
}

# ================================================================
#  MAIN
# ================================================================
Write-Log "INFO" "====== UPDATER START ======"

Remove-LeftoverFolders

$remoteVer = Get-RemoteVersion
$localVer  = Get-LocalVersion

if ($null -eq $remoteVer) {
    Write-Log "WARN" "Could not fetch remote version - skipping this cycle"
    exit 0
}

if ($remoteVer -eq $localVer) {
    Write-Log "INFO" "Already up to date - nothing to do"
    exit 0
}

Write-Log "INFO" ("Update : " + $localVer + " -> " + $remoteVer)

# ================================================================
#  PHASE 1 -- Download & extract  (project\ untouched)
# ================================================================

if (Test-Path $TempDir) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue }
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

if (-not (Download-WithRetry -Url $ZipUrl -Dest $ZipPath)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 1 failed : download error - project\ intact"
    exit 1
}

if (-not (Extract-Zip -ZipFile $ZipPath -OutPath $ExtractPath)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 1 failed : extraction error - project\ intact"
    exit 1
}

$realSource = Resolve-ExtractRoot -ExtractPath $ExtractPath

# ================================================================
#  PHASE 2 -- Stage into project_new\  (project\ untouched)
# ================================================================

if (-not (Copy-ToStaging -SourcePath $realSource -Dest $ProjectNew)) {
    Remove-Item $TempDir    -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 2 failed : staging error - project\ intact"
    exit 1
}

if (-not (Test-StagingValid -StagingPath $ProjectNew)) {
    Remove-Item $TempDir    -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 2 failed : validation error - project\ intact"
    exit 1
}

Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
Write-Log "INFO" "Temp folder cleaned"

# ================================================================
#  PHASE 3 -- Quiesce, backup, sync new version in place
#
#  project\ folder itself NEVER moves or gets deleted.
#
#  Order :
#    1. Kill pythonw.exe           (releases exe/pyc handles)
#    2. Stop Windows Search        (releases .py/.pyc read locks)
#    3. robocopy project\ -> project_old\   (backup)
#    4. robocopy project_new\ -> project\   (update, /R:3 /W:2)
#    5. Restart Windows Search
#    6. Restart app process
#
#  If step 4 fails -> rollback via robocopy + restart
# ================================================================

Stop-AppProcess
$searchWasRunning = Stop-WindowsSearch

if (-not (Invoke-Backup -ActivePath $ProjectDir -BackupPath $ProjectOld)) {
    Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 3 failed : could not create backup - aborting update"
    if ($searchWasRunning) { Start-WindowsSearch }
    Start-AppProcess
    exit 1
}

if (-not (Invoke-SyncNewVersion -NewPath $ProjectNew -ActivePath $ProjectDir)) {
    Write-Log "ERROR" "Phase 3 failed : sync error - initiating rollback"
    $rollbackOK = Invoke-Rollback -ActivePath $ProjectDir -BackupPath $ProjectOld
    if ($rollbackOK) {
        Write-Log "WARN" "Rollback succeeded - previous version restored"
    } else {
        Write-Log "ERROR" "Rollback failed - application may be in broken state"
    }
    Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
    if ($searchWasRunning) { Start-WindowsSearch }
    Start-AppProcess
    exit 1
}

Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
Write-Log "INFO" "Staging folder cleaned"

if ($searchWasRunning) { Start-WindowsSearch }

# ================================================================
#  PHASE 4 -- Run setup.py  (rollback + restart if it fails)
# ================================================================

if (-not (Run-Setup)) {
    Write-Log "ERROR" "Phase 4 failed : setup.py error - initiating rollback"
    $rollbackOK = Invoke-Rollback -ActivePath $ProjectDir -BackupPath $ProjectOld
    if ($rollbackOK) {
        Write-Log "WARN" "Rollback succeeded - previous version restored"
        Start-AppProcess
    } else {
        Write-Log "ERROR" "Rollback failed - application may be in broken state"
    }
    exit 1
}

# ================================================================
#  PHASE 5 -- Commit  (only reached after 100% success)
# ================================================================

Set-Content -Path $LocalVerFile -Value $remoteVer -Encoding UTF8
Write-Log "INFO" ("Version saved : " + $remoteVer)

Remove-Item $ProjectOld -Recurse -Force -ErrorAction SilentlyContinue
Write-Log "INFO" "Backup cleaned"

Write-Log "INFO" "====== UPDATE SUCCESS ======"
exit 0