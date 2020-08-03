from PyQt5.QtWidgets import  QApplication, QPushButton , QDialog , QGroupBox, QHBoxLayout, QVBoxLayout , QGridLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title="Grid Layout"
        self.top=100
        self.left=100
        self.width=400
        self.height=100
        self.iconName = "logo.png"

        self.InitWindow()
    
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon(self.iconName))

        self.CreateLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)
        

        self.show()

    def CreateLayout(self):
        self.groupBox = QGroupBox("What is your favorite programming language?")
        gridLayout = QGridLayout()

        button = QPushButton("Python", self)
        button.setIcon(QtGui.QIcon("python.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("Python")
        button.setMinimumHeight(40)
        gridLayout.addWidget(button, 0,0)

        button1 = QPushButton("Java", self)
        button1.setIcon(QtGui.QIcon("java.png"))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setToolTip("Java")
        button1.setMinimumHeight(40)
        gridLayout.addWidget(button, 0,1)

        button2 = QPushButton("C++", self)
        button2.setIcon(QtGui.QIcon("cpp.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setToolTip("C++")
        button2.setMinimumHeight(40)
        gridLayout.addWidget(button,1,0)

        button3 = QPushButton("C#", self)
        button3.setIcon(QtGui.QIcon("csharp.png"))
        button3.setIconSize(QtCore.QSize(40,40))
        button3.setToolTip("C#")
        button3.setMinimumHeight(40)
        gridLayout.addWidget(button,1,1)


        self.groupBox.setLayout(gridLayout)

if __name__== "__main__":
    App = QApplication(sys.argv)
    window= Window()
    sys.exit(App.exec())
