from PyQt5.QtWidgets import QMainWindow,  QApplication, QLabel , QDialog, QVBoxLayout , QRadioButton , QHBoxLayout , QGroupBox, QCheckBox , QWidget , QPushButton, QLineEdit
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
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Algerian",14))
        hbox.addWidget(self.lineedit)

        self.label = QLabel("Hello ")
        self.label.setFont(QtGui.QFont("Algerian",14))
        self.lineedit.returnPressed.connect(self.onPressed)
        hbox.addWidget(self.label)
        self.setLayout(hbox)

        self.show()

    def onPressed(self):
        self.label.setText(self.lineedit.text())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())