import sys
import json
import os

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QCalendarWidget,
    QLineEdit,
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QCheckBox,
    QMessageBox
)

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class Sozlamalar(QDialog):
    def __init__(self, ota, malumot):
        super().__init__()

        self.ota = ota

        self.setWindowTitle("Sozlamalar")
        self.setFixedSize(400, 450)

        self.setStyleSheet("""
            QDialog {
                background-color: #FFF0F5;
            }

            QLabel {
                color: #8B4A67;
                font-size: 18px;
                font-weight: bold;
            }

            QLineEdit {
                background-color: white;
                border: 2px solid #F2B6C9;
                border-radius: 12px;
                padding: 10px;
                font-size: 16px;
                color: #6E4052;
            }

            QPushButton {
                background-color: #F2A9C2;
                color: white;
                border: none;
                border-radius: 12px;
                padding: 12px;
                font-size: 17px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #E88EAD;
            }
        """)

        layout = QVBoxLayout()

        self.ism_label = QLabel("Ismingiz:")
        self.ism = QLineEdit()
        self.ism.setText(malumot.get("ism", ""))

        self.yosh_label = QLabel("Yoshingiz:")
        self.yosh = QLineEdit()
        self.yosh.setText(malumot.get("yosh", ""))

        self.sana_label = QLabel("Tug'ilgan sanangiz:")
        self.sana = QLineEdit()
        self.sana.setPlaceholderText("Masalan: 17.09.2007")
        self.sana.setText(malumot.get("tugilgan_sana", ""))

        self.saqlash = QPushButton("Saqlash")
        self.saqlash.clicked.connect(self.saqlash_malumot)

        layout.addWidget(self.ism_label)
        layout.addWidget(self.ism)

        layout.addWidget(self.yosh_label)
        layout.addWidget(self.yosh)

        layout.addWidget(self.sana_label)
        layout.addWidget(self.sana)

        layout.addStretch()
        layout.addWidget(self.saqlash)

        self.setLayout(layout)

    def saqlash_malumot(self):
        ism = self.ism.text().strip()
        yosh = self.yosh.text().strip()
        sana = self.sana.text().strip()

        if ism == "":
            QMessageBox.warning(
                self,
                "Xatolik",
                "Iltimos, ismingizni kiriting!"
            )
            return

        self.ota.malumot["ism"] = ism
        self.ota.malumot["yosh"] = yosh
        self.ota.malumot["tugilgan_sana"] = sana

        self.ota.malumot_saqlash()
        self.ota.ism.setText(ism)

        QMessageBox.information(
            self,
            "Saqlandi",
            "Ma'lumotlaringiz saqlandi!"
        )

        self.close()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("To Do List")
        self.setGeometry(500, 100, 800, 900)

        self.fayl = "todo_malumot.json"

        self.malumot = {
            "ism": "Oygul",
            "yosh": "",
            "tugilgan_sana": "",
            "vazifalar": {}
        }

        self.malumot_yuklash()

        self.rasm = QLabel(self)

        pixmap = QPixmap(
            "C:/Users/hp/Desktop/4-oy/to_do_list/download.jpg"
        )

        self.rasm.setPixmap(pixmap)
        self.rasm.setScaledContents(True)

        self.ism = QLabel(
            self.malumot.get("ism", "Oygul"),
            self
        )

        self.ism.setStyleSheet("""
            QLabel {
                color: #8B4A67;
                font-size: 30px;
                font-weight: bold;
                background-color: rgba(255, 255, 255, 170);
                border-radius: 15px;
                padding: 5px 15px;
            }
        """)

        self.menyu = QPushButton("☰", self)

        self.menyu.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 190);
                color: #8B4A67;
                border: none;
                border-radius: 15px;
                font-size: 30px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #FFE1EB;
            }
        """)

        self.menyu.clicked.connect(
            self.sozlamalarni_ochish
        )

        self.kalendar = QCalendarWidget(self)

        self.kalendar.setGridVisible(True)

        self.kalendar.setStyleSheet("""
            QCalendarWidget {
                background-color: white;
                border: 1px solid #F2B6C9;
                border-radius: 10px;
            }

            QCalendarWidget QWidget {
                background-color: white;
            }

            QCalendarWidget QToolButton {
                color: #8B4A67;
                background-color: white;
                border: none;
                font-size: 15px;
                padding: 4px;
            }

            QCalendarWidget QToolButton:hover {
                background-color: #FFE8F0;
            }

            QCalendarWidget QSpinBox {
                color: #8B4A67;
                background-color: white;
                border: none;
            }

            QCalendarWidget QAbstractItemView {
                background-color: white;
                color: #6E4052;
                selection-background-color: #F2A9C2;
                selection-color: white;
                font-size: 14px;
                border: none;
            }
        """)

        self.kalendar.clicked.connect(
            self.sana_ozgardi
        )

        self.sarlavha = QLabel(
            "Bugungi vazifalar",
            self
        )

        self.sarlavha.setStyleSheet("""
            QLabel {
                color: #8B4A67;
                font-size: 24px;
                font-weight: bold;
                background-color: rgba(255, 255, 255, 180);
                border-radius: 15px;
                padding: 8px 15px;
            }
        """)

        self.vazifalar_widget = QWidget(self)

        self.vazifalar_widget.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 170);
                border-radius: 20px;
            }
        """)

        self.vazifalar_layout = QVBoxLayout()

        self.vazifalar_layout.setContentsMargins(
            20,
            15,
            20,
            15
        )

        self.vazifalar_layout.setSpacing(10)

        self.vazifalar_widget.setLayout(
            self.vazifalar_layout
        )

        self.qoshish = QPushButton("+", self)

        self.qoshish.setFixedSize(75, 75)

        self.qoshish.setStyleSheet("""
            QPushButton {
                background-color: #F2A9C2;
                color: white;
                border: 4px solid white;
                border-radius: 37px;
                font-size: 42px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #E88EAD;
            }

            QPushButton:pressed {
                background-color: #D9799B;
            }
        """)

        self.qoshish.clicked.connect(
            self.vazifa_qoshish
        )

        self.vazifalarni_chiqarish()

    def malumot_yuklash(self):
        if os.path.exists(self.fayl):

            try:
                with open(
                    self.fayl,
                    "r",
                    encoding="utf-8"
                ) as fayl:

                    yuklangan = json.load(fayl)

                self.malumot.update(
                    yuklangan
                )

            except:
                pass

    def malumot_saqlash(self):
        with open(
            self.fayl,
            "w",
            encoding="utf-8"
        ) as fayl:

            json.dump(
                self.malumot,
                fayl,
                ensure_ascii=False,
                indent=4
            )

    def sana(self):

        sana = self.kalendar.selectedDate()

        return sana.toString(
            "yyyy-MM-dd"
        )

    def sana_ozgardi(self):

        self.vazifalarni_chiqarish()

        sana = self.kalendar.selectedDate()

        sana_matn = sana.toString(
            "dd.MM.yyyy"
        )

        self.sarlavha.setText(
            sana_matn + " vazifalari"
        )

    def vazifa_qoshish(self):

        dialog = QDialog(self)

        dialog.setWindowTitle(
            "Yangi vazifa"
        )

        dialog.setFixedSize(
            400,
            200
        )

        dialog.setStyleSheet("""
            QDialog {
                background-color: #FFF0F5;
            }

            QLabel {
                color: #8B4A67;
                font-size: 20px;
                font-weight: bold;
            }

            QLineEdit {
                background-color: white;
                border: 2px solid #F2B6C9;
                border-radius: 12px;
                padding: 10px;
                font-size: 17px;
                color: #6E4052;
            }

            QPushButton {
                background-color: #F2A9C2;
                color: white;
                border: none;
                border-radius: 12px;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #E88EAD;
            }
        """)

        layout = QVBoxLayout()

        label = QLabel(
            "Yangi vazifani kiriting:"
        )

        input_vazifa = QLineEdit()

        input_vazifa.setPlaceholderText(
            "Masalan: Python darsini qilish"
        )

        tugmalar = QHBoxLayout()

        saqlash = QPushButton(
            "Qo'shish"
        )

        bekor = QPushButton(
            "Bekor qilish"
        )

        tugmalar.addWidget(
            bekor
        )

        tugmalar.addWidget(
            saqlash
        )

        layout.addWidget(
            label
        )

        layout.addWidget(
            input_vazifa
        )

        layout.addLayout(
            tugmalar
        )

        dialog.setLayout(
            layout
        )

        bekor.clicked.connect(
            dialog.close
        )

        def qoshish():

            matn = input_vazifa.text().strip()

            if matn == "":
                QMessageBox.warning(
                    dialog,
                    "Xatolik",
                    "Vazifani kiriting!"
                )
                return

            sana = self.sana()

            if sana not in self.malumot["vazifalar"]:
                self.malumot["vazifalar"][sana] = []

            self.malumot["vazifalar"][sana].append({
                "matn": matn,
                "bajarildi": False
            })

            self.malumot_saqlash()

            self.vazifalarni_chiqarish()

            dialog.close()

        saqlash.clicked.connect(
            qoshish
        )

        dialog.exec_()

    def vazifalarni_chiqarish(self):

        while self.vazifalar_layout.count():

            item = self.vazifalar_layout.takeAt(0)

            widget = item.widget()

            if widget:
                widget.deleteLater()

        sana = self.sana()

        vazifalar = self.malumot[
            "vazifalar"
        ].get(
            sana,
            []
        )

        if len(vazifalar) == 0:

            bosh = QLabel(
                "Bu kun uchun vazifalar yo'q 🌸"
            )

            bosh.setStyleSheet("""
                QLabel {
                    color: #A66A80;
                    font-size: 17px;
                    background-color: transparent;
                    padding: 10px;
                }
            """)

            bosh.setAlignment(
                Qt.AlignCenter
            )

            self.vazifalar_layout.addWidget(
                bosh
            )

            return

        for raqam, vazifa in enumerate(vazifalar):

            checkbox = QCheckBox(
                vazifa["matn"],
                self.vazifalar_widget
            )

            checkbox.setChecked(
                vazifa["bajarildi"]
            )

            if vazifa["bajarildi"]:

                checkbox.setStyleSheet("""
                    QCheckBox {
                        background-color: #FCE8EF;
                        color: #A97B8A;
                        border-radius: 12px;
                        padding: 12px;
                        font-size: 17px;
                        text-decoration: line-through;
                    }

                    QCheckBox::indicator {
                        width: 22px;
                        height: 22px;
                    }

                    QCheckBox::indicator:checked {
                        border: 2px solid #E58AA9;
                        border-radius: 6px;
                        background-color: #F2A9C2;
                    }
                """)

            else:

                checkbox.setStyleSheet("""
                    QCheckBox {
                        background-color: #FFF7FA;
                        color: #6E4052;
                        border-radius: 12px;
                        padding: 12px;
                        font-size: 17px;
                    }

                    QCheckBox:hover {
                        background-color: #FFE8F0;
                    }

                    QCheckBox::indicator {
                        width: 22px;
                        height: 22px;
                    }

                    QCheckBox::indicator:unchecked {
                        border: 2px solid #E5A5BA;
                        border-radius: 6px;
                        background-color: white;
                    }

                    QCheckBox::indicator:checked {
                        border: 2px solid #E58AA9;
                        border-radius: 6px;
                        background-color: #F2A9C2;
                    }
                """)

            def bajarildi(
                holat,
                index=raqam
            ):

                self.malumot[
                    "vazifalar"
                ][sana][index][
                    "bajarildi"
                ] = holat

                self.malumot_saqlash()

                self.vazifalarni_chiqarish()

            checkbox.stateChanged.connect(
                bajarildi
            )

            self.vazifalar_layout.addWidget(
                checkbox
            )

    def sozlamalarni_ochish(self):

        oynacha = Sozlamalar(
            self,
            self.malumot
        )

        oynacha.exec_()

    def resizeEvent(self, event):

        self.rasm.setGeometry(
            0,
            0,
            self.width(),
            self.height()
        )

        self.ism.adjustSize()

        self.ism.move(
            25,
            20
        )

        self.menyu.setGeometry(
            self.width() - 80,
            20,
            55,
            55
        )

        kalendar_kenglik = 500
        kalendar_balandlik = 230

        self.kalendar.setGeometry(
            (self.width() - kalendar_kenglik) // 2,
            100,
            kalendar_kenglik,
            kalendar_balandlik
        )

        self.sarlavha.adjustSize()

        self.sarlavha.move(
            (self.width() - self.sarlavha.width()) // 2,
            345
        )

        vazifa_kenglik = 600
        vazifa_balandlik = 300

        self.vazifalar_widget.setGeometry(
            (self.width() - vazifa_kenglik) // 2,
            395,
            vazifa_kenglik,
            vazifa_balandlik
        )

        x = (
            self.width()
            - self.qoshish.width()
        ) // 2

        y = (
            self.height()
            - self.qoshish.height()
            - 30
        )

        self.qoshish.move(
            x,
            y
        )


app = QApplication(sys.argv)

oyna = Window()

oyna.show()

sys.exit(
    app.exec_()
)