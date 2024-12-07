# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fromwin8.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formwin8(object):
    def setupUi(self, Formwin8):
        Formwin8.setObjectName("Formwin8")
        Formwin8.resize(1100, 800)
        Formwin8.setMinimumSize(QtCore.QSize(1100, 700))
        self.layoutWidget = QtWidgets.QWidget(Formwin8)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 60, 1008, 311))
        self.layoutWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_load = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_load.setMinimumSize(QtCore.QSize(400, 50))
        self.pushButton_load.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_load.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_load.setObjectName("pushButton_load")
        self.gridLayout.addWidget(self.pushButton_load, 1, 0, 1, 1)
        self.label_jieguo = QtWidgets.QLabel(self.layoutWidget)
        self.label_jieguo.setMinimumSize(QtCore.QSize(500, 0))
        self.label_jieguo.setStyleSheet("")
        self.label_jieguo.setObjectName("label_jieguo")
        self.gridLayout.addWidget(self.label_jieguo, 0, 1, 1, 1)
        self.label_daichuli = QtWidgets.QLabel(self.layoutWidget)
        self.label_daichuli.setMinimumSize(QtCore.QSize(500, 0))
        self.label_daichuli.setStyleSheet("")
        self.label_daichuli.setObjectName("label_daichuli")
        self.gridLayout.addWidget(self.label_daichuli, 0, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(400, 50))
        self.pushButton_save.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(Formwin8)
        self.layoutWidget1.setGeometry(QtCore.QRect(220, 400, 661, 111))
        self.layoutWidget1.setMinimumSize(QtCore.QSize(80, 50))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_yd = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_yd.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_yd.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:30px;")
        self.pushButton_yd.setObjectName("pushButton_yd")
        self.horizontalLayout.addWidget(self.pushButton_yd)
        self.pushButton_sj = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_sj.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_sj.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:30px;")
        self.pushButton_sj.setObjectName("pushButton_sj")
        self.horizontalLayout.addWidget(self.pushButton_sj)
        self.pushButton_pinpu = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_pinpu.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_pinpu.setStyleSheet("background-color: rgb(255, 255, 255);border-radius:30px;")
        self.pushButton_pinpu.setObjectName("pushButton_pinpu")
        self.horizontalLayout.addWidget(self.pushButton_pinpu)

        self.retranslateUi(Formwin8)
        QtCore.QMetaObject.connectSlotsByName(Formwin8)

    def retranslateUi(self, Formwin8):
        _translate = QtCore.QCoreApplication.translate
        Formwin8.setWindowTitle(_translate("Formwin8", "Form"))
        self.pushButton_load.setText(_translate("Formwin8", "选择图片"))
        self.label_jieguo.setText(_translate("Formwin8", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">结果</span></p></body></html>"))
        self.label_daichuli.setText(_translate("Formwin8", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">待处理</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Formwin8", "保存图片"))
        self.pushButton_yd.setText(_translate("Formwin8", "运动模糊"))
        self.pushButton_sj.setText(_translate("Formwin8", "散焦模糊"))
        self.pushButton_pinpu.setText(_translate("Formwin8", "频谱图"))

