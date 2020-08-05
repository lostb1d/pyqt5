from PyQt5.QtWidgets import QMainWindow,  QApplication, QLabel , QDialog, QVBoxLayout , QRadioButton , QHBoxLayout , QGroupBox
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap

class Window(QDialog):
    def  __init__(self):
        super().__init__()
        self.title="Learning PyQt5"
        self.top=100
        self.left=100
        self.width=400
        self.height=300
        self.iconName = "logo.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.radioButton()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Britannic",20))
        vbox.addWidget(self.label)


        self.setLayout(vbox)

        self.show()

    def radioButton(self):
        self.groupBox = QGroupBox("What is your favorite sport?")
        self.groupBox.setFont(QtGui.QFont("Comic Sans MS",14))

        hboxLayout = QHBoxLayout()
        self.radiobtn1 = QRadioButton("Football")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.setIcon(QtGui.QIcon("football.png"))
        self.radiobtn1.setIconSize(QtCore.QSize(40,40))
        self.radiobtn1.setFont(QtGui.QFont("Bernard MT",12))
        self.radiobtn1.toggled.connect(self.onRadioBtn)
        hboxLayout.addWidget(self.radiobtn1)

        self.radiobtn2 = QRadioButton("Cricket")
        self.radiobtn2.setChecked(False)
        self.radiobtn2.setIcon(QtGui.QIcon("cricket.png"))
        self.radiobtn2.setIconSize(QtCore.QSize(40,40))
        self.radiobtn2.setFont(QtGui.QFont("Bernard MT",12))
        self.radiobtn2.toggled.connect(self.onRadioBtn)
        hboxLayout.addWidget(self.radiobtn2)

        self.radiobtn3 = QRadioButton("Tennis")
        self.radiobtn3.setChecked(False)
        self.radiobtn3.setIcon(QtGui.QIcon("tennis.png"))
        self.radiobtn3.setIconSize(QtCore.QSize(40,40))
        self.radiobtn3.setFont(QtGui.QFont("Bernard MT",12))
        self.radiobtn3.toggled.connect(self.onRadioBtn)
        hboxLayout.addWidget(self.radiobtn3)

        self.groupBox.setLayout(hboxLayout)

    def onRadioBtn(self):
        radioBtn = self.sender()

        if radioBtn.isChecked():
            self.label.setText("You have selected " + radioBtn.text())




if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
