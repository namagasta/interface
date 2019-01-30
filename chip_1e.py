import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication

class AppWindow(QDialog):
    ###Sliders defining    
    def v_change(self):
        my_value = str(self.horizontalSlider.value())
        self.lineEdit.setText(my_value)

    def v_change_2(self):
        my_value = str(self.verticalSlider.value())
        self.lineEdit_2.setText(my_value)        

    ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Laser Active")

    def pressedOffButton(self):
        print ("Rocket Launched")

    def __init__(self):
        super().__init__()
        uic.loadUi('chip_1.ui', self)
  
        self.pushButton.clicked.connect(lambda: self.pressedOnButton())
        self.pushButton_2.clicked.connect(lambda: self.pressedOffButton())
        self.horizontalSlider.valueChanged.connect(self.v_change)
        self.verticalSlider.valueChanged.connect(self.v_change_2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
