from configparser import SafeConfigParser
import commands


class configuration:
    def __init__(self):
        self.functions = {}
        self.registered_notes = ["c", "c-sharp", "d", "d-sharp", "e", "f", "f-sharp", "g", "g-sharp", "a", "a-sharp", "b"]

    def __reset(self):
        self.functions = {}


    def parse(self, configuration_path):
        parser = SafeConfigParser()
        # read the given config file and if it doesnt exist fallback onto the default one
        configs = parser.read([configuration_path, 'sample.ini'])


        # Wrap in a massive exception block :P
        try:
            for section in configs.sections():
                category = {"movement-controls": commands.Movement, "system-controls": commands.System, "keyboard-controls": commands.Keyboard}[section]
                
                for (key, val) in configs.items(section):
                    enum_val = category(key)
                    # check that the note exists and does not currently have an action assigned to it
                    if key not in self.registered_notes or key in self.functions:
                        raise Exception()
                    self.functions.update({key, enum_val})
                    
        except:
            return "Invalid config file"

