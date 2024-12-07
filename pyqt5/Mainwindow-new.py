# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow-new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Mainwindow(object):
    def setupUi(self, Mainwindow):
        Mainwindow.setObjectName("Mainwindow")
        Mainwindow.resize(1600, 1015)
        Mainwindow.setMinimumSize(QtCore.QSize(1600, 1015))
        Mainwindow.setMaximumSize(QtCore.QSize(1600, 1015))
        Mainwindow.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.frame_3 = QtWidgets.QFrame(Mainwindow)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 1600, 1015))
        self.frame_3.setMinimumSize(QtCore.QSize(1600, 1015))
        self.frame_3.setMaximumSize(QtCore.QSize(1600, 1015))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame1_2 = QtWidgets.QFrame(self.frame_3)
        self.frame1_2.setGeometry(QtCore.QRect(20, 20, 261, 950))
        self.frame1_2.setMinimumSize(QtCore.QSize(231, 950))
        self.frame1_2.setMaximumSize(QtCore.QSize(16777215, 950))
        self.frame1_2.setStyleSheet("QFrame#frame_2{\n"
"    background-color: rgba(255, 255, 255, 255);\n"
"    border-radius:20px;\n"
"}")
        self.frame1_2.setObjectName("frame1_2")
        self.frame_5 = QtWidgets.QFrame(self.frame1_2)
        self.frame_5.setGeometry(QtCore.QRect(0, 220, 251, 700))
        self.frame_5.setMinimumSize(QtCore.QSize(251, 700))
        self.frame_5.setMaximumSize(QtCore.QSize(251, 700))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.formLayout = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout.setObjectName("formLayout")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(-1, 10, -1, 18)
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(31)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_14 = QtWidgets.QWidget(self.frame_5)
        self.widget_14.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_14.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_14.setStyleSheet("image: url(:/buttom/img/buttom/背心_vest.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_14.setObjectName("widget_14")
        self.gridLayout_4.addWidget(self.widget_14, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_5.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_5.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #616161;\n"
"    color: #424242;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_6.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #616161;\n"
"    color: #424242;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 5, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_4.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #616161;\n"
"    color: #424242;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.widget_20 = QtWidgets.QWidget(self.frame_5)
        self.widget_20.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_20.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_20.setStyleSheet("image: url(:/buttom/img/buttom/处方_prescription.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_20.setObjectName("widget_20")
        self.gridLayout_4.addWidget(self.widget_20, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #616161;\n"
"    color: #424242;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 2, 1, 1, 1)
        self.widget_19 = QtWidgets.QWidget(self.frame_5)
        self.widget_19.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_19.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_19.setStyleSheet("image: url(:/buttom/img/buttom/外部传输_external-transmission.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_19.setObjectName("widget_19")
        self.gridLayout_4.addWidget(self.widget_19, 3, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_1.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_1.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #616161;\n"
"    color: #424242;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_4.addWidget(self.pushButton_1, 0, 1, 1, 1)
        self.widget_21 = QtWidgets.QWidget(self.frame_5)
        self.widget_21.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_21.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_21.setStyleSheet("image: url(:/buttom/img/buttom/眼睛_eyes.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_21.setObjectName("widget_21")
        self.gridLayout_4.addWidget(self.widget_21, 5, 0, 1, 1)
        self.widget_18 = QtWidgets.QWidget(self.frame_5)
        self.widget_18.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_18.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_18.setStyleSheet("image: url(:/buttom/img/buttom/3D眼镜_three-d-glasses.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_18.setObjectName("widget_18")
        self.gridLayout_4.addWidget(self.widget_18, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #616161;\n"
"    color: #424242;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}\n"
"font: 9pt \"微软雅黑\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.widget_13 = QtWidgets.QWidget(self.frame_5)
        self.widget_13.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_13.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_13.setStyleSheet("image: url(:/buttom/img/buttom/全景水平_panorama-horizontal.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_13.setObjectName("widget_13")
        self.gridLayout_4.addWidget(self.widget_13, 0, 0, 1, 1)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.gridLayout_4)
        self.splitter = QtWidgets.QSplitter(self.frame1_2)
        self.splitter.setGeometry(QtCore.QRect(11, 8, 241, 211))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame_6 = QtWidgets.QFrame(self.splitter)
        self.frame_6.setStyleSheet("border:none")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_8 = QtWidgets.QWidget(self.frame_6)
        self.widget_8.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_8.setMaximumSize(QtCore.QSize(100, 100))
        self.widget_8.setStyleSheet("image: url(:/svg/Morikawa/01_Data/img/image/image.png);\n"
"border-radius:45px;\n"
"background-color: rgb(223, 223, 223);")
        self.widget_8.setObjectName("widget_8")
        self.gridLayout.addWidget(self.widget_8, 0, 0, 1, 1)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(22, 54, 53)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(102, 128, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.frame = QtWidgets.QWidget(self.frame_3)
        self.frame.setGeometry(QtCore.QRect(300, 20, 1280, 950))
        self.frame.setMinimumSize(QtCore.QSize(1280, 950))
        self.frame.setMaximumSize(QtCore.QSize(1280, 950))
        self.frame.setObjectName("frame")
        self.splitter_2 = QtWidgets.QSplitter(self.frame)
        self.splitter_2.setGeometry(QtCore.QRect(0, 1, 1250, 950))
        self.splitter_2.setMinimumSize(QtCore.QSize(1250, 950))
        self.splitter_2.setMaximumSize(QtCore.QSize(1250, 16777215))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(3)
        self.gridLayout_3.setVerticalSpacing(1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(22, 54, 53)")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(22, 54, 53)")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 1, 0, 1, 1)
        self.frame11 = QtWidgets.QFrame(self.splitter_2)
        self.frame11.setMinimumSize(QtCore.QSize(1250, 880))
        self.frame11.setMaximumSize(QtCore.QSize(1250, 880))
        self.frame11.setStyleSheet(".QFrame {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.431818 rgba(157, 255, 232, 255), stop:1 rgba(203, 255, 231, 255));\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.frame11.setObjectName("frame11")

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "Form"))
        self.pushButton_5.setText(_translate("Mainwindow", "图像预处理"))
        self.pushButton_6.setText(_translate("Mainwindow", "病变诊断"))
        self.pushButton_4.setText(_translate("Mainwindow", "血管分割"))
        self.pushButton_3.setText(_translate("Mainwindow", "图像锐化"))
        self.pushButton_1.setText(_translate("Mainwindow", "灰度/二值化"))
        self.pushButton_2.setText(_translate("Mainwindow", "图像翻转"))
        self.label_3.setText(_translate("Mainwindow", "Erduo"))
        self.label_4.setText(_translate("Mainwindow", "Pro Member"))
        self.label_6.setText(_translate("Mainwindow", "<html><head/><body><p align=\"center\">欢迎使用糖尿病视网膜病变智能诊疗系统</p></body></html>"))
        self.label_7.setText(_translate("Mainwindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Welcome to the intelligent diagnosis and treatment system for diabetic retinopathy</span></p></body></html>"))

import resources_rc
