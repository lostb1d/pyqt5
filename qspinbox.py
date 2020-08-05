from PyQt5.QtWidgets import QApplication, QWidget , QSpinBox, QLabel, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

class Window(QWidget):
    def __init__(self):
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

        self.spinBox = QSpinBox()
        vbox.addWidget(self.spinBox)
        self.spinBox.valueChanged.connect(self.spin_changed)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        
        self.show()

    def spin_changed(self):
        getvalue = self.spinBox.value()
        self.label.setText("SpinBox Value is changed to " + str(getvalue))



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())