# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fromwin6.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formwin6(object):
    def setupUi(self, Formwin6):
        Formwin6.setObjectName("Formwin6")
        Formwin6.resize(1100, 700)
        Formwin6.setMinimumSize(QtCore.QSize(1100, 700))
        Formwin6.setMaximumSize(QtCore.QSize(1100, 700))
        self.splitter = QtWidgets.QSplitter(Formwin6)
        self.splitter.setGeometry(QtCore.QRect(2, 1, 1101, 711))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_load = QtWidgets.QPushButton(self.widget)
        self.pushButton_load.setMinimumSize(QtCore.QSize(400, 60))
        self.pushButton_load.setMaximumSize(QtCore.QSize(400, 60))
        self.pushButton_load.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 30px;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    box-shadow: 0 0 20px #eee;\n"
"    display: block;\n"
"    margin: 10px;\n"
"    color: white; /* 文字颜色为白色 */\n"
"    transition: box-shadow 0.5s, background-position 0.5s, border-color 0.5s; /* 添加过渡效果 */\n"
"    background-size: 200% auto;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 14px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-position: 100% 0; /* 改变背景位置以实现渐变的滑动效果 */\n"
"    border-color: #2c3e50; /* 悬浮时边框颜色调整为渐变的中间颜色 */\n"
"    color: white; /* 鼠标悬浮时保持文字颜色为白色 */\n"
"    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* 增加悬浮阴影效果 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    /* 按下和选中时，你可以选择保持渐变效果或设置不同的样式 */\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #2c3e50, stop:1 #bdc3c7); /* 示例：反转渐变的方向 */\n"
"    color: white; /* 按下时保持文字颜色为白色 */\n"
"    border-color: #2c3e50; /* 按下时边框颜色调整为渐变的深色 */\n"
"}\n"
"")
        self.pushButton_load.setObjectName("pushButton_load")
        self.gridLayout_3.addWidget(self.pushButton_load, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_classical = QtWidgets.QPushButton(self.frame)
        self.pushButton_classical.setMinimumSize(QtCore.QSize(150, 50))
        self.pushButton_classical.setMaximumSize(QtCore.QSize(150, 50))
        self.pushButton_classical.setAcceptDrops(False)
        self.pushButton_classical.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_classical.setStyleSheet("\n"
"QPushButton {\n"
"    background-color:#ef4565 ; /* 深青色背景 */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #ef4565; /* 边框颜色与背景色一致 */\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    transition: box-shadow 0.5s;\n"
"    box-shadow: 0 0 20px #eee;\n"
"    display: block;\n"
"    margin: 5px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 14px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:#ef4565;\n"
"    background-color: #fffffe; /* 悬浮时改为更深的颜色 */\n"
"    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* 增加悬浮阴影效果 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background-color: #fffffe; /* 按下时使用更深的颜色 */\n"
"    border: 1px solid #5f6c7b; /* 按下时边框颜色调整为更深 */\n"
"    color: #ef4565; /* 维持字体颜色为白色 */\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px; /* 特定按钮的圆角 */\n"
"}\n"
"")
        self.pushButton_classical.setAutoDefault(False)
        self.pushButton_classical.setDefault(False)
        self.pushButton_classical.setFlat(False)
        self.pushButton_classical.setObjectName("pushButton_classical")
        self.gridLayout.addWidget(self.pushButton_classical, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)
        self.label_daichuli = QtWidgets.QLabel(self.widget)
        self.label_daichuli.setMinimumSize(QtCore.QSize(400, 400))
        self.label_daichuli.setMaximumSize(QtCore.QSize(400, 400))
        self.label_daichuli.setStyleSheet("")
        self.label_daichuli.setAlignment(QtCore.Qt.AlignCenter)
        self.label_daichuli.setObjectName("label_daichuli")
        self.gridLayout_3.addWidget(self.label_daichuli, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(60, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(150, 40))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 4, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(150, 40))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 6, 0, 1, 1)
        self.lineEdit_0 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_0.setMinimumSize(QtCore.QSize(150, 40))
        self.lineEdit_0.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_0.setFont(font)
        self.lineEdit_0.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_0.setObjectName("lineEdit_0")
        self.gridLayout_2.addWidget(self.lineEdit_0, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_1.setMinimumSize(QtCore.QSize(150, 40))
        self.lineEdit_1.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout_2.addWidget(self.lineEdit_1, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(150, 40))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(150, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(150, 50))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Formwin6)
        QtCore.QMetaObject.connectSlotsByName(Formwin6)

    def retranslateUi(self, Formwin6):
        _translate = QtCore.QCoreApplication.translate
        Formwin6.setWindowTitle(_translate("Formwin6", "Form"))
        self.pushButton_load.setText(_translate("Formwin6", "选 择 图 片"))
        self.pushButton_classical.setText(_translate("Formwin6", "病变诊断"))
        self.label_daichuli.setText(_translate("Formwin6", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">待处理</span></p></body></html>"))
        self.lineEdit_2.setText(_translate("Formwin6", "2-Moderate"))
        self.lineEdit_4.setText(_translate("Formwin6", "4-Proliferative DR"))
        self.lineEdit_0.setWhatsThis(_translate("Formwin6", "<html><head/><body><p align=\"center\"><br/>0-No DR</p></body></html>"))
        self.lineEdit_0.setText(_translate("Formwin6", "0-No DR"))
        self.lineEdit_1.setText(_translate("Formwin6", "1-Mild"))
        self.lineEdit_3.setText(_translate("Formwin6", "3-Severe"))
        self.label.setText(_translate("Formwin6", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">诊断结果</span></p></body></html>"))

import resources_rc
