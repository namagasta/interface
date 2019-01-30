# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chip_1.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_chip_4(object):
    def setupUi(self, chip_4):
        chip_4.setObjectName("chip_4")
        chip_4.resize(879, 800)
        self.buttonBox = QtWidgets.QDialogButtonBox(chip_4)
        self.buttonBox.setGeometry(QtCore.QRect(650, 760, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalSlider = QtWidgets.QSlider(chip_4)
        self.horizontalSlider.setGeometry(QtCore.QRect(100, 710, 701, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(chip_4)
        self.verticalSlider.setGeometry(QtCore.QRect(40, 50, 22, 621))
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.graphicsView = QtWidgets.QGraphicsView(chip_4)
        self.graphicsView.setEnabled(True)
        self.graphicsView.setGeometry(QtCore.QRect(100, 50, 731, 611))
        self.graphicsView.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(chip_4)
        self.label.setGeometry(QtCore.QRect(90, 740, 71, 16))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(chip_4)
        self.label_2.setGeometry(QtCore.QRect(20, 680, 61, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(chip_4)
        self.textBrowser.setGeometry(QtCore.QRect(95, 760, 61, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(chip_4)
        self.pushButton.setGeometry(QtCore.QRect(360, 740, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(chip_4)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 740, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(chip_4)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 700, 61, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")

        self.retranslateUi(chip_4)
        self.buttonBox.accepted.connect(chip_4.accept)
        self.buttonBox.rejected.connect(chip_4.reject)
        QtCore.QMetaObject.connectSlotsByName(chip_4)

    def retranslateUi(self, chip_4):
        _translate = QtCore.QCoreApplication.translate
        chip_4.setWindowTitle(_translate("chip_4", "Dialog"))
        self.label.setText(_translate("chip_4", "Left & Right"))
        self.label_2.setText(_translate("chip_4", "Up & Down"))
        self.pushButton.setText(_translate("chip_4", "Rocket #1"))
        self.pushButton_2.setText(_translate("chip_4", "Rocket #2"))

