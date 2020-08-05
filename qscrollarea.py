from PyQt5.QtWidgets import QApplication,QScrollArea, QVBoxLayout, QPushButton, QWidget, QFormLayout, QFormLayout, QLabel, QGroupBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self, val):
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
        
        formLayout = QFormLayout()
        groupBox = QGroupBox("This is a group Box")

        labelList= []
        buttonList = []

        for i in range(val):
            labelList.append(QLabel("Label"))
            buttonList.append(QPushButton("Click Me"))
            formLayout.addRow(labelList[i], buttonList[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)

        layout =  QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)


        self.show()



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())