from PyQt5.QtWidgets import QMainWindow,  QApplication, QLabel , QDialog, QVBoxLayout , QRadioButton , QHBoxLayout , QGroupBox, QCheckBox , QWidget , QPushButton
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title="PyQt CheckBox"
        self.top=100
        self.left=100
        self.width=400
        self.height=120
        self.iconName = "logo.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        hbox = QHBoxLayout()

        label = QLabel("Focus and Press Shift + F1")
        hbox.addWidget(label)

        button = QPushButton("Click Me ", self)
        button.setWhatsThis("This is the button you can click !!")
        hbox.addWidget(button)

        self.setLayout(hbox)
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
