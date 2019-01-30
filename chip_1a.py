import sys
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QDialog, QApplication

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('chip_1.ui', self)
        self.show()  

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
