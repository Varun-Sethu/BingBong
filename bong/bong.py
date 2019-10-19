from config import configuration, commands
from api import mouse, keyboard, system
import ..observer as observer



class Bong(observer.Observer):
    def __init__(self):
        current_configuration = configuration()
        current_configuration.parse("config.ini")

    # Observer methods
    def update(self, message):
        pass




    # this function really isnt that nice :&
    def __handle_command(self, command):
        if type(command).__class__ == commands.Movement:
            if command == Movement.LEFT_CLCIK or command == Movement.RIGHT_CLICK:
                direction = command.value.split('-')[0]
                click_side = mouse.Click[direction]

                mouse.perform_click(click_side)
            else:
                # TODO: improve this so that it isnt doesnt have to convert our command code into the command code for the mouse, this reduces redundancy
                mouse_movement = mouse.Direction[command.value]
                mouse.move_mouse(mouse_movement)
        elif type(command).__class__ == commands.Keyboard:
            keyboard.press(command.value)
        elif type(command).__class__ == commands.System:
            system.__start_stop(command.value)