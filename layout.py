from PyQt5.QtWidgets import  QApplication, QPushButton , QDialog , QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title="Layout Management"
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

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        
        self.show()
    
    def createLayout(self):
        self.groupBox = QGroupBox("Whats your favorite sport?")
        hboxlayout = QHBoxLayout()

        button = QPushButton("Football", self)
        button.setIcon(QtGui.QIcon("football.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("Football")
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button)

        button1 = QPushButton("Cricket", self)
        button1.setIcon(QtGui.QIcon("cricket.png"))
        button1.setIconSize(QtCore.QSize(40,40))
        button1.setToolTip("Cricket")
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button1)

        button2 = QPushButton("Tennis", self)
        button2.setIcon(QtGui.QIcon("tennis.png"))
        button2.setIconSize(QtCore.QSize(40,40))
        button2.setToolTip("Tennis")
        button.setMinimumHeight(40)
        hboxlayout.addWidget(button2)

        self.groupBox.setLayout(hboxlayout)
            
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
