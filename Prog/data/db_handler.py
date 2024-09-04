from .db_config import get_db_connection

class DBHandler:
    def init(self):
        self.connection = get_db_connection()

    def add_animal(self, animal):
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO Все_животные (имя, масть, дата_рождения, команды, тип, старое_таблице) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (animal.name, animal.color, animal.birth_date, animal.commands, animal.type, animal.old_table))
            self.connection.commit()

    def get_animal_by_name(self, name):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM Все_животные WHERE имя = %s"
            cursor.execute(sql, (name,))
            return cursor.fetchone()

    def update_animal_commands(self, animal_id, new_commands):
        with self.connection.cursor() as cursor:
            sql = "UPDATE Все_животные SET команды = %s WHERE id = %s"
            cursor.execute(sql, (new_commands, animal_id))
            self.connection.commit()