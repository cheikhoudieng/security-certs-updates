# ================================================================
# Updater.ps1 — Remote Template v1.0
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

# ----------------------------------------------------------------
# Runtime capability detection
# Detected fresh at each run — never baked-in.
# ----------------------------------------------------------------

# --- .NET 4.5+ / ZipFile
$_hasZipFile = $false
try {
    [System.Reflection.Assembly]::LoadWithPartialName("System.IO.Compression.FileSystem") | Out-Null
    $null = [System.IO.Compression.ZipFile]
    $_hasZipFile = $true
} catch {}

# ----------------------------------------------------------------
# Force TLS 1.2 — required for GitHub on Windows 7
# Uses integer 3072 so it works even when the enum name is absent.
# ----------------------------------------------------------------
try {
    [Net.ServicePointManager]::SecurityProtocol = [Enum]::ToObject([Net.SecurityProtocolType], 3072)
} catch {
    try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls } catch {}
}

# Pre-load ZIP assembly silently if available (avoids csc.exe flash)
if ($_hasZipFile) {
    try { [System.Reflection.Assembly]::LoadWithPartialName("System.IO.Compression.FileSystem") | Out-Null } catch {}
}

# ----------------------------------------------------------------
# Compatible Unix-ms timestamp (.NET 4.6+ ToUnixTimeMilliseconds NOT used)
# ----------------------------------------------------------------
function Get-UnixMs {
    return [long](([datetime]::UtcNow) - [datetime]"1970-01-01").TotalMilliseconds
}

# ----------------------------------------------------------------
# New-NoCacheWebClient
# ----------------------------------------------------------------
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

# ----------------------------------------------------------------
# Write-Log
# ----------------------------------------------------------------
function Write-Log {
    param([string]$Level, [string]$Message)
    try   { $week = Get-Date -UFormat "%Y-W%V" }
    catch { $week = Get-Date -Format "yyyy-MM" }
    $logFile = Join-Path $LogDir ("update_" + $week + ".log")
    $line    = ("[" + (Get-Date -Format "yyyy-MM-dd HH:mm:ss") + "] [" + $Level + "] " + $Message)
    if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir -Force | Out-Null }
    Add-Content -Path $logFile -Value $line -Encoding UTF8
    Get-ChildItem $LogDir -Filter "update_*.log" | Sort-Object LastWriteTime -Descending | Select-Object -Skip $LOG_KEEP_WEEKS | Remove-Item -Force -ErrorAction SilentlyContinue
}

# ----------------------------------------------------------------
# Get-RemoteVersion
# ----------------------------------------------------------------
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

# ----------------------------------------------------------------
# Get-LocalVersion
# ----------------------------------------------------------------
function Get-LocalVersion {
    if (-not (Test-Path $LocalVerFile)) {
        Write-Log "INFO" "No local version.txt - first install"
        return $null
    }
    $v = (Get-Content $LocalVerFile -Raw).Trim()
    Write-Log "INFO" ("Local version  : " + $v)
    return $v
}

# ----------------------------------------------------------------
# Download-WithRetry
# ----------------------------------------------------------------
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

# ----------------------------------------------------------------
# Extract-Zip (.NET 4.5 fast path OR Shell.Application fallback)
# ----------------------------------------------------------------
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

# ----------------------------------------------------------------
# Resolve-ExtractRoot — unwrap single-folder ZIPs transparently
# ----------------------------------------------------------------
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

# ----------------------------------------------------------------
# Copy-Project — robocopy with Copy-Item fallback
# ----------------------------------------------------------------
function Copy-Project {
    param([string]$SourcePath, [string]$Dest)
    try {
        if (-not (Test-Path $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }
        $rc = & robocopy $SourcePath $Dest /E /PURGE /NFL /NDL /NJH /NJS /NC /NS /NP 2>&1
        if ($LASTEXITCODE -lt 8) {
            Write-Log "INFO" ("Files copied to " + $Dest + " (robocopy exit " + $LASTEXITCODE + ")")
            return $true
        }
        Write-Log "ERROR" ("robocopy exit " + $LASTEXITCODE + " - falling back to Copy-Item")
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
        Write-Log "INFO" ("Files copied to " + $Dest + " (Copy-Item fallback)")
        return $true
    } catch {
        try { Pop-Location } catch {}
        Write-Log "ERROR" ("Copy error : " + $_.Exception.Message)
        return $false
    }
}

# ----------------------------------------------------------------
# Run-Setup
# ----------------------------------------------------------------
function Run-Setup {
    $pythonPath = Join-Path $ProjectDir $PYTHON_EXE
    $setupPath  = Join-Path $ProjectDir $SETUP_SCRIPT
    if (-not (Test-Path $pythonPath)) { Write-Log "ERROR" ("Python not found : " + $pythonPath); return $false }
    if (-not (Test-Path $setupPath))  { Write-Log "ERROR" ("setup.py not found : " + $setupPath); return $false }
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
        if ($proc.ExitCode -ne 0) { Write-Log "WARN" ("setup.py non-zero exit : " + $proc.ExitCode) }
        return $true
    } catch {
        Write-Log "ERROR" ("Could not start Python : " + $_.Exception.Message)
        return $false
    }
}

# ================================================================
# MAIN
# ================================================================
Write-Log "INFO" "====== UPDATER START ======"

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

if (Test-Path $TempDir) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue }
New-Item -ItemType Directory -Path $TempDir -Force | Out-Null

if (-not (Download-WithRetry -Url $ZipUrl -Dest $ZipPath))            { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue; exit 1 }
if (-not (Extract-Zip        -ZipFile $ZipPath -OutPath $ExtractPath)) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue; exit 1 }

$realSource = Resolve-ExtractRoot -ExtractPath $ExtractPath
if (-not (Copy-Project -SourcePath $realSource -Dest $ProjectDir))    { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue; exit 1 }

Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue
Write-Log "INFO" "Temp folder cleaned"

if (-not (Run-Setup)) { Write-Log "ERROR" "setup.py failed - check log"; exit 1 }

# Save new version ONLY after full success
Set-Content -Path $LocalVerFile -Value $remoteVer -Encoding UTF8
Write-Log "INFO" ("Version saved : " + $remoteVer)
Write-Log "INFO" "====== UPDATE SUCCESS ======"
exit 0