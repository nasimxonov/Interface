from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
import sys
from PyQt5.QtGui import QFont

class RegisterWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setGeometry(100, 100, 1000, 500)

        padding_y = 10  
        label_width = 300  
        input_width = 400  

        self.txt = QLabel("Username kiriting:", self)
        self.user = QLineEdit(self)
        self.user.setPlaceholderText("username...")
        self.xywh(self.txt, 30, 100, label_width, 40)
        self.xywh(self.user, 350, 100, input_width, 40)

        self.matn = QLabel("E-mail kiriting:", self)
        self.email = QLineEdit(self)
        self.email.setPlaceholderText("e-mail...")
        self.xywh(self.matn, 30, 170 + padding_y, label_width, 40)
        self.xywh(self.email, 350, 170 + padding_y, input_width, 40)

        self.label = QLabel("Parol kiriting:", self)
        self.password = QLineEdit(self)
        self.password.setPlaceholderText("parol...")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("color:white; background-color:gray;")
        self.xywh(self.label, 30, 240 + 2 * padding_y, label_width, 40)
        self.xywh(self.password, 350, 240 + 2 * padding_y, 220, 40)

        self.toggle_button = QPushButton('Show', self)
        self.toggle_button.setGeometry(580, 240 + 2 * padding_y, 100, 40)
        self.toggle_button.clicked.connect(self.toggle_password)

        self.ok = QPushButton("Submit", self)
        self.xywh(self.ok, 350, 350 + 3 * padding_y, 120, 40)

        self.reset = QPushButton("Reset", self)
        self.xywh(self.reset, 480, 350 + 3 * padding_y, 120, 40)

        self.ok.clicked.connect(self.start)
        self.reset.clicked.connect(self.remove)

        self.setStyleSheet("""
        background-color:#CCF3DD;
        """)

        self.show()

    def xywh(self, obj, x, y, width, height):
        obj.setFont(QFont("Poppins", 24))
        obj.setGeometry(x, y, width, height)

    def start(self):
        self.messege = QMessageBox(self)
        if self.user.text() == "":
            self.messege.warning(self, "Xatolik", "Siz username kiritmadingiz.")
        elif self.email.text() == "":
            self.messege.warning(self, "Xatolik", "Siz email kiritmadingiz.")
        elif self.password.text() == "":
            self.messege.warning(self, "Xatolik", "Siz parol kiritmadingiz.")
        else:
            self.messege.information(self, "Success", 
                                     f"Username: {self.user.text()}\nEmail: {self.email.text()}")

    def remove(self):
        self.user.setText("")
        self.email.setText("")
        self.password.setText("")

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure you want to quit?", 
                                     QMessageBox.Yes | QMessageBox.No, 
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def toggle_password(self):
        if self.password.echoMode() == QLineEdit.Password:
            self.password.setEchoMode(QLineEdit.Normal)
            self.toggle_button.setText("Hide")
        else:
            self.password.setEchoMode(QLineEdit.Password)
            self.toggle_button.setText("Show")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    sys.exit(app.exec_())
