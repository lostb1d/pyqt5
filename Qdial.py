from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QLabel, QVBoxLayout, QDial
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self, val):
        super().__init__()

        self.title="QDial"
        self.top=100
        self.left=100
        self.width=400
        self.height=120
        self.iconName = "logo.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        vbox = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Elephant",10))

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(30)
        self.dial.valueChanged.connect(self.dial_change)

        vbox.addWidget(self.dial)
        vbox.addWidget(self.label)
        self.setLayout(vbox)
        
        self.show()

    def dial_change(self):
        getvalue = self.dial.value()
        self.label.setText("Dial is changed to " + str(getvalue))



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())