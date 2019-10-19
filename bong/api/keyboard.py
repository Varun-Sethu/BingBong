import win32api, win32con, win32gui
import c_long
import os
import psutil
from enum import Enum


def press(self, key):
        keys = {"ctrl": 0x11, "tab": 0x09, "enter": 0x0D, "caps_lock": 0x14, "windows": 0x5B}
        win32api.keybd_event(keys[key], 0, 0, 0)
        time.sleep(.05)
        win32api.keybd_event(keys[key], 0, win32con.KEYEVENTF_KEYUP, 0)