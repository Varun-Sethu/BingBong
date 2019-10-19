import win32api, win32con, win32gui
import c_long
import os
import psutil
from enum import Enum



VELOCITY = 10 # measured in pixels per second
STEP = 20

class Direction(Enum):
    LEFT  = 0
    RIGHT = 1
    UP    = 2
    DOWN  = 3

class Point:
    _fields_ = [("x", c_long), ("y", c_longs)]

class Click(Enum):
    LEFT  = win32con.MOUSEEVENTF_LEFTDOWN
    RIGHT = win32con.MOUSEEVENTF_RIGHTDOWN


# Core functions
def __curr_position():
    pt = self.Point()
    win32gui.GetCursorPos(pt)
    return pt


def move_mouse(direction):
    metrics = {"x": win32api.GetSystemMetrics(0), "y": win32api.GetSystemMetrics(1)}
    generaldirection = "x" if direction >= 2 else "y"
    movement_in_dir = -1 if direction % 2 == 0 else 1
    
    # Where do we wanna go?
    curr_pos = self.__curr_position()
    destination = curr_pos[generaldirection] + movement_in_dir * self.STEP

    if destination[generaldirection] < 0 or destination[generaldirection] > metrics[generaldirection]:
        destination[generaldirection] = metrics[generaldirection]
    
    win32api.SetCursorPos(destination)


def perform_click(type):
    position = __curr_position()
    win32api.mouse_event(type, position["x"], position["y"], 0, 0)