import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication
#from trial2 import Ui_Dialog

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
##        self.ui = Ui_Dialog()
##        self.ui.setupUi(self)
        uic.loadUi('trial2.ui', self)
        self.show()  

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
