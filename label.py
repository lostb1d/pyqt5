from PyQt5.QtWidgets import QMainWindow,  QApplication, QLabel , QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap

class Window(QDialog):
    def  __init__(self):
        super().__init__()
        self.title="Learning PyQt5"
        self.top=100
        self.left=100
        self.width=400
        self.height=300
        self.iconName = "logo.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        label = QLabel("This is a lable")
        vbox.addWidget(label)

        label2 = QLabel("This is another label")
        label2.setFont(QtGui.QFont("Sanserif",20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("logo_with_text.png")
        labelImage.setPixmap(pixmap)

        vbox.addWidget(labelImage)



        self.setLayout(vbox)

        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
