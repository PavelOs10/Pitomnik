from PyQt5.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit
from PyQt5.QtCore import Qt

class CommandsDialog(QDialog):
    def __init__(self, animal_id, animal_name, current_commands, db_handler, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"Commands for {animal_name}")
        self.setFixedSize(400, 300)
        
        self.animal_id = animal_id
        self.animal_name = animal_name
        self.current_commands = current_commands
        self.db_handler = db_handler
        
        self.init_ui()
    
    def init_ui(self):
        layout = QVBoxLayout()
        
        self.commands_label = QLabel(f"Current commands for {self.animal_name}:")
        layout.addWidget(self.commands_label)
        
        self.commands_text_edit = QTextEdit()
        self.commands_text_edit.setText(self.current_commands)
        self.commands_text_edit.setReadOnly(True)
        layout.addWidget(self.commands_text_edit)
        
        self.new_command_input = QLineEdit()
        self.new_command_input.setPlaceholderText("Enter new command")
        layout.addWidget(self.new_command_input)
        
        buttons_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Add Command")
        self.add_button.clicked.connect(self.add_command)
        buttons_layout.addWidget(self.add_button)
        
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_commands)
        buttons_layout.addWidget(self.save_button)
        
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.close)
        buttons_layout.addWidget(self.cancel_button)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
    
    def add_command(self):
        new_command = self.new_command_input.text().strip()
        if new_command:
            current_text = self.commands_text_edit.toPlainText()
            updated_text = f"{current_text}\n{new_command}" if current_text else new_command
            self.commands_text_edit.setText(updated_text)
            self.new_command_input.clear()
    
    def save_commands(self):
        updated_commands = self.commands_text_edit.toPlainText().strip()
        if updated_commands:
           
            self.db_handler.update_animal_commands(self.animal_id, updated_commands)
        self.close()