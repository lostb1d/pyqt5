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

        self.groupbox = QGroupBox("Select your favorite fruit")
        self.groupbox.setFont(QtGui.QFont("Times New Roman",15))

        hbox.addWidget(self.groupbox)

        vbox = QVBoxLayout()

        rad1 = QRadioButton("Apple")
        vbox.addWidget(rad1)

        rad2 = QRadioButton("Banana")
        vbox.addWidget(rad2)

        rad3 = QRadioButton("Orange")
        vbox.addWidget(rad3)

        self.groupbox.setLayout(vbox)

        self.setLayout(hbox)




        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())