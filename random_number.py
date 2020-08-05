from PyQt5.QtWidgets import QApplication, QWidget , QLCDNumber, QLabel, QVBoxLayout, QPushButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from random import randint

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title="Random Number Generator"
        self.top=100
        self.left=100
        self.width=400
        self.height=120
        self.iconName = "logo.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitUI()
        self.show()

    def InitUI(self):

        vbox = QVBoxLayout()

        self.lcd = QLCDNumber()
        self.lcd.display("0")
        
        vbox.addWidget(self.lcd)

        self.button = QPushButton("Randomize")
        self.button.clicked.connect(self.LCDHandler)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def LCDHandler(self):
        random = randint(1,48)
        self.lcd.display(random)
    

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())