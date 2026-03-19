# ================================================================
# Updater.ps1 -- Remote Template v2.0  (Atomic Swap Edition)
# Placeholders injected by setup.py at each update cycle.
# DO NOT fill path variables manually.
# ================================================================

# ---- Baked-in variables (injected by setup.py)
$LOG_KEEP_WEEKS  = %%LOG_KEEP_WEEKS%%
$ProjectDir      = "%%PROJECT_DIR%%"
$LogDir          = "%%LOG_DIR%%"
$ZipUrl          = "%%ZIP_URL%%"
$VerBaseUrl      = "%%VER_URL%%"
$LocalVerFile    = "%%LOCAL_VER_FILE%%"
$PYTHON_EXE      = "%%PYTHON_EXE%%"
$SETUP_SCRIPT    = "%%SETUP_SCRIPT%%"
$TempDir         = Join-Path $env:TEMP "GH_Update_%%REPO_NAME%%"
$ZipPath         = Join-Path $TempDir "download.zip"
$ExtractPath     = Join-Path $TempDir "extracted"

# ---- Swap paths (computed from ProjectDir)
$ProjectNew      = $ProjectDir + "_new"
$ProjectOld      = $ProjectDir + "_old"

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
    param([string]$SourcePath, [string]$Dest)
    try {
        if (Test-Path $Dest) { Remove-Item $Dest -Recurse -Force }
        New-Item -ItemType Directory -Path $Dest -Force | Out-Null

        $null = & robocopy $SourcePath $Dest /E /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1
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

function Invoke-AtomicSwap {
    param([string]$OldPath, [string]$NewPath, [string]$BackupPath)
    try {
        if (Test-Path $BackupPath) {
            Remove-Item $BackupPath -Recurse -Force -ErrorAction Stop
            Write-Log "INFO" "Removed leftover backup"
        }

        # Step 1/2 : project\ -> project_old\  (~1ms kernel op)
        Rename-Item -Path $OldPath -NewName (Split-Path $BackupPath -Leaf) -ErrorAction Stop
        Write-Log "INFO" "Swap step 1/2 : project -> project_old OK"

        # Step 2/2 : project_new\ -> project\  (~1ms kernel op)
        Rename-Item -Path $NewPath -NewName (Split-Path $OldPath -Leaf) -ErrorAction Stop
        Write-Log "INFO" "Swap step 2/2 : project_new -> project OK"

        return $true
    } catch {
        Write-Log "ERROR" ("Atomic swap error : " + $_.Exception.Message)
        return $false
    }
}

function Invoke-Rollback {
    param([string]$ActivePath, [string]$BackupPath)
    Write-Log "WARN" "====== ROLLBACK INITIATED ======"
    try {
        if (Test-Path $ActivePath) {
            Remove-Item $ActivePath -Recurse -Force -ErrorAction Stop
            Write-Log "INFO" "Broken active folder removed"
        }
        Rename-Item -Path $BackupPath -NewName (Split-Path $ActivePath -Leaf) -ErrorAction Stop
        Write-Log "INFO" "Rollback OK - previous version restored"
        return $true
    } catch {
        Write-Log "ERROR" ("Rollback FAILED : " + $_.Exception.Message)
        Write-Log "ERROR" "Manual action required :"
        Write-Log "ERROR" ("  Rename '" + $BackupPath + "' -> '" + $ActivePath + "'")
        return $false
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
        $psi.Arguments        = """" + $setupPath + """"
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
#  PHASE 1 -- Download & extract  (ProjectDir untouched)
# ================================================================

if (Test-Path $TempDir) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue }
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

if (-not (Download-WithRetry -Url $ZipUrl -Dest $ZipPath)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 1 failed : download error - ProjectDir intact"
    exit 1
}

if (-not (Extract-Zip -ZipFile $ZipPath -OutPath $ExtractPath)) {
    Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 1 failed : extraction error - ProjectDir intact"
    exit 1
}

$realSource = Resolve-ExtractRoot -ExtractPath $ExtractPath

# ================================================================
#  PHASE 2 -- Stage into ProjectNew  (ProjectDir untouched)
# ================================================================

if (-not (Copy-ToStaging -SourcePath $realSource -Dest $ProjectNew)) {
    Remove-Item $TempDir    -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 2 failed : staging error - ProjectDir intact"
    exit 1
}

if (-not (Test-StagingValid -StagingPath $ProjectNew)) {
    Remove-Item $TempDir    -Recurse -Force -ErrorAction SilentlyContinue
    Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
    Write-Log "ERROR" "Phase 2 failed : validation error - ProjectDir intact"
    exit 1
}

Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
Write-Log "INFO" "Temp folder cleaned"

# ================================================================
#  PHASE 3 -- Atomic swap
#    project\     -> project_old\   (backup,  ~1ms)
#    project_new\ -> project\       (activate, ~1ms)
# ================================================================

if (-not (Invoke-AtomicSwap -OldPath $ProjectDir -NewPath $ProjectNew -BackupPath $ProjectOld)) {
    Write-Log "ERROR" "Phase 3 failed : atomic swap error"

    if (Test-Path $ProjectDir) {
        Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
        Write-Log "INFO" "ProjectDir intact - staging cleaned"
    } else {
        Write-Log "ERROR" "ProjectDir missing after partial swap - emergency restore"
        if (Test-Path $ProjectOld) {
            Rename-Item -Path $ProjectOld -NewName (Split-Path $ProjectDir -Leaf) -ErrorAction SilentlyContinue
            if (Test-Path $ProjectDir) {
                Write-Log "INFO" "Emergency restore OK - previous version is active"
            } else {
                Write-Log "ERROR" "Emergency restore FAILED - manual action required"
                Write-Log "ERROR" ("  Rename '" + $ProjectOld + "' -> '" + $ProjectDir + "'")
            }
        }
        Remove-Item $ProjectNew -Recurse -Force -ErrorAction SilentlyContinue
    }
    exit 1
}

# ================================================================
#  PHASE 4 -- Run setup.py  (rollback if it fails)
# ================================================================

if (-not (Run-Setup)) {
    Write-Log "ERROR" "Phase 4 failed : setup.py error - initiating rollback"
    $rollbackOK = Invoke-Rollback -ActivePath $ProjectDir -BackupPath $ProjectOld
    if ($rollbackOK) {
        Write-Log "WARN" "Rollback succeeded - previous version is running"
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