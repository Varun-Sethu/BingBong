import win32api, win32con, win32gui
import c_long
import os
import psutil
from enum import Enum


def __start_stop(self, application):
    keyboard_on = False
    pID = 0
    for process in psutil.process_iter():
        if process.name == application:
            keyboard_on = True
            pID = process.pid
    if not keyboard_on:
        win32api.ShellExecute(None, "open", application, None, None, 6)
    else:
        os.system(f"taskkill /pid {pID}")

# function to toggle the onscreen keyboard
def toggle_OSK(self):
    __start_stop("osk.exe")
def toggle_explorer(self):
    __start_stop("explorer.exe")