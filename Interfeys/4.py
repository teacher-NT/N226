import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QLineEdit
)
from PyQt5.QtCore import Qt



style_body2 = """
    background-color: black;
"""
style_sarlavha2 = """
    font-size: 40px;
    color: white;
    font-weight: bold;
"""

style_btn2 = """
    font-size: 20px;
    color: blue;
    background-color: white;
    border: 2px solid grey;
    border-radius: 20px;
    padding: 15px;
"""

class AboutWindow(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setGeometry(1200, 200, 400, 700)
        self.setStyleSheet(style_body2)
        self.vbox = QVBoxLayout()

        self.sarlavha = QLabel("About Us")
        self.sarlavha.setStyleSheet(style_sarlavha)
        self.sarlavha.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.vbox.addWidget(self.sarlavha)

        self.btn1 = QPushButton("Back")
        self.btn1.setStyleSheet(style_btn2)
        self.btn1.clicked.connect(self.open_back)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)

    def open_back(self):
        self.main.show()
        self.hide()




style_body = """
    background-color: black;
"""
style_sarlavha = """
    font-size: 40px;
    color: red;
    font-weight: bold;
"""

style_btn1 = """
    font-size: 20px;
    color: red;
    background-color: white;
    border: 2px solid grey;
    border-radius: 20px;
    padding: 15px;
"""

style_edit1 = """
    font-size: 20px;
    background-color: white;
    padding: 5px;
"""

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(1200, 200, 400, 700)
        self.setStyleSheet(style_body)
        self.vbox = QVBoxLayout()

        self.sarlavha = QLabel("Welcome to App")
        self.sarlavha.setStyleSheet(style_sarlavha)
        self.sarlavha.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.vbox.addWidget(self.sarlavha)

        self.edit = QLineEdit()
        self.edit.setPlaceholderText("nimadir kiriting")
        self.edit.setStyleSheet(style_edit1)
        self.vbox.addWidget(self.edit)

        self.btn1 = QPushButton("Next")
        self.btn1.setStyleSheet(style_btn1)
        self.btn1.clicked.connect(self.open_about)
        self.vbox.addWidget(self.btn1)

        self.setLayout(self.vbox)
        self.show()

    def open_about(self):
        self.second = AboutWindow(self)
        self.second.show()
        self.hide()

app = QApplication([])
win = MainWindow()
app.exec_()