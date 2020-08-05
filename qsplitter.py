from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget , QFrame , QHBoxLayout, QSplitter , QLineEdit
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
        left = QFrame()
        left.setFrameShape(QFrame.StyledPanel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.StyledPanel)

        splitter1 = QSplitter(Qt.Horizontal)
        
        lineedit1 = QLineEdit()
        splitter1.addWidget(left)
        splitter1.addWidget(lineedit1)
        splitter1.setSizes([200,200])

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)

        self.setLayout(hbox)


        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())