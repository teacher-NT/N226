import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox
)

style_menu = """
    font-size: 20px;
    background-color: #66d8f2;
    border: 2px solid black;
"""


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur")
        self.setGeometry(1200, 200, 400, 700)

        self.matn1 = QLabel("Welcome to My App")
        self.matn1.setStyleSheet("font-size: 30px; color: red;")

        self.vbox.addWidget(self.matn1)

        self.matn2 = QLabel("Taom savatingiz bo'sh")
        self.matn2.setStyleSheet("font-size: 25px;")
        self.vbox.addWidget(self.matn2)

        self.menu = QComboBox()
        self.menu.addItems(["Ovqatlar", "Lag'mon", "Qo'ziqorinli soup", "Manti", "Osh", "Qoshonkabob", "Somsa"])
        self.menu.setStyleSheet(style_menu)
        self.menu.currentTextChanged.connect(self.choice_food)
        self.vbox.addWidget(self.menu)

        self.btn1 = QPushButton("OK")
        # self.btn1.setGeometry(125, 640,  150, 50)
        self.btn1.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            background-color: #5beb34;
            border: 2px solid black;
            border-radius: 20px;
        """)
        self.vbox.addWidget(self.btn1)

        
        self.setLayout(self.vbox)
        self.show()

    def choice_food(self):
        food_name = self.menu.currentText()
        self.matn2.setText(f"Siz tanlagan taom: {food_name}")



app = QApplication([])
win = Window()
app.exec_()