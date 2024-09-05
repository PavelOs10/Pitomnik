from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtSql import QSqlQuery

class AddAnimalDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Animal')
        layout = QVBoxLayout()
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Имя')
        layout.addWidget(self.name_input)
        self.type_input = QLineEdit(self)
        self.type_input.setPlaceholderText('Тип(Домашнее/Вьючное)')
        layout.addWidget(self.type_input)
        self.commands_input = QLineEdit(self)
        self.commands_input.setPlaceholderText('Команды')
        layout.addWidget(self.commands_input)
        self.add_button = QPushButton('Добавить')
        self.add_button.clicked.connect(self.add_animal)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

    def add_animal(self):
        name = self.name_input.text()
        animal_type = self.type_input.text()
        commands = self.commands_input.text()
        
        if not name or not animal_type:
            QMessageBox.warning(self, "Ошибка", "Имя и тип животного обязательны для заполнения.")
            return
        
        query = QSqlQuery()
        query.prepare("INSERT INTO Все_животные (имя, тип, команды) VALUES (?, ?, ?)")
        query.addBindValue(name)
        query.addBindValue(animal_type)
        query.addBindValue(commands)
        
        if query.exec_():
            QMessageBox.information(self, "Успех", "Животное успешно добавлено.")
            self.accept()
        else:
            QMessageBox.critical(self, "Ошибка", f"Не удалось добавить животное: {query.lastError().text()}")