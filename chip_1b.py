import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication

class AppWindow(QDialog):
        


    ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Pressed On!")

    def pressedOffButton(self):
        print ("Pressed Off!")

    def __init__(self):
        super().__init__()
        uic.loadUi('chip_1.ui', self)
  
        self.pushButton.clicked.connect(lambda: self.pressedOnButton())
        self.pushButton_2.clicked.connect(lambda: self.pressedOffButton())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
