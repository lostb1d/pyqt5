from PyQt5.QtWidgets import QMainWindow,  QApplication, QPushButton
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title="Learning PyQt5"
        self.top=100
        self.left=100
        self.width=400
        self.height=300
        self.InitWindow()
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top, self.width, self.height)\
        
        self.UiComponents()

        self.show()
    
    def UiComponents(self):
        button = QPushButton("Click Me !!", self)
        # button.move(50,50)
        button.setGeometry(QRect(100,100,111,40))
        button.setIcon(QtGui.QIcon("logo.png"))
        button.setIconSize(QtCore.QSize(40,40))
        button.setToolTip("This is a click me demo button.")
        button.clicked.connect(self.ClickMe)

    def ClickMe(self):
        print("Button Clicked  & Closing")
        sys.exit()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())