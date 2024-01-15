import subprocess
import time

commands = [
    "winvnc.exe -run",
    "winvnc.exe -connect 192.168.2.163::4444"
]

folder_path = "C:/VNC"

for command in commands:
    full_command = f'cd /d {folder_path} && {command}'
    subprocess.run(full_command, shell=True)
    time.sleep(1)
