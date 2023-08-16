from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QCheckBox, QHBoxLayout, QLineEdit, QMainWindow, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('PasswordTool')
        self.layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        self.add_settings()

    def add_settings(self):
        checkbox_layout = QHBoxLayout()
        checkbox_titles = ("lowercase", "UPPERCASE", "Numbers", "Symbols")
        for checkbox_title in checkbox_titles:
            checkbox = QCheckBox(checkbox_title)
            checkbox_layout.addWidget(checkbox)
        self.layout.addLayout(checkbox_layout)

        length_layout = QHBoxLayout()
        length = QLineEdit()
        length.setPlaceholderText("Length")
        length.setInputMask("9999")
        length.setAlignment(Qt.AlignmentFlag.AlignRight)
        length_layout.addWidget(length)
        self.layout.addLayout(length_layout)
