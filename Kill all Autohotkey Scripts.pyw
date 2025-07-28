import sys
import time
import psutil
import keyboard
from pystray import Icon, Menu, MenuItem
from PIL import Image

# The script sets Ctrl + Alt + Escape to kill every autohotkey script that is currently running

# ---------- Functions

def kill_autohotkey_scripts():
    
    # List of possible AutoHotkey process names
    ahk_process_names = ['AutoHotkey.exe', 'AutoHotkey64.exe', 'AutoHotkey32_UIA.exe', 'AutoHotkey64_UIA.exe']
    
    for process in psutil.process_iter(['name']):
        try:
            if process.info['name'] in ahk_process_names:
                print(f"Killing process {process.pid} ({process.info['name']})")
                process.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    time.sleep(0.1) # Prevents triggering multiple times    


# ---------- Code

if __name__ == "__main__":

     keyboard.add_hotkey('ctrl+alt+esc', kill_autohotkey_scripts) # Sets hotkey to Ctrl + Alt + Escape

     icon_image = Image.open('./kill ahk.ico')

     menu = Menu(MenuItem('Exit', lambda icon, item: (icon.stop(), sys.exit(0))))
     icon = Icon("ico", icon_image, "Kill AHK Scripts Keybind", menu=menu)
     icon.run()
    
