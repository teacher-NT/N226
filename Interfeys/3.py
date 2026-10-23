import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QCheckBox,
    QRadioButton, QMessageBox
)

style_menu = """
    font-size: 20px;
    background-color: #66d8f2;
    border: 2px solid black;
"""
style_checkbox = """
    font-size: 20px;
    color: #f57fa1;
"""

style_radio = """
    font-size: 18px;
    color: #b664fa;
"""

style_btn1 = """
            QPushButton {
            font-size: 20px;
            font-weight: bold;
            background-color: #5beb34;
            border: 2px solid black;
            border-radius: 20px;
            padding: 15px;
            }
            QPushButton:hover {
                background-color: red;
            }
        """


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QVBoxLayout()
        self.setWindowTitle("Dastur")
        self.setGeometry(1200, 200, 400, 700)

        self.matn1 = QLabel("Milliy Taomlarga Xush kelibsiz")
        self.matn1.setStyleSheet("font-size: 30px; color: red;")

        self.vbox.addWidget(self.matn1)

        self.matn2 = QLabel("Taom savatingiz bo'sh")
        self.matn2.setStyleSheet("font-size: 25px;")
        self.vbox.addWidget(self.matn2)

        self.matn3 = QLabel("Tanlangan ichimliklar")
        self.matn3.setStyleSheet("font-size: 25px;")
        self.vbox.addWidget(self.matn3)

        self.add_combo()
        self.add_checkbox()
        self.add_radio()

        self.btn1 = QPushButton("Buyurtma berish")
        self.btn1.setStyleSheet(style_btn1)
        self.btn1.clicked.connect(self.show_order)
        self.vbox.addWidget(self.btn1)

        
        self.setLayout(self.vbox)
        self.show()

    def add_combo(self):
        self.menu = QComboBox()
        self.menu.addItems(["Ovqatlar", "Lag'mon", "Qo'ziqorinli soup", "Manti", "Osh", "Qoshonkabob", "Somsa"])
        self.menu.setStyleSheet(style_menu)
        self.menu.currentTextChanged.connect(self.choice_food)
        self.vbox.addWidget(self.menu)

    def choice_food(self):
        food_name = self.menu.currentText()
        text = f"Siz tanlagan taom: {food_name}"
        self.matn2.setText(text)
        return text


    def add_checkbox(self):
        self.ch1 = QCheckBox("Kofe")
        self.ch1.setStyleSheet(style_checkbox)
        self.ch1.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch1)

        self.ch2 = QCheckBox("Choy")
        self.ch2.setStyleSheet(style_checkbox)
        self.ch2.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch2)

        self.ch3 = QCheckBox("Ays tea")
        self.ch3.setStyleSheet(style_checkbox)
        self.ch3.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch3)

        self.ch4 = QCheckBox("RedBull")
        self.ch4.setStyleSheet(style_checkbox)
        self.ch4.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch4)        

        self.ch5 = QCheckBox("Cola")
        self.ch5.setStyleSheet(style_checkbox)
        self.ch5.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch5)

        self.ch6 = QCheckBox("Kakteyl")
        self.ch6.setStyleSheet(style_checkbox)
        self.ch6.stateChanged.connect(self.set_drink)
        self.vbox.addWidget(self.ch6)

    def set_drink(self):
        drinks = []
        if self.ch1.isChecked():
            drinks.append(self.ch1.text())
        if self.ch2.isChecked():
            drinks.append(self.ch2.text())
        if self.ch3.isChecked():
            drinks.append(self.ch3.text())
        if self.ch4.isChecked():
            drinks.append(self.ch4.text())
        if self.ch5.isChecked():
            drinks.append(self.ch5.text())
        if self.ch6.isChecked():
            drinks.append(self.ch6.text())
        drinks = "\n- ".join(drinks)
        self.matn3.setText(f"Tanlangan ichimliklar:\n- {drinks}")   
        return drinks

    def add_radio(self):
        self.r_buttons = [
            QRadioButton("Naqd"),
            QRadioButton("Plastik"),
            QRadioButton("Onlayn")
        ]
        for i in range(len(self.r_buttons)):
            self.vbox.addWidget(self.r_buttons[i])
            self.r_buttons[i].setStyleSheet(style_radio)

    def show_order(self):
        food = self.choice_food()
        drinks = self.set_drink()
        for i in self.r_buttons:
            if i.isChecked():
                payment = i.text()
                break
        QMessageBox.information(self, "Sizning buyurtmangiz",
                                 f"{food}\nIchimliklar:\n{drinks}\nTo'lov turi: {payment}")

app = QApplication([])
win = Window()
app.exec_()