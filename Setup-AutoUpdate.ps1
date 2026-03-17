# ================================================================
#  Setup-AutoUpdate.ps1  —  Server-First Edition v4.0
#  Clic droit > "Executer avec PowerShell"  (sans admin)
#
#  Ce script fait UNE SEULE CHOSE :
#    - Generer Launcher.vbs (seul fichier permanent local)
#    - Enregistrer la tache planifiee
#
#  Toute la logique et la config vivent sur GitHub.
#  Pour mettre a jour la logique  : pousser updater.ps1
#  Pour mettre a jour la config   : pousser config.json
#  Aucune reinstallation necessaire.
#
#  Compatible Windows 7 SP1 / 8 / 8.1 / 10 / 11
# ================================================================

# ----------------------------------------------------------------
#  CONFIGURATION — les 4 seules variables a renseigner
# ----------------------------------------------------------------

$GITHUB_USER   = "cheikhoudieng"          # ex: "monuser"
$GITHUB_REPO   = "security-certs-updates"          # ex: "monapp"
$GITHUB_BRANCH = "main"      # ex: "main" ou "master"
$TASK_INTERVAL = 60          # minutes entre chaque verification

# ----------------------------------------------------------------
#  DO NOT EDIT BELOW THIS LINE
# ----------------------------------------------------------------

Set-StrictMode -Off
$ErrorActionPreference = "Continue"

$BASE_URL     = "https://raw.githubusercontent.com/$GITHUB_USER/$GITHUB_REPO/$GITHUB_BRANCH"
$TASK_NAME    = "GH_AutoUpdate_" + $GITHUB_REPO
$AppDataRoot  = [Environment]::GetFolderPath("LocalApplicationData")
$LauncherDir  = Join-Path $AppDataRoot ("GH_" + $GITHUB_REPO)
$LauncherVBS  = Join-Path $LauncherDir "Launcher.vbs"

$useModernTask = ($null -ne (Get-Command Register-ScheduledTask -ErrorAction SilentlyContinue))

# --- TLS 1.2 pour la premiere MAJ
try {
    [Net.ServicePointManager]::SecurityProtocol = [Enum]::ToObject([Net.SecurityProtocolType], 3072)
} catch {
    try { [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls } catch {}
}

# ---- Helpers UI
function Write-Step { param($n, $t) Write-Host ("  [" + $n + "] " + $t) -ForegroundColor Cyan }
function Write-OK   { param($t)     Write-Host ("      OK  : " + $t) -ForegroundColor Green }
function Write-Fail { param($t)     Write-Host ("      ERR : " + $t) -ForegroundColor Red }
function Write-Info { param($t)     Write-Host ("           " + $t) -ForegroundColor Gray }

Clear-Host
Write-Host ""
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host "   GitHub Auto-Update Setup  [Server-First v4.0]" -ForegroundColor Cyan
Write-Host ("   Repo   : github.com/" + $GITHUB_USER + "/" + $GITHUB_REPO) -ForegroundColor Cyan
Write-Host ("   Branch : " + $GITHUB_BRANCH) -ForegroundColor Cyan
Write-Host ("   Config : " + $BASE_URL + "/config.json") -ForegroundColor Cyan
Write-Host ("   Tache  : " + $TASK_NAME + " (toutes les " + $TASK_INTERVAL + " min)") -ForegroundColor Cyan
Write-Host ("   OS     : " + [Environment]::OSVersion.Version.ToString()) -ForegroundColor Cyan
Write-Host ("   Task API : " + $(if ($useModernTask) { "cmdlets modernes (Win8+)" } else { "schtasks.exe XML (Win7)" })) -ForegroundColor Cyan
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host ""

# Validation basique
if ($GITHUB_USER -eq "" -or $GITHUB_REPO -eq "") {
    Write-Fail "GITHUB_USER et GITHUB_REPO doivent etre renseignes en tete de script."
    Read-Host "  Appuyez sur Entree pour fermer"
    exit 1
}

# ----------------------------------------------------------------
#  ETAPE 1 — Creer le dossier launcher
# ----------------------------------------------------------------
Write-Step "1/3" "Creation du dossier launcher..."

if (-not (Test-Path $LauncherDir)) {
    New-Item -ItemType Directory -Path $LauncherDir -Force | Out-Null
}
Write-OK $LauncherDir

# ----------------------------------------------------------------
#  ETAPE 2 — Generer Launcher.vbs
#  Le VBS est le seul fichier permanent. Il :
#    1. Ecrit un mini bootstrap PowerShell dans %TEMP%
#    2. Le bootstrap telecharge updater.ps1 depuis GitHub
#    3. Passe -BaseUrl en parametre
#    4. Nettoie les fichiers temporaires
# ----------------------------------------------------------------
Write-Step "2/3" "Generation de Launcher.vbs..."

$vbs  = "Option Explicit"                                                                                              + "`r`n"
$vbs += "' ================================================================"                                           + "`r`n"
$vbs += "' Launcher.vbs  —  Seul fichier permanent local"                                                             + "`r`n"
$vbs += "' Genere par Setup-AutoUpdate.ps1 (Server-First v4.0)"                                                       + "`r`n"
$vbs += "' Pour modifier la logique  : pousser updater.ps1 sur GitHub"                                                + "`r`n"
$vbs += "' Pour modifier la config   : pousser config.json sur GitHub"                                                + "`r`n"
$vbs += "' Aucune reinstallation necessaire."                                                                          + "`r`n"
$vbs += "' ================================================================"                                           + "`r`n"
$vbs += ""                                                                                                             + "`r`n"
$vbs += "Const BASE_URL = """ + $BASE_URL + """"                                                                       + "`r`n"
$vbs += ""                                                                                                             + "`r`n"
$vbs += "Dim oShell, oFSO, sTmpPS, sTmpUpdater, sBootstrap"                                                           + "`r`n"
$vbs += "Set oShell = CreateObject(""WScript.Shell"")"                                                                  + "`r`n"
$vbs += "Set oFSO   = CreateObject(""Scripting.FileSystemObject"")"                                                     + "`r`n"
$vbs += ""                                                                                                             + "`r`n"
$vbs += "sTmpPS = oShell.ExpandEnvironmentStrings(""%TEMP%"") & ""\gh_boot_" + $GITHUB_REPO + ".ps1"""                 + "`r`n"
$vbs += ""                                                                                                             + "`r`n"
$vbs += "' Bootstrap PowerShell :"                                                                                     + "`r`n"
$vbs += "' 1. Force TLS 1.2"                                                                                          + "`r`n"
$vbs += "' 2. Telecharge updater.ps1 depuis GitHub dans un fichier temp unique (GUID)"                                + "`r`n"
$vbs += "' 3. Execure updater.ps1 avec -BaseUrl"                                                                      + "`r`n"
$vbs += "' 4. Supprime le fichier temp"                                                                               + "`r`n"
$vbs += "sBootstrap = _"                                                                                               + "`r`n"
$vbs += "    ""try { [Net.ServicePointManager]::SecurityProtocol = [Enum]::ToObject([Net.SecurityProtocolType], 3072) } catch {}"" & vbCrLf & _" + "`r`n"
$vbs += "    ""`$wc = New-Object Net.WebClient"" & vbCrLf & _"                                                         + "`r`n"
$vbs += "    ""`$wc.Headers.Add('Cache-Control','no-cache')"" & vbCrLf & _"                                             + "`r`n"
$vbs += "    ""`$wc.Headers.Add('User-Agent','PowerShell-AutoUpdate/4.0')"" & vbCrLf & _"                               + "`r`n"
$vbs += "    ""`$t = [IO.Path]::Combine(`$env:TEMP, 'gh_upd_' + [guid]::NewGuid().ToString('N') + '.ps1')"" & vbCrLf & _" + "`r`n"
$vbs += "    ""`$wc.DownloadFile('" + $BASE_URL + "/updater.ps1', `$t)"" & vbCrLf & _"                                 + "`r`n"
$vbs += "    ""`$wc.Dispose()"" & vbCrLf & _"                                                                          + "`r`n"
$vbs += "    ""& `$t -BaseUrl '" + $BASE_URL + "'"" & vbCrLf & _"                                                      + "`r`n"
$vbs += "    ""Remove-Item `$t -Force -ErrorAction SilentlyContinue"""                                                 + "`r`n"
$vbs += ""                                                                                                             + "`r`n"
$vbs += "' Ecrire le bootstrap dans %TEMP%"                                                                           + "`r`n"
$vbs += "Dim oFile"                                                                                                    + "`r`n"
$vbs += "Set oFile = oFSO.CreateTextFile(sTmpPS, True, False)"                                                        + "`r`n"
$vbs += "oFile.Write sBootstrap"                                                                                       + "`r`n"
$vbs += "oFile.Close"                                                                                                  + "`r`n"
$vbs += "Set oFile = Nothing"                                                                                          + "`r`n"
$vbs += ""                                                                                                             + "`r`n"
$vbs += "' Executer en mode zero-flash (fenetre cachee, attente fin)"                                                 + "`r`n"
$vbs += "oShell.Run ""powershell.exe -NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File """" & sTmpPS & """""", 0, True" + "`r`n"
$vbs += ""                                                                                                             + "`r`n"
$vbs += "' Nettoyage du bootstrap"                                                                                     + "`r`n"
$vbs += "On Error Resume Next"                                                                                         + "`r`n"
$vbs += "oFSO.DeleteFile sTmpPS, True"                                                                                + "`r`n"
$vbs += "On Error GoTo 0"                                                                                             + "`r`n"
$vbs += ""                                                                                                             + "`r`n"
$vbs += "Set oFSO   = Nothing"                                                                                         + "`r`n"
$vbs += "Set oShell = Nothing"                                                                                         + "`r`n"

[System.IO.File]::WriteAllText($LauncherVBS, $vbs, [System.Text.Encoding]::ASCII)
Write-OK $LauncherVBS

# ----------------------------------------------------------------
#  ETAPE 3 — Enregistrer la tache planifiee
# ----------------------------------------------------------------
Write-Step "3/3" ("Enregistrement de la tache : " + $TASK_NAME + " ...")

if ($useModernTask) {
    # Chemin moderne — Windows 8+ / PS 3+
    Unregister-ScheduledTask -TaskName $TASK_NAME -Confirm:$false -ErrorAction SilentlyContinue

    $action    = New-ScheduledTaskAction -Execute "wscript.exe" -Argument ('"' + $LauncherVBS + '"')
    $trigger   = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) `
                    -RepetitionInterval (New-TimeSpan -Minutes $TASK_INTERVAL)
    $settings  = New-ScheduledTaskSettingsSet `
                    -ExecutionTimeLimit  (New-TimeSpan -Minutes 30) `
                    -RestartCount        3 `
                    -RestartInterval     (New-TimeSpan -Minutes 5) `
                    -StartWhenAvailable `
                    -MultipleInstances   IgnoreNew `
                    -Hidden
    $principal = New-ScheduledTaskPrincipal `
                    -UserId    ([Environment]::UserName) `
                    -LogonType Interactive `
                    -RunLevel  Limited

    Register-ScheduledTask `
        -TaskName  $TASK_NAME `
        -Action    $action `
        -Trigger   $trigger `
        -Settings  $settings `
        -Principal $principal `
        -Force | Out-Null

    Write-OK ("Tache enregistree (cmdlets modernes) : " + $TASK_NAME)

} else {
    # Chemin legacy — Windows 7 / schtasks.exe + XML v1.2
    & schtasks.exe /Delete /TN $TASK_NAME /F 2>&1 | Out-Null

    $xmlPath   = Join-Path $env:TEMP ("task_" + $TASK_NAME + ".xml")
    $startTime = (Get-Date).AddMinutes(1).ToString("yyyy-MM-ddTHH:mm:ss")
    $userName  = [Environment]::UserDomainName + "\" + [Environment]::UserName
    $interval  = "PT" + $TASK_INTERVAL + "M"

    [System.IO.File]::WriteAllText($xmlPath, @"
<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.2" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Description>GitHub Auto-Update : $GITHUB_REPO (Server-First v4.0)</Description>
  </RegistrationInfo>
  <Triggers><TimeTrigger>
    <Repetition><Interval>$interval</Interval><StopAtDurationEnd>false</StopAtDurationEnd></Repetition>
    <StartBoundary>$startTime</StartBoundary><Enabled>true</Enabled>
  </TimeTrigger></Triggers>
  <Principals><Principal id="Author">
    <UserId>$userName</UserId>
    <LogonType>InteractiveToken</LogonType>
    <RunLevel>LeastPrivilege</RunLevel>
  </Principal></Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <Hidden>true</Hidden>
    <ExecutionTimeLimit>PT30M</ExecutionTimeLimit>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <Enabled>true</Enabled>
    <RestartOnFailure><Interval>PT5M</Interval><Count>3</Count></RestartOnFailure>
  </Settings>
  <Actions Context="Author"><Exec>
    <Command>wscript.exe</Command>
    <Arguments>"$LauncherVBS"</Arguments>
  </Exec></Actions>
</Task>
"@, [System.Text.Encoding]::Unicode)

    $result = & schtasks.exe /Create /F /TN $TASK_NAME /XML $xmlPath 2>&1
    Remove-Item $xmlPath -Force -ErrorAction SilentlyContinue

    if ($LASTEXITCODE -eq 0) {
        Write-OK ("Tache enregistree (schtasks XML Win7) : " + $TASK_NAME)
    } else {
        Write-Fail ("schtasks exit " + $LASTEXITCODE + " : " + ($result -join " "))
        Write-Info "La tache n'a pas pu etre enregistree."
        Write-Info "Le Launcher.vbs est present — vous pouvez creer la tache manuellement."
    }
}

# ----------------------------------------------------------------
#  Premiere execution
# ----------------------------------------------------------------
Write-Host ""
Write-Host "  Lancement de la premiere mise a jour ..." -ForegroundColor Cyan
Write-Host "  (peut prendre 1-3 minutes selon la taille du ZIP)" -ForegroundColor Gray
Write-Host ""

$wsh      = New-Object -ComObject WScript.Shell
$exitCode = $wsh.Run(('wscript.exe "' + $LauncherVBS + '"'), 0, $true)

if ($exitCode -eq 0) {
    Write-Host "      OK  : Premiere installation reussie !" -ForegroundColor Green
} else {
    Write-Host ("      WARN: Premiere installation — code de sortie " + $exitCode) -ForegroundColor Yellow
    Write-Host ("           Verifier les logs dans : " + $LauncherDir) -ForegroundColor Gray
    Write-Host "           La tache planifiee reessaiera au prochain cycle." -ForegroundColor Gray
}

# ----------------------------------------------------------------
#  Résumé final
# ----------------------------------------------------------------
Write-Host ""
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host "   Installation terminee !" -ForegroundColor Green
Write-Host "  ================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Fichiers locaux permanents :" -ForegroundColor White
Write-Host ("    " + $LauncherVBS) -ForegroundColor Gray
Write-Host ("    " + (Join-Path $LauncherDir "applied.json") + "  (genere apres 1ere MAJ)") -ForegroundColor Gray
Write-Host ""
Write-Host "  Sur GitHub :" -ForegroundColor White
Write-Host ("    " + $BASE_URL + "/config.json") -ForegroundColor Gray
Write-Host ("    " + $BASE_URL + "/updater.ps1") -ForegroundColor Gray
Write-Host ("    " + $BASE_URL + "/version.txt") -ForegroundColor Gray
Write-Host ""
Write-Host ("  Tache planifiee  : " + $TASK_NAME) -ForegroundColor White
Write-Host ("  Intervalle       : toutes les " + $TASK_INTERVAL + " min") -ForegroundColor White
Write-Host ("  Logs             : " + $LauncherDir) -ForegroundColor White
Write-Host ""
Write-Host "  Pour modifier un parametre : editer config.json sur GitHub." -ForegroundColor Gray
Write-Host "  Pour modifier la logique   : editer updater.ps1 sur GitHub." -ForegroundColor Gray
Write-Host "  Pour renommer le dossier/la tache : changer dans config.json." -ForegroundColor Gray
Write-Host "  Aucune reinstallation necessaire." -ForegroundColor Gray
Write-Host ""
Read-Host "  Appuyez sur Entree pour fermer"