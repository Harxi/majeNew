class Commands:
    def __init__(self, *args):
        self.showCommands = {}
        self.commands = {}
        for command in args:
            self.showCommands[command.name] = command
            for name in command.name.split('|'):
                self.commands[name] = command

class Command:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.function = None
        
    def __str__(self):
        return f"{', '.join(self.name.split('|'))} - {self.description}"
        
    def command(self, function):
        self.function = function
        
