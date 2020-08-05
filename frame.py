from PyQt5.QtWidgets import QApplication, QWidget, QSizeGrip , QVBoxLayout , QFrame, QHBoxLayout , QPushButton
import sys
from PyQt5 import QtGui , QtCore


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
        self.setStyleSheet('background-color:yellow')

        hbox = QHBoxLayout()

        btn = QPushButton("Click Ok")
        btn.setStyleSheet("color:white; background-color:black")
        
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(0.6)
        frame.setStyleSheet("background-color:red")

        hbox.addWidget(frame)
        hbox.addWidget(btn)
        
        self.setLayout(hbox)
       
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())