from enum import Enum


class Movement(Enum):
    UP          = 'up'
    DOWN        = 'down'
    LEFT        = 'left'
    RIGHT       = 'right'
    LEFT_CLCIK  = 'left-click'
    RIGHT_CLICK = 'right-click'

class Keyboard(Enum):
    WINDOWS = 'windows'
    CTRL    = 'ctrl'
    ENTER   = 'enter'
    CAPS    = 'caps_lock'
    TAB     = 'tab'


class System(Enum):
    EXPLORER = 'explorer'
    KEYBOARD = 'osk'
