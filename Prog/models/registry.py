from data.db_handler import DBHandler

class Registry:
    def __init__(self):
        self.db = DBHandler()
    
    def add_animal(self, animal):
        self.db.add_animal(animal)
    
    def get_animal(self, name):
        return self.db.get_animal_by_name(name)
    
    def teach_command(self, name, command):
        animal = self.get_animal(name)
        if animal:
            new_commands = animal['команды'].split(', ') + [command]
            self.db.update_animal_commands(animal['id'], ', '.join(new_commands))