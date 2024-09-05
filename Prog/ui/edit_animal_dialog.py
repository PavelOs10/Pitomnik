from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtSql import QSqlQuery

class EditAnimalDialog(QDialog):
    def __init__(self, animal_id, parent=None):
        super().__init__(parent)
        self.animal_id = animal_id
        self.setWindowTitle('Редактировать животное')

        layout = QVBoxLayout()

        self.name_input = QLineEdit(self)
        self.type_input = QLineEdit(self)
        self.commands_input = QLineEdit(self)

        query = QSqlQuery()
        query.prepare("SELECT имя, тип, команды FROM Все_животные WHERE id = ?")
        query.addBindValue(self.animal_id)
        query.exec_()

        if query.next():
            self.name_input.setText(query.value(0))
            self.type_input.setText(query.value(1))
            self.commands_input.setText(query.value(2))

        layout.addWidget(self.name_input)
        layout.addWidget(self.type_input)
        layout.addWidget(self.commands_input)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.save_changes)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_changes(self):
        name = self.name_input.text()
        animal_type = self.type_input.text()
        commands = self.commands_input.text()

        query = QSqlQuery()
        query.prepare("UPDATE Все_животные SET имя = ?, тип = ?, команды = ? WHERE id = ?")
        query.addBindValue(name)
        query.addBindValue(animal_type)
        query.addBindValue(commands)
        query.addBindValue(self.animal_id)

        if query.exec_():
            self.accept()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить изменения.")