from PyQt5.QtWidgets import QApplication, QDialog ,QPushButton, QLabel, QVBoxLayout, QProgressBar
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QThread, pyqtSignal
import time

class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        cnt =0
        while cnt<100:
            cnt+=1
            time.sleep(0.3)
            self.change_value.emit(cnt)

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title="Progress Bar"
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
        self.progressbar = QProgressBar()
        self.progressbar.setMaximum(50)
        vbox.addWidget(self.progressbar)

        self.button = QPushButton("Run Progressbar")
        self.button.clicked.connect(self.startProgressBar)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def startProgressBar(self):
        self.thread = MyThread()
        self.thread.change_value.connect(self.setProgressval)
        self.thread.start()

    def setProgressval(self, val):
        self.progressbar.setValue(val)
        
    

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())