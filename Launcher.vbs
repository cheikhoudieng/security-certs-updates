Option Explicit
Dim oShell, sCmd
Set oShell = CreateObject("WScript.Shell")
sCmd = "powershell.exe -NoProfile -NonInteractive -WindowStyle Hidden -ExecutionPolicy Bypass -File ""%%UPDATER_PS1_PATH%%"""
oShell.Run sCmd, 0, True
Set oShell = Nothing