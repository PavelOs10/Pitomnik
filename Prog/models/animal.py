class Animal:
    def __init__(self, name, color, birth_date, commands):
        self.name = name
        self.color = color
        self.birth_date = birth_date
        self.commands = commands
    
    def add_command(self, command):
        self.commands.append(command)

class DomesticAnimal(Animal):
    def __init__(self, name, color, birth_date, commands):
        super().__init__(name, color, birth_date, commands)
        self.type = 'Domestic'

class PackAnimal(Animal):
    def __init__(self, name, color, birth_date, commands):
        super().__init__(name, color, birth_date, commands)
        self.type = 'Pack'