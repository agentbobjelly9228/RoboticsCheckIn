# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/alexman/python15/check in program/form.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CheckIn(object):
    def setupUi(self, CheckIn):
        CheckIn.setObjectName("CheckIn")
        CheckIn.resize(800, 600)
        CheckIn.setStyleSheet("\n"
"background-color: rgb(125, 177, 255);")
        self.label = QtWidgets.QLabel(CheckIn)
        self.label.setGeometry(QtCore.QRect(270, 40, 251, 51))
        self.label.setStyleSheet("font: 40pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")
        self.camera = QtWidgets.QPushButton(CheckIn)
        self.camera.setGeometry(QtCore.QRect(110, 250, 191, 61))
        self.camera.setStyleSheet("font: 14pt \".AppleSystemUIFont\";\n"
"selection-color: #AC8887")
        self.camera.setObjectName("camera")
        self.label_2 = QtWidgets.QLabel(CheckIn)
        self.label_2.setGeometry(QtCore.QRect(460, 210, 291, 41))
        self.label_2.setObjectName("label_2")
        self.save = QtWidgets.QPushButton(CheckIn)
        self.save.setGeometry(QtCore.QRect(310, 410, 161, 51))
        self.save.setObjectName("save")
        self.submit = QtWidgets.QPushButton(CheckIn)
        self.submit.setGeometry(QtCore.QRect(630, 260, 113, 32))
        self.submit.setObjectName("submit")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(CheckIn)
        self.plainTextEdit.setGeometry(QtCore.QRect(450, 260, 181, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")

        self.retranslateUi(CheckIn)
        QtCore.QMetaObject.connectSlotsByName(CheckIn)

    def retranslateUi(self, CheckIn):
        _translate = QtCore.QCoreApplication.translate
        CheckIn.setWindowTitle(_translate("CheckIn", "CheckIn"))
        self.label.setText(_translate("CheckIn", "Check in Here"))
        self.camera.setText(_translate("CheckIn", "Sign or out with Camera"))
        self.label_2.setText(_translate("CheckIn", "Type in Student ID if forgot to bring card"))
        self.save.setText(_translate("CheckIn", "Save to File"))
        self.submit.setText(_translate("CheckIn", "Submit"))