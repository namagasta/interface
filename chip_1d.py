import sys
from PyQt5 import QtGui, uic
##from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import (QDialog, QLineEdit, QSlider, QPushButton, QVBoxLayout, QApplication, QWidget)
from PyQt5.QtCore import Qt

class AppWindow(QDialog):

    ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Firing Rocket #1")

    def pressedOffButton(self):
        print ("Firing Rocket #2")

    def __init__(self):
        super().__init__()
        uic.loadUi('chip_1.ui', self)

  
        self.pushButton.clicked.connect(lambda: self.pressedOnButton())
        self.pushButton_2.clicked.connect(lambda: self.pressedOffButton())
        self.pushButton_3.clicked.connect(lambda: self.btn_clk())

        self.verticalSlider.valueChanged.connect(self.v_change)

    def v_change(self):
        my_value = str(self.vericalSlider.value())
        self.lineEdit.setText(my_value)

    def btn_clk(self, b, string):
        if b.text() == 'Print':
            print(self.lineEdit.text())
        else:
            self.lineEdit.clear()
        print(string)        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
