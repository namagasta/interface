#from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
    
#import RPi.GPIO as GPIO
import time      
import re
from PyQt5 import QtGui, uic, QtCore
from PyQt5.QtCore import QTimer
#from PyQt5.QtGui import QApplication

##class AppWindow(QtWidgets.QMainWindow):
##    def __init__(self):
##        super(AppWindow,self).__init__()
##        uic.loadUi('trial.ui', self)  

class AppWindow(QtGui.QMainWindow): #Class to bind ledonoff.ui with Python             Script do not change anything here
    def __init__(self):
        super(MyWindow, self).__init__()
        uic.loadUi('trial.ui', self)
        self.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
