import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton
)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dastur")
        self.setGeometry(1200, 200, 400, 700)

        self.matn1 = QLabel(self)
        self.matn1.setText("Welcome to My App")
        self.matn1.setStyleSheet("font-size: 30px; color: red;")
        self.matn1.move(65, 50)

        self.btn1 = QPushButton(self)
        self.btn1.setText("OK")
        self.btn1.setGeometry(125, 640,  150, 50)
        self.btn1.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            background-color: #5beb34;
            border: 2px solid black;
            border-radius: 20px;
        """)
        self.show()


app = QApplication([])
win = Window()

# oyna = QWidget()
# oyna.setWindowTitle("Dastur")
# oyna.setGeometry(1200, 200, 400, 700)

# matn1 = QLabel(oyna)
# matn1.setText("Welcome to My App")
# matn1.setStyleSheet("font-size: 30px; color: red;")
# matn1.move(65, 50)

# btn1 = QPushButton(oyna)
# btn1.setText("OK")
# btn1.setGeometry(125, 640,  150, 50)
# btn1.setStyleSheet("""
#     font-size: 20px;
#     font-weight: bold;
#     background-color: #5beb34;
#     border: 2px solid black;
#     border-radius: 20px;
# """)


# oyna.show()
app.exec_()