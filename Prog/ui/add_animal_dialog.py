from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton
from models.registry import Registry
from models.animal import DomesticAnimal, PackAnimal

class AddAnimalDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Add Animal')
        layout = QVBoxLayout()
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText('Name')
        layout.addWidget(self.name_input)
        self.type_input = QLineEdit(self)
        self.type_input.setPlaceholderText('Type (Domestic/Pack)')
        layout.addWidget(self.type_input)
        self.commands_input = QLineEdit(self)
        self.commands_input.setPlaceholderText('Commands (comma-separated)')
        layout.addWidget(self.commands_input)
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.add_animal)
        layout.addWidget(self.add_button)
        self.setLayout(layout)

    def add_animal(self):
        name = self.name_input.text()
        animal_type = self.type_input.text()
        commands = self.commands_input.text().split(', ')
        if animal_type.lower() == 'domestic':
            animal = DomesticAnimal(name, None, None, commands)
        else:
            animal = PackAnimal(name, None, None, commands)
        registry = Registry()
        registry.add_animal(animal)
        self.accept()