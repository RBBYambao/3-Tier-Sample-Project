# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SampleSignUp.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sys


class Ui_SignUp(object):
    def setupUi(self, SignUp):
        SignUp.setObjectName("SignUp")
        SignUp.resize(430, 410)
        self.SignUpCreateAccount = QtWidgets.QPushButton(SignUp)
        self.SignUpCreateAccount.setGeometry(QtCore.QRect(150, 300, 111, 28))
        self.SignUpCreateAccount.setObjectName("SignUpCreateAccount")
        self.label = QtWidgets.QLabel(SignUp)
        self.label.setGeometry(QtCore.QRect(60, 170, 71, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SignUp)
        self.label_2.setGeometry(QtCore.QRect(60, 210, 81, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(SignUp)
        self.label_3.setGeometry(QtCore.QRect(24, 250, 121, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(SignUp)
        self.label_4.setGeometry(QtCore.QRect(10, 40, 381, 91))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.SignUpUsername = QtWidgets.QLineEdit(SignUp)
        self.SignUpUsername.setGeometry(QtCore.QRect(150, 160, 241, 31))
        self.SignUpUsername.setObjectName("SignUpUsername")
        self.SignUpPassword = QtWidgets.QLineEdit(SignUp)
        self.SignUpPassword.setGeometry(QtCore.QRect(150, 200, 241, 31))
        self.SignUpPassword.setObjectName("SignUpPassword")
        self.SignUpReEnterPassword = QtWidgets.QLineEdit(SignUp)
        self.SignUpReEnterPassword.setGeometry(QtCore.QRect(150, 240, 241, 31))
        self.SignUpReEnterPassword.setObjectName("SignUpReEnterPassword")
        self.SignUpPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.SignUpReEnterPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.retranslateUi(SignUp)
        QtCore.QMetaObject.connectSlotsByName(SignUp)

    def retranslateUi(self, SignUp):
        _translate = QtCore.QCoreApplication.translate
        SignUp.setWindowTitle(_translate("SignUp", "Signing Up"))
        self.SignUpCreateAccount.setText(_translate("SignUp", "Create Account"))
        self.label.setText(_translate("SignUp", "Username :"))
        self.label_2.setText(_translate("SignUp", "Password : "))
        self.label_3.setText(_translate("SignUp", "Re-enter Password :"))
        self.label_4.setText(_translate("SignUp", "  Create Your Account Here"))
        self.SignUpCreateAccount.clicked.connect(self.signUp)
        
    def signUp(self):
        Username = self.SignUpUsername.text().strip()
        Password = self.SignUpPassword.text().strip()
        ReEnter = self.SignUpReEnterPassword.text().strip()
        
        
