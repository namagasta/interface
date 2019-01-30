import os
import sys
import time

from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication

class AppWindow(QDialog):
        
    def __init__(self):
        super().__init__()
        uic.loadUi('time_1.ui', self)
        
        self.pushButton.clicked.connect(lambda: self.pressedOnButton())
        self.pushButton_2.clicked.connect(lambda: self.pressedOffButton())

    ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Pressed On!")

    def pressedOffButton(self):
        print ("Pressed Off!")


if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
