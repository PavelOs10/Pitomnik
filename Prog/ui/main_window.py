from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from .add_animal_dialog import AddAnimalDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Animal Registry')
        layout = QVBoxLayout()
        self.add_animal_button = QPushButton('Завести новое животное')
        self.add_animal_button.clicked.connect(self.open_add_animal_dialog)
        layout.addWidget(self.add_animal_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_add_animal_dialog(self):
        dialog = AddAnimalDialog(self)
        dialog.exec_()