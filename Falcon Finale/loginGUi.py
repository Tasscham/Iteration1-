# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import intGraphGUi 
import OtherWindow
#import sys



var=False
class Ui_Dialog(object):
    def openWindow(self):
        if str(self.pass_lineEdit.text()) == 'falcon' and  str(self.uname_lineEdit.text()) == 'falcon2018' :
            self.window = QtWidgets.QMainWindow()
            self.ui =intGraphGUi.Ui_Form()
            self.ui.setupUi(self.window)
            Dialog.hide()
            self.window.show()
        else :
            self.window = QtWidgets.QMainWindow()
            self.ui =OtherWindow.Ui_OtherWindow()
            self.ui.setupUi(self.window)
            #Dialog.hide()
            self.window.show()
            
       

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon("falcon.png"))
        Dialog.resize(506, 274)
        Dialog.setStyleSheet("QWidget { background-color: rgb(20, 18, 39);border-color: rgb(237, 255, 66); }")
        #Dialog.setStyleSheet(" { font: italic 14pt Georgia } ")
        #Dialog.setStyleSheet("{ background-color: rgb(99, 180, 255)}")
                             #;border-color: rgb(237, 255, 66);font: italic 14pt 'Georgia';background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0.482412 rgba(0, 170, 255, 255), stop:1 rgba(255, 255, 255, 255));gridline-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0 rgba(255, 255, 0, 69), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(251, 255, 0, 145), stop:0.45 rgba(247, 255, 0, 208), stop:0.477581 rgba(255, 244, 71, 130), stop:0.518717 rgba(255, 218, 71, 130), stop:0.55 rgba(255, 255, 0, 255), stop:0.57754 rgba(255, 203, 0, 130), stop:0.625 rgba(255, 255, 0, 69), stop:1 rgba(255, 255, 0, 69));}")
        self.u_name_label = QtWidgets.QLabel(Dialog)
        self.u_name_label.setGeometry(QtCore.QRect(150, 110, 71, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(60)
        self.u_name_label.setFont(font)
        self.u_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.u_name_label.setObjectName("u_name_label")
        self.u_name_label.setStyleSheet("color: rgb(255,255,255);")
        self.pass_label = QtWidgets.QLabel(Dialog)
        self.pass_label.setGeometry(QtCore.QRect(150, 150, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pass_label.setFont(font)
        self.pass_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pass_label.setObjectName("pass_label")
        self.pass_label.setStyleSheet("color: rgb(255,255,255);")
        self.uname_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.uname_lineEdit.setGeometry(QtCore.QRect(230, 110, 113, 20))
        self.uname_lineEdit.setObjectName("uname_lineEdit")
        self.uname_lineEdit.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.pass_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.pass_lineEdit.setGeometry(QtCore.QRect(230, 150, 113, 20))
        self.pass_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.pass_lineEdit.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.login_btn = QtWidgets.QPushButton(Dialog)
        self.login_btn.setGeometry(QtCore.QRect(250, 200, 80, 23))
        self.login_btn.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.login_btn.setObjectName("login_btn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(170, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
       
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.login_btn.clicked.connect(self.openWindow)
        
    
   


      
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "FALCON TUNISIA"))
        self.u_name_label.setText(_translate("Dialog", "USERNAME "))
        self.pass_label.setText(_translate("Dialog", "PASSWORD"))
        self.login_btn.setText(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "FALCON TUNISIA"))
        self.label.setStyleSheet("color: rgb(255,255,255);")
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    
    sys.exit(app.exec_())

