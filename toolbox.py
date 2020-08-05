from PyQt5.QtWidgets import QApplication, QDialog ,QPushButton, QLabel, QVBoxLayout, QProgressBar , QToolBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title="Toolbox"
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
        toolbox = QToolBox()
        toolbox.setStyleSheet("background-color:green")
        vbox.addWidget(toolbox)

        label = QLabel()
        toolbox.addItem(label,"Python")

        label = QLabel()
        toolbox.addItem(label,"Java")

        label = QLabel()
        toolbox.addItem(label,"C++")


        self.setLayout(vbox)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())