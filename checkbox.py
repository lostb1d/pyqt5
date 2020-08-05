from PyQt5.QtWidgets import QMainWindow,  QApplication, QLabel , QDialog, QVBoxLayout , QRadioButton , QHBoxLayout , QGroupBox, QCheckBox
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap

class Window(QDialog):
    def  __init__(self):
        super().__init__()
        self.title="PyQt CheckBox"
        self.top=100
        self.left=100
        self.width=400
        self.height=120
        self.iconName = "logo.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.createCheckBox()

        vbox = QVBoxLayout()
        vbox.addWidget(self.groupbox)

        self.label = QLabel("Hello")
        self.label.setFont(QtGui.QFont("Algerian",12))
        vbox.addWidget(self.label)


        self.setLayout(vbox)
        self.show()

    def createCheckBox(self):
        self.groupbox = QGroupBox("Which programming language do you recommend?")
        self.groupbox.setFont(QtGui.QFont("Times New Roman", 14))
        hboxLayout = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon("python.png"))
        self.check1.setIconSize(QtCore.QSize(40,40))
        self.check1.toggled.connect(self.onCheckBoxToggled)
        hboxLayout.addWidget(self.check1)

        self.check2 = QCheckBox("Java")
        self.check2.setIcon(QtGui.QIcon("java.png"))
        self.check2.setIconSize(QtCore.QSize(40,40))
        self.check2.toggled.connect(self.onCheckBoxToggled)
        hboxLayout.addWidget(self.check2)

        self.check3 = QCheckBox("C++")
        self.check3.setIcon(QtGui.QIcon("cpp.png"))
        self.check3.setIconSize(QtCore.QSize(40,40))
        self.check3.toggled.connect(self.onCheckBoxToggled)
        hboxLayout.addWidget(self.check3)

        self.check4 = QCheckBox("C#")
        self.check4.setIcon(QtGui.QIcon("csharp.png"))
        self.check4.setIconSize(QtCore.QSize(40,40))
        self.check4.toggled.connect(self.onCheckBoxToggled)
        hboxLayout.addWidget(self.check4)

        self.groupbox.setLayout(hboxLayout)

    def onCheckBoxToggled(self):
        if self.check1.isChecked():
            self.label.setText("You have selected : " + self.check1.text())
        if self.check2.isChecked():
            self.label.setText("You have selected : " + self.check2.text())
        if self.check3.isChecked():
            self.label.setText("You have selected : " + self.check3.text())
        if self.check4.isChecked():
            self.label.setText("You have selected : " + self.check4.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
