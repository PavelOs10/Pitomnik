from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QMessageBox, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel
from .add_animal_dialog import AddAnimalDialog
from .edit_animal_dialog import EditAnimalDialog
from data.db_config import get_db_connection, create_tables

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Регистрация животных')

        self.db = self.connect_to_db()

        layout = QVBoxLayout()

        self.add_animal_button = QPushButton('Завести новое животное')
        self.add_animal_button.clicked.connect(self.open_add_animal_dialog)
        layout.addWidget(self.add_animal_button)

        self.edit_animal_button = QPushButton('Редактировать выбранное животное')
        self.edit_animal_button.clicked.connect(self.edit_selected_animal)
        layout.addWidget(self.edit_animal_button)

        self.delete_animal_button = QPushButton('Удалить выбранное животное')
        self.delete_animal_button.clicked.connect(self.delete_selected_animal)
        layout.addWidget(self.delete_animal_button)

        self.table_view = QTableView()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable("Все_животные")
        self.model.select()
        self.table_view.setModel(self.model)
        layout.addWidget(self.table_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def connect_to_db(self):
        db = get_db_connection()
        if db.isOpen():
            create_tables()
        return db

    def open_add_animal_dialog(self):
        if self.db.isOpen():
            dialog = AddAnimalDialog(self)
            if dialog.exec_() == QDialog.Accepted:
                self.model.select()
        else:
            QMessageBox.critical(self, "Ошибка", "Нет подключения к базе данных.")

    def edit_selected_animal(self):
        selected_index = self.table_view.currentIndex()
        if selected_index.isValid():
            animal_id = self.model.data(self.model.index(selected_index.row(), 0))
            dialog = EditAnimalDialog(animal_id, self)
            if dialog.exec_() == QDialog.Accepted:
                self.model.select()
        else:
            QMessageBox.warning(self, "Выбор записи", "Пожалуйста, выберите запись для редактирования.")

    def delete_selected_animal(self):
        selected_index = self.table_view.currentIndex()
        if selected_index.isValid():
            confirm = QMessageBox.question(self, "Удалить запись", "Вы уверены, что хотите удалить эту запись?")
            if confirm == QMessageBox.Yes:
                self.model.removeRow(selected_index.row())
                self.model.submitAll()
                self.model.select()
        else:
            QMessageBox.warning(self, "Выбор записи", "Пожалуйста, выберите запись для удаления.")