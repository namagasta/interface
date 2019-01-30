import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication

class AppWindow(QDialog):
        
    def btn_clk(self, b, string):
        print(b.text())
        if b.text() == 'Print':
            print(self.lineEdit.text())
        else:
            self.lineEdit.clear()
        print(string)

    def v_change(self):
        my_value = str(self.horizontalSlider.value())
        self.lineEdit.setText(my_value)

    ### functions for the buttons to call
##    def pressedOnButton(self):
##        print ("Fire Rocket 1!")
##
##    def pressedOffButton(self):
##        print ("Fire Rocket 2!")

    def __init__(self):
        super().__init__()
        uic.loadUi('slider_1.ui', self)
  
##        self.pushButton.clicked.connect(lambda: self.pressedOnButton())
##        self.pushButton_2.clicked.connect(lambda: self.pressedOffButton())
        self.pushButton.clicked.connect(lambda: self.btn_clk(self.pushButton, 'Grind'))
        self.pushButton_2.clicked.connect(lambda: self.btn_clk(self.pushButton_2, 'Axe'))
        self.horizontalSlider.valueChanged.connect(self.v_change)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
