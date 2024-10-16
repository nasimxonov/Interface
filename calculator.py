from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox
import sys
from PyQt5.QtGui import QFont

class CalculatorWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 300)
        
        self.setStyleSheet("background-color: #ADD8E6;")

        self.ason = QLineEdit(self)
        self.ason.setPlaceholderText("A son kiriting")
        self.ason.setFont(QFont("Poppins", 18))

        self.bson = QLineEdit(self)
        self.bson.setPlaceholderText("B son kiriting")
        self.bson.setFont(QFont("Poppins", 18))
        
        self.qoshish = QPushButton("+", self)
        self.qoshish.setFont(QFont("Poppins", 18))
        self.qoshish.clicked.connect(self.qosh)
        
        self.ayirish = QPushButton("-", self)
        self.ayirish.setFont(QFont("Poppins", 18))
        self.ayirish.clicked.connect(self.ayir)
        
        self.kopaytirish = QPushButton("*", self)
        self.kopaytirish.setFont(QFont("Poppins", 18))
        self.kopaytirish.clicked.connect(self.kopaytir)
        
        self.bulish = QPushButton("/", self)
        self.bulish.setFont(QFont("Poppins", 18))
        self.bulish.clicked.connect(self.bol)
        
        self.nnatija = QLabel("Natija: ", self)
        self.nnatija.setFont(QFont("Poppins", 18))
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.ason)
        vbox.addWidget(self.bson)
        
        hbox = QHBoxLayout()
        hbox.addWidget(self.qoshish)
        hbox.addWidget(self.ayirish)
        hbox.addWidget(self.kopaytirish)
        hbox.addWidget(self.bulish)
        
        vbox.addLayout(hbox)
        vbox.addWidget(self.nnatija)
        
        self.setLayout(vbox)

    def qosh(self):
        self.hisoblash('+')

    def ayir(self):
        self.hisoblash('-')

    def kopaytir(self):
        self.hisoblash('*')

    def bol(self):
        self.hisoblash('/')

    def hisoblash(self, amallar):
        try:
            a = float(self.ason.text())
            b = float(self.bson.text())

            if amallar == '+':
                result = a + b
            elif amallar == '-':
                result = a - b
            elif amallar == '*':
                result = a * b
            elif amallar == '/':
                if b == 0:
                    raise ZeroDivisionError
                result = a / b

            self.nnatija.setText(f"Natija: {result}")
        
        except ValueError:
            QMessageBox.warning(self, "Xatolik", "Iltimos raqamlarni tog'ri kiriting")
        except ZeroDivisionError:
            QMessageBox.warning(self, "Xatolik", "0 ga bo'lish mumkinmas")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec_())
