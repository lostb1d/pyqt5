from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget , QFrame , QHBoxLayout, QSplitter , QLineEdit , QSlider, QLabel
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title="Frame Window"
        self.top=100
        self.left=100
        self.width=400
        self.height=120
        self.iconName = "logo.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        hbox = QHBoxLayout()

        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.changeValue)

        self.label = QLabel("0")
        self.label.setFont(QtGui.QFont("Sanserif",15))

        self.label2 = QLabel("Volume")
        self.label2.setFont(QtGui.QFont("Algerian",15))
        
        hbox.addWidget(self.label2)
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()

    def changeValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())