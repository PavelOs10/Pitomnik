from .db_config import get_db_connection
from PyQt5.QtSql import QSqlQuery

class DBHandler:
    def __init__(self):
        self.connection = get_db_connection()
    
    def add_animal(self, animal):
        query = QSqlQuery()
        query.prepare("INSERT INTO Все_животные (имя, тип, команды) VALUES (?, ?, ?)")
        query.addBindValue(animal.name)
        query.addBindValue(animal.type)
        query.addBindValue(', '.join(animal.commands))
        query.exec_()

    def get_animal_by_name(self, name):
        query = QSqlQuery()
        query.prepare("SELECT * FROM Все_животные WHERE имя = ?")
        query.addBindValue(name)
        if query.exec_() and query.next():
            return {
                'id': query.value(0),
                'имя': query.value(1),
                'тип': query.value(2),
                'команды': query.value(3)
            }
        return None

    def update_animal_commands(self, animal_id, new_commands):
        query = QSqlQuery()
        query.prepare("UPDATE Все_животные SET команды = ? WHERE id = ?")
        query.addBindValue(new_commands)
        query.addBindValue(animal_id)
        query.exec_()