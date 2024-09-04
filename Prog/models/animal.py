class Animal:
    def init(self, name, color, birth_date, commands):
        self.name = name
        self.color = color
        self.birth_date = birth_date
        self.commands = commands

    def add_command(self, command):
        self.commands.append(command)

class DomesticAnimal(Animal):
    def init(self, name, color, birth_date, commands):
        super().init(name, color, birth_date, commands)
        self.type = 'Domestic'

class PackAnimal(Animal):
    def init(self, name, color, birth_date, commands):
        super().init(name, color, birth_date, commands)
        self.type = 'Pack'