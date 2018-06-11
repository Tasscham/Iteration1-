# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intFinal1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import cv2
import datetime

import Base
import matplotlib.pyplot as plt
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowIcon(QtGui.QIcon("falcon.png"))
        Form.resize(815, 593)
        Form.setStyleSheet("background-color: rgb(20, 18, 39);")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(180, 50, 411, 171))
        self.calendarWidget.setStyleSheet("alternate-background-color: rgb(204, 204, 204);\n"
        "background-color: rgb(177, 177, 177);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.labelImg = QtWidgets.QLabel(Form)
        self.labelImg.setGeometry(QtCore.QRect(0, 0, 81, 91))
        self.labelImg.setText("")
        self.labelImg.setPixmap(QtGui.QPixmap("test.png"))
        self.labelImg.setObjectName("labelImg")
        self.showCam = QtWidgets.QToolButton(Form)
        self.showCam.setGeometry(QtCore.QRect(630, 80, 171, 41))
        self.showCam.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.showCam.setObjectName("showCam")
        self.showStat = QtWidgets.QPushButton(Form)
        self.showStat.setGeometry(QtCore.QRect(20, 350, 101, 41))
        self.showStat.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.showStat.setObjectName("showStat")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 260, 431, 281))
        self.label_3.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.label_3.setText("")
        #self.label_3.setPixmap(QtGui.QPixmap("Figure.png"))
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setGeometry(QtCore.QRect(630, 170, 171, 41))
        self.toolButton.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.toolButton.setObjectName("toolButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.showStat.clicked.connect(self.affStat)
        self.showCam.clicked.connect(self.affCam)
        self.toolButton.clicked.connect(self.on_click)
    def affStat(self):
         #x1 = np.linspace(l1[0], l1[len(l1)-1])
         #x2 = np.linspace(l2[0], l2[len(l1)-1])
         #y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
        # plt.subplot(2, 1, 1)
         #plt.plot(x1, y1, 'o-')
         cur=Base.selection()
         l1=[]
         l2=[]
         for i in cur:
             l1.append(i[0])
             l2.append(i[1])
         plt.plot(l2, l1,"g",linewidth=0.8,marker="*")
        # plt.figure('Statistique')
         plt.xlabel('Temps')
         plt.ylabel('Nb Face')
         f=plt.gcf()
         f.savefig('Figure.png')
         plt.show()
         self.label_3.setPixmap(QtGui.QPixmap("Figure.png"))
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "FALCON TUNISIA"))
        self.showCam.setText(_translate("Form", "Show camera Manual Mode"))
        self.showStat.setText(_translate("Form", "Show Statistics"))
        self.toolButton.setText(_translate("Form", "Show camera Autoamtic Mode"))

    def on_click(self):
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        #eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        count=0;
        nb=0;
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            # Our operations on the frame come here
            # #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            date = datetime.datetime.now()
            cv2.putText(frame, str(date),(370,470), cv2.FONT_ITALIC, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, "By FALCON TUNISIA",(15,470), cv2.FONT_ITALIC, 0.5,(255,255,255),1,cv2.LINE_AA)
            for (x,y,w,h) in faces:
                count=len(faces)
                if nb!=count:
                    nb=count
                    dt=datetime.datetime.now().strftime('%H:%M:%S')
                    Base.insertion(count,dt)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),5)
                #roi_gray = frame[y:y+h, x:x+w]
                #roi_color = frame[y:y+h, x:x+w]
                ##eyes = eye_cascade.detectMultiScale(roi_gray)
                #for (ex,ey,ew,eh) in eyes:
                    #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        # Display the resulting frame
            cv2.putText(frame, str(count),(300,60), cv2.FONT_ITALIC, 2,(255,0,0),2,cv2.LINE_AA)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        #self.statusBar().showMessage('Hello world'
    def affCam(self):
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        #eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        count=0;
        nb=0;
        while(True):
            # Capture frame-by-frame
            ret, frame = cap.read()
            # Our operations on the frame come here
            # #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(frame, 1.3, 5)
            date = datetime.datetime.now()
            cv2.putText(frame, str(date),(370,470), cv2.FONT_ITALIC, 0.5,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame, "By FALCON TUNISIA",(15,470), cv2.FONT_ITALIC, 0.5,(255,255,255),1,cv2.LINE_AA)
            for (x,y,w,h) in faces:
                count=len(faces)
                if nb!=count:
                    nb=count
                    dt=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    Base.insertion(count,dt)
                    #cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
                    #roi_gray = frame[y:y+h, x:x+w]
                    #roi_color = frame[y:y+h, x:x+w]
                    ##eyes = eye_cascade.detectMultiScale(roi_gray)
                    #for (ex,ey,ew,eh) in eyes:
                    #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    # Display the resulting frame
            cv2.putText(frame, str(count),(300,60), cv2.FONT_ITALIC, 2,(255,0,0),2,cv2.LINE_AA)
            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

