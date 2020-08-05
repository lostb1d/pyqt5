from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QDial, QMenuBar, QAction
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title="Menu"
        self.top=100
        self.left=100
        self.width=400
        self.height=120
        self.iconName = "logo.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateMenu()
        self.show()

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")


        copyAction = QAction(QIcon("img/copy.png"),"Copy",self)
        copyAction.setShortcut("Ctrl+C")
        editMenu.addAction(copyAction)

        cutAction = QAction(QIcon("img/cut.png"),"Cut",self)
        cutAction.setShortcut("Ctrl+X")
        editMenu.addAction(cutAction)

        saveAction = QAction(QIcon("img/save.png"),"Save",self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        exitAction = QAction(QIcon("img/exit.png"),"Exit",self)
        exitAction.setShortcut("Alt + F4")
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

    def exitWindow(self):
        self.close()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())