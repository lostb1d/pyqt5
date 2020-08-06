from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QVBoxLayout, QDial, QMenuBar, QAction, QToolBar , QTextEdit, QFontDialog, QColorDialog
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt 

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title="Text Edit"
        self.top=100
        self.left=100
        self.width=400
        self.height=120
        self.iconName = "logo.png"

        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.CreateMenu()
        self.createEditor()
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

        pasteAction = QAction(QIcon("img/paste.png"),"Paste",self)
        pasteAction.setShortcut("Ctrl+V")
        editMenu.addAction(pasteAction)

        fontAction = QAction(QIcon("img/font.png"),"Font",self)
        fontAction.setShortcut("Ctrl + F")
        fontAction.triggered.connect(self.fontDialof)
        viewMenu.addAction(fontAction)

        colorAction = QAction(QIcon("img/color.png"),"Font Color", self)
        colorAction.triggered.connect(self.colorDialog)
        viewMenu.addAction(colorAction)

        saveAction = QAction(QIcon("img/save.png"),"Save",self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)

        exitAction = QAction(QIcon("img/exit.png"),"Exit",self)
        exitAction.setShortcut("Alt + F4")
        exitAction.triggered.connect(self.exitWindow)
        fileMenu.addAction(exitAction)

        toolbar = self.addToolBar("Toolbar")
        toolbar.addAction(copyAction)
        toolbar.addAction(cutAction)
        toolbar.addAction(pasteAction)
        toolbar.addAction(saveAction)
        toolbar.addAction(exitAction)
        toolbar.addAction(fontAction)
        toolbar.addAction(colorAction)
        


    def exitWindow(self):
        self.close()

    def createEditor(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

    def fontDialof(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.textEdit.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())