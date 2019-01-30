##import sys
from PyQt5 import QtGui, uic
##from PyQt5.QtWidgets import QDialog, QApplication

import os
import sys
import time

#from PyQt5.uic import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class AppWindow(QDialog):
        
    def __init__(self):
        super().__init__()
        uic.loadUi('chip_1.ui', self)

        self.available_cameras = QCameraInfo.availableCameras()
        if not self.available_cameras:
            pass #quit

##        self.status = QStatusBar()
##        self.setStatusBar(self.status)


##        self.save_path = ""

        self.viewfinder = QCameraViewfinder()
#        self.viewfinder.show()
#        self.graphicsView(self.viewfinder)

        # Set the default camera.
        self.select_camera(0)

    ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Pressed On!")

    def pressedOffButton(self):
        print ("Pressed Off!")

    def select_camera(self, i):
        self.camera = QCamera(self.available_cameras[i])
        self.camera.setViewfinder(self.viewfinder)
        self.camera.setCaptureMode(QCamera.CaptureStillImage)
        self.camera.error.connect(lambda: self.alert(self.camera.errorString()))
        self.camera.start()

        self.capture = QCameraImageCapture(self.camera)
        self.capture.error.connect(lambda i, e, s: self.alert(s))
        self.capture.imageCaptured.connect(lambda d, i: self.status.showMessage("Image %04d captured" % self.save_seq))

        self.current_camera_name = self.available_cameras[i].description()
        self.save_seq = 0
        
        self.pushButton.clicked.connect(lambda: self.pressedOnButton())
        self.pushButton_2.clicked.connect(lambda: self.pressedOffButton())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())
