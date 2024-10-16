from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import QDateTime
import sys

class TextSwitcher(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Qandaydir Dastur')
        self.setGeometry(100, 100, 500, 300)

        self.input_text = QLineEdit(self)
        
        self.result_label = QLabel("Result: ", self)
        self.result_text = QLineEdit(self)
        self.result_text.setReadOnly(True)
        
        self.lower_button = QPushButton("Lower", self)
        self.upper_button = QPushButton("Upper", self)
        self.length_button = QPushButton("Length", self)
        self.reverse_button = QPushButton("Reverse", self)
        self.time_button = QPushButton("Time now", self)
        self.capitalize_button = QPushButton("Capitalize", self)
        self.clear_button = QPushButton("Clear", self)

        self.lower_button.clicked.connect(self.to_lower)
        self.upper_button.clicked.connect(self.to_upper)
        self.length_button.clicked.connect(self.get_length)
        self.reverse_button.clicked.connect(self.reverse_text)
        self.time_button.clicked.connect(self.show_time)
        self.capitalize_button.clicked.connect(self.capitalize_text)
        self.clear_button.clicked.connect(self.clear_text)

        a = QVBoxLayout()
        button_layout = QHBoxLayout()

        a.addWidget(self.input_text)
        a.addWidget(self.result_label)
        a.addWidget(self.result_text)

        button_layout.addWidget(self.lower_button)
        button_layout.addWidget(self.upper_button)
        button_layout.addWidget(self.length_button)
        button_layout.addWidget(self.reverse_button)
        button_layout.addWidget(self.time_button)
        button_layout.addWidget(self.capitalize_button)
        
        a.addLayout(button_layout)
        a.addWidget(self.clear_button)

        self.setLayout(a)

    def to_lower(self):
        text = self.input_text.text()
        self.result_text.setText(text.lower())

    def to_upper(self):
        text = self.input_text.text()
        self.result_text.setText(text.upper())

    def get_length(self):
        text = self.input_text.text()
        length = len(text)
        self.result_text.setText(f"Length: {length}")

    def reverse_text(self):
        text = self.input_text.text()
        self.result_text.setText(text[::-1])

    def show_time(self):
        current_time = QDateTime.currentDateTime().toString()
        self.result_text.setText(f"Time: {current_time}")

    def capitalize_text(self):
        text = self.input_text.text()
        self.result_text.setText(text.capitalize())

    def clear_text(self):
        self.input_text.clear()
        self.result_text.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TextSwitcher()
    window.show()
    sys.exit(app.exec_())
