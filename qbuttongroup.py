from PyQt5.QtWidgets import QMainWindow,  QApplication, QLabel , QDialog, QVBoxLayout , QRadioButton , QHBoxLayout , QGroupBox, QCheckBox , QWidget , QPushButton, QLineEdit , QButtonGroup
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title="QLine Edit"
        self.top=100
        self.left=100
        self.width=400
        self.height=120
        self.iconName = "logo.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        self.label = QLabel("Hello")
        hbox.addWidget(self.label)
        self.label.setFont(QtGui.QFont("Algerian",14))

        self.buttongroup = QButtonGroup()
        self.buttongroup.buttonClicked[int].connect(self.onButtonClicked)

        btn1 = QPushButton("Python")
        btn1.setIcon(QtGui.QIcon("python.png"))
        self.buttongroup.addButton(btn1,1)
        hbox.addWidget(btn1)

        btn2 = QPushButton("Java")
        btn2.setIcon(QtGui.QIcon("java.png"))
        self.buttongroup.addButton(btn2,2)
        hbox.addWidget(btn2)

        btn3 = QPushButton("C++")
        btn3.setIcon(QtGui.QIcon("Cpp.png"))
        self.buttongroup.addButton(btn3,3)
        hbox.addWidget(btn3)
        self.setLayout(hbox)

        self.show()

    def onButtonClicked(self,id):
        for button in self.buttongroup.buttons():
            if button is self.buttongroup.button(id):
                self.label.setText(button.text()+ " Clicked!")

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())