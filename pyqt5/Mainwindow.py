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
        self.widget = QtWidgets.QWidget(self.frame_3)
        self.widget.setGeometry(QtCore.QRect(5, 5, 1588, 1002))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame1_2 = QtWidgets.QFrame(self.widget)
        self.frame1_2.setMinimumSize(QtCore.QSize(300, 950))
        self.frame1_2.setMaximumSize(QtCore.QSize(300, 950))
        self.frame1_2.setStyleSheet("QFrame#frame_2{\n"
"    background-color: rgba(255, 255, 255, 255);\n"
"    border-radius:20px;\n"
"}")
        self.frame1_2.setObjectName("frame1_2")
        self.frame_5 = QtWidgets.QFrame(self.frame1_2)
        self.frame_5.setGeometry(QtCore.QRect(0, 220, 300, 800))
        self.frame_5.setMinimumSize(QtCore.QSize(300, 800))
        self.frame_5.setMaximumSize(QtCore.QSize(300, 800))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.widget1 = QtWidgets.QWidget(self.frame_5)
        self.widget1.setGeometry(QtCore.QRect(5, 9, 291, 721))
        self.widget1.setObjectName("widget1")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_14 = QtWidgets.QWidget(self.widget1)
        self.widget_14.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_14.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_14.setStyleSheet("image: url(:/buttom/img/buttom/背心_vest.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_14.setObjectName("widget_14")
        self.gridLayout_4.addWidget(self.widget_14, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_5.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"color:#334257;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 4, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_6.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton_6.setMaximumSize(QtCore.QSize(300, 16777215))
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"color:#334257;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 5, 1, 1, 1)
#         self.pushButton_4 = QtWidgets.QPushButton(self.widget1)
#         self.pushButton_4.setMinimumSize(QtCore.QSize(150, 80))
#         self.pushButton_4.setMaximumSize(QtCore.QSize(150, 16777215))
#         self.pushButton_4.setStyleSheet("QPushButton {\n"
# "    background-color: #fafafa;\n"
# "color:#334257;\n"
# "    border: 1px solid #cccccc;\n"
# "    padding: 5px;\n"
# "    border-radius: 5px;\n"
# "    font-family: \"Arial\"; /* 添加字体族 */\n"
# "    font-size: 24px; /* 添加字体大小 */\n"
# "    font-weight: bold; /* 添加字体粗细 */\n"
# "    font-style: normal; /* 添加字体风格 */\n"
# "}\n"
# "\n"
# "QPushButton:hover {\n"
# "    background-color: #f5f5f5;\n"
# "    \n"
# "}\n"
# "\n"
# "QPushButton:pressed, QPushButton:checked {\n"
# "    border: 1px solid #616161;\n"
# "    color: #424242;\n"
# "}\n"
# "\n"
# "#button3 {\n"
# "    border-radius: 20px;\n"
# "}\n"
# "font: 9pt \"微软雅黑\";\n"
# "")
#         self.pushButton_4.setObjectName("pushButton_4")
#         self.gridLayout_4.addWidget(self.pushButton_4, 3, 1, 1, 1)
        self.widget_20 = QtWidgets.QWidget(self.widget1)
        self.widget_20.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_20.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_20.setStyleSheet("image: url(:/buttom/img/buttom/处方_prescription.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_20.setObjectName("widget_20")
        self.gridLayout_4.addWidget(self.widget_20, 2, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton_3.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"color:#334257;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
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
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 2, 1, 1, 1)
#         self.widget_19 = QtWidgets.QWidget(self.widget1)
#         self.widget_19.setMinimumSize(QtCore.QSize(40, 40))
#         self.widget_19.setMaximumSize(QtCore.QSize(40, 40))
#         self.widget_19.setStyleSheet("image: url(:/buttom/img/buttom/外部传输_external-transmission.svg);\n"
# "border:3px solid rgb(255, 255, 255);\n"
# "\n"
# "border-radius:32px")
#         self.widget_19.setObjectName("widget_19")
#         self.gridLayout_4.addWidget(self.widget_19, 3, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_1.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton_1.setMaximumSize(QtCore.QSize(150, 80))
        self.pushButton_1.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    color:#334257;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #616161;\n"
"    color: #334257;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}\n"
"font: 9pt \"微软雅黑\";\n"
"")
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_4.addWidget(self.pushButton_1, 0, 1, 1, 1)
        self.widget_21 = QtWidgets.QWidget(self.widget1)
        self.widget_21.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_21.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_21.setStyleSheet("image: url(:/buttom/img/buttom/眼睛_eyes.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_21.setObjectName("widget_21")
        self.gridLayout_4.addWidget(self.widget_21, 5, 0, 1, 1)
        self.widget_18 = QtWidgets.QWidget(self.widget1)
        self.widget_18.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_18.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_18.setStyleSheet("image: url(:/buttom/img/buttom/3D眼镜_three-d-glasses.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_18.setObjectName("widget_18")
        self.gridLayout_4.addWidget(self.widget_18, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    color:#334257;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    \n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    border: 1px solid #616161;\n"
"    color: #334257;\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px;\n"
"}\n"
"font: 9pt \"微软雅黑\";\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.widget_13 = QtWidgets.QWidget(self.widget1)
        self.widget_13.setMinimumSize(QtCore.QSize(40, 40))
        self.widget_13.setMaximumSize(QtCore.QSize(40, 40))
        self.widget_13.setStyleSheet("image: url(:/buttom/img/buttom/全景水平_panorama-horizontal.svg);\n"
"border:3px solid rgb(255, 255, 255);\n"
"\n"
"border-radius:32px")
        self.widget_13.setObjectName("widget_13")
        self.gridLayout_4.addWidget(self.widget_13, 0, 0, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.frame1_2)
        self.splitter.setGeometry(QtCore.QRect(11, 8, 281, 211))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.frame_6 = QtWidgets.QFrame(self.splitter)
        self.frame_6.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_6.setStyleSheet("border:none")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_8 = QtWidgets.QWidget(self.frame_6)
        self.widget_8.setMinimumSize(QtCore.QSize(100, 100))
        self.widget_8.setMaximumSize(QtCore.QSize(100, 100))
        self.widget_8.setStyleSheet("image: url(logo.png);\n"
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
        self.label_3.setMinimumSize(QtCore.QSize(300, 0))
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
        self.label_4.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(102, 128, 127);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.horizontalLayout.addWidget(self.frame1_2)
        self.frame = QtWidgets.QWidget(self.widget)
        self.frame.setMinimumSize(QtCore.QSize(1280, 1000))
        self.frame.setMaximumSize(QtCore.QSize(1280, 1000))
        self.frame.setObjectName("frame")
        self.widget2 = QtWidgets.QWidget(self.frame)
        self.widget2.setGeometry(QtCore.QRect(0, 11, 1252, 981))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(22, 54, 53)")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setFamily("Bodoni MT")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(22, 54, 53)")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.frame11 = QtWidgets.QFrame(self.widget2)
        self.frame11.setMinimumSize(QtCore.QSize(1250, 880))
        self.frame11.setMaximumSize(QtCore.QSize(1250, 880))
        self.frame11.setStyleSheet(".QFrame {\n"
"    background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #009695, stop:0.33 #71b9b7, stop:0.66 #b5dcda, stop:1 #f7ffff);\n"
";\n"
"    border-radius: 20px;\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.frame11.setObjectName("frame11")
        self.verticalLayout.addWidget(self.frame11)
        self.horizontalLayout.addWidget(self.frame)

        self.retranslateUi(Mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Mainwindow)

    def retranslateUi(self, Mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Mainwindow.setWindowTitle(_translate("Mainwindow", "Form"))
        self.pushButton_5.setText(_translate("Mainwindow", "图像预处理"))
        self.pushButton_6.setText(_translate("Mainwindow", "病变诊断"))
        # self.pushButton_4.setText(_translate("Mainwindow", "血管分割"))
        self.pushButton_3.setText(_translate("Mainwindow", "图像锐化"))
        self.pushButton_1.setText(_translate("Mainwindow", "灰度/二值化"))
        self.pushButton_2.setText(_translate("Mainwindow", "图像翻转"))
        self.label_3.setText(_translate("Mainwindow", "Gwansy"))
        self.label_4.setText(_translate("Mainwindow", "Pro Member"))
        self.label_6.setText(_translate("Mainwindow", "<html><head/><body><p align=\"center\">欢迎使用糖尿病视网膜病变智能诊疗系统</p></body></html>"))
        self.label_7.setText(_translate("Mainwindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:9pt;\">Welcome to the intelligent diagnosis and treatment system for diabetic retinopathy</span></p></body></html>"))


import resources_rc
class Ui_Formwin1(object):
    def setupUi(self, Formwin1):
        Formwin1.setObjectName("Formwin1")
        Formwin1.resize(1100, 700)
        Formwin1.setMinimumSize(QtCore.QSize(1250, 880))
        Formwin1.setMaximumSize(QtCore.QSize(1250, 880))
        self.layoutWidget = QtWidgets.QWidget(Formwin1)
        self.layoutWidget.setGeometry(QtCore.QRect(85, 180, 1100, 700))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_load = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_load.setMinimumSize(QtCore.QSize(400, 50))
        self.pushButton_load.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.gridLayout.addWidget(self.pushButton_load, 1, 0, 1, 1)
        self.label_jieguo = QtWidgets.QLabel(self.layoutWidget)
        self.label_jieguo.setMinimumSize(QtCore.QSize(350, 350))
        self.label_jieguo.setMaximumSize(QtCore.QSize(350, 350))
        self.label_jieguo.setObjectName("label_jieguo")
        self.gridLayout.addWidget(self.label_jieguo, 0, 1, 1, 1)
        self.label_daichuli = QtWidgets.QLabel(self.layoutWidget)
        self.label_daichuli.setMinimumSize(QtCore.QSize(350, 350))
        self.label_daichuli.setMaximumSize(QtCore.QSize(350, 350))
        self.label_daichuli.setObjectName("label_daichuli")
        self.gridLayout.addWidget(self.label_daichuli, 0, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(400, 50))
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 10, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_turntoGray = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_turntoGray.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_turntoGray.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_turntoGray.setStyleSheet("QPushButton {\n"
"    background-color:#00ebc7 ; /* 深青色背景 */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #3A6073; /* 边框颜色与背景色一致 */\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    transition: box-shadow 0.5s;\n"
"    box-shadow: 0 0 20px #eee;\n"
"    display: block;\n"
"    margin: 5px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3A6073; /* 悬浮时改为更深的颜色 */\n"
"    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* 增加悬浮阴影效果 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background-color: #3A6073; /* 按下时使用更深的颜色 */\n"
"    border: 1px solid #616161; /* 按下时边框颜色调整为更深 */\n"
"    color: #fff; /* 维持字体颜色为白色 */\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px; /* 特定按钮的圆角 */\n"
"}\n"
"")
        self.pushButton_turntoGray.setObjectName("pushButton_turntoGray")
        self.horizontalLayout.addWidget(self.pushButton_turntoGray)
        self.pushButton_turntotwo = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_turntotwo.setMinimumSize(QtCore.QSize(80, 50))
        self.pushButton_turntotwo.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_turntotwo.setStyleSheet("QPushButton {\n"
"    background-color:#00ebc7 ; /* 深青色背景 */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #3A6073; /* 边框颜色与背景色一致 */\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    transition: box-shadow 0.5s;\n"
"    box-shadow: 0 0 20px #eee;\n"
"    display: block;\n"
"    margin: 5px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3A6073; /* 悬浮时改为更深的颜色 */\n"
"    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* 增加悬浮阴影效果 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background-color: #3A6073; /* 按下时使用更深的颜色 */\n"
"    border: 1px solid #616161; /* 按下时边框颜色调整为更深 */\n"
"    color: #fff; /* 维持字体颜色为白色 */\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px; /* 特定按钮的圆角 */\n"
"}\n"
"")
        self.pushButton_turntotwo.setObjectName("pushButton_turntotwo")
        self.horizontalLayout.addWidget(self.pushButton_turntotwo)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Formwin1)
        QtCore.QMetaObject.connectSlotsByName(Formwin1)

    def retranslateUi(self, Formwin1):
        _translate = QtCore.QCoreApplication.translate
        Formwin1.setWindowTitle(_translate("Formwin1", "Form"))
        self.pushButton_load.setText(_translate("Formwin1", "选 择 图 片"))
        self.label_jieguo.setText(_translate("Formwin1", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:black;\">结果</span></p></body></html>"))
        self.label_daichuli.setText(_translate("Formwin1", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:black;\">待处理</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Formwin1", "保 存 图 片"))
        self.pushButton_turntoGray.setText(_translate("Formwin1", "转成灰度图"))
        self.pushButton_turntotwo.setText(_translate("Formwin1", "将图片二值化"))



class Ui_Formwin2(object):
    def setupUi(self, Formwin2):
        Formwin2.setObjectName("Formwin2")
        Formwin2.resize(1100, 700)
        Formwin2.setMinimumSize(QtCore.QSize(1250, 880))
        Formwin2.setMaximumSize(QtCore.QSize(1250, 880))
        Formwin2.setStyleSheet("border-radius:20px;")
        self.layoutWidget = QtWidgets.QWidget(Formwin2)
        self.layoutWidget.setGeometry(QtCore.QRect(85, 180, 1100, 700))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_daichuli = QtWidgets.QLabel(self.layoutWidget)
        self.label_daichuli.setMinimumSize(QtCore.QSize(350, 350))
        self.label_daichuli.setMaximumSize(QtCore.QSize(350, 350))
        self.label_daichuli.setStyleSheet("border-radius:20px;")
        self.label_daichuli.setObjectName("label_daichuli")
        self.horizontalLayout.addWidget(self.label_daichuli)
        self.label_jieguo = QtWidgets.QLabel(self.layoutWidget)
        self.label_jieguo.setMinimumSize(QtCore.QSize(350, 350))
        self.label_jieguo.setMaximumSize(QtCore.QSize(350, 350))
        self.label_jieguo.setStyleSheet("border-radius:20px;")
        self.label_jieguo.setObjectName("label_jieguo")
        self.horizontalLayout.addWidget(self.label_jieguo)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_load = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_load.setMinimumSize(QtCore.QSize(400, 60))
        self.pushButton_load.setMaximumSize(QtCore.QSize(400, 80))
        self.pushButton_load.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.horizontalLayout_2.addWidget(self.pushButton_load)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(400, 50))
        self.pushButton_save.setMaximumSize(QtCore.QSize(400, 80))
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_2.addWidget(self.pushButton_save)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 23, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_tips = QtWidgets.QLabel(self.layoutWidget)
        self.label_tips.setMinimumSize(QtCore.QSize(100, 30))
        self.label_tips.setMaximumSize(QtCore.QSize(100, 30))
        self.label_tips.setObjectName("label_tips")
        self.gridLayout_2.addWidget(self.label_tips, 0, 0, 1, 1)
        self.pushButton_fun0 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_fun0.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_fun0.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_fun0.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: regular; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    color: #757575;\n"
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
        self.pushButton_fun0.setObjectName("pushButton_fun0")
        self.gridLayout_2.addWidget(self.pushButton_fun0, 0, 1, 1, 1)
        self.pushButton_fun1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_fun1.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_fun1.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_fun1.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: regular; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    color: #757575;\n"
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
        self.pushButton_fun1.setObjectName("pushButton_fun1")
        self.gridLayout_2.addWidget(self.pushButton_fun1, 0, 2, 1, 1)
        self.pushButton_fun11 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_fun11.setMinimumSize(QtCore.QSize(100, 50))
        self.pushButton_fun11.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_fun11.setStyleSheet("QPushButton {\n"
"    background-color: #fafafa;\n"
"    border: 1px solid #cccccc;\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: regular; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f5f5f5;\n"
"    color: #757575;\n"
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
        self.pushButton_fun11.setObjectName("pushButton_fun11")
        self.gridLayout_2.addWidget(self.pushButton_fun11, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Formwin2)
        QtCore.QMetaObject.connectSlotsByName(Formwin2)

    def retranslateUi(self, Formwin2):
        _translate = QtCore.QCoreApplication.translate
        Formwin2.setWindowTitle(_translate("Formwin2", "Form"))
        self.label_daichuli.setText(_translate("Formwin2", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;color:black; font-weight:600;\">待处理</span></p></body></html>"))
        self.label_jieguo.setText(_translate("Formwin2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;color:black; font-weight:600;\">结果</span></p></body></html>"))
        self.pushButton_load.setText(_translate("Formwin2", "选 择 图 片"))
        self.pushButton_save.setText(_translate("Formwin2", "保 存 图 片"))
        self.label_tips.setText(_translate("Formwin2", "<head>\n"
"<style>\n"
".center-text {\n"
"  text-align: center;\n"
"  font-size: 14pt;\n"
"  font-weight: 600;\n"
"}\n"
"</style>\n"
"</head>\n"
"<body>\n"
"<p class=\"center-text\">操作：</p>\n"
"</body>"))
        self.pushButton_fun0.setText(_translate("Formwin2", "水平翻转"))
        self.pushButton_fun1.setText(_translate("Formwin2", "垂直翻转"))
        self.pushButton_fun11.setText(_translate("Formwin2", "沿xy轴翻转"))




class Ui_Formwin3(object):
    def setupUi(self, Formwin3):
        Formwin3.setObjectName("Formwin3")
        Formwin3.resize(1100, 700)
        Formwin3.setMinimumSize(QtCore.QSize(1250, 880))
        Formwin3.setMaximumSize(QtCore.QSize(1250, 880))
        self.layoutWidget = QtWidgets.QWidget(Formwin3)
        self.layoutWidget.setGeometry(QtCore.QRect(85, 180, 1100, 700))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_load = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_load.setMinimumSize(QtCore.QSize(400, 65))
        self.pushButton_load.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.gridLayout.addWidget(self.pushButton_load, 1, 0, 1, 1)
        self.label_jieguo = QtWidgets.QLabel(self.layoutWidget)
        self.label_jieguo.setMinimumSize(QtCore.QSize(350, 350))
        self.label_jieguo.setMaximumSize(QtCore.QSize(350, 350))
        self.label_jieguo.setToolTipDuration(0)
        self.label_jieguo.setAlignment(QtCore.Qt.AlignCenter)
        self.label_jieguo.setObjectName("label_jieguo")
        self.gridLayout.addWidget(self.label_jieguo, 0, 1, 1, 1)
        self.label_daichuli = QtWidgets.QLabel(self.layoutWidget)
        self.label_daichuli.setMinimumSize(QtCore.QSize(350, 350))
        self.label_daichuli.setMaximumSize(QtCore.QSize(350, 350))
        self.label_daichuli.setObjectName("label_daichuli")
        self.gridLayout.addWidget(self.label_daichuli, 0, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(400, 65))
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 0, -1, 98)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_lap = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_lap.setMinimumSize(QtCore.QSize(300, 80))
        self.pushButton_lap.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_lap.setStyleSheet("QPushButton {\n"
"    background-color: #FCF6F5; /* 淡粉色背景 */\n"
"    color: #2BAE66; /* 深褐色文字 */\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"   /* border: 1px solid #3A6073; /* 边框颜色暂时保留为深青色 */\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    transition: box-shadow 0.5s, color 0.5s; /* 添加颜色过渡效果 */\n"
"    box-shadow: 0 0 20px #eee;\n"
"    display: block;\n"
"    margin: 15px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2BAE66; /* 悬浮时背景色变为深褐色 */\n"
"    color: #FCF6F5; /* 悬浮时字体颜色变为白色 */\n"
"    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* 增加悬浮阴影效果 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background-color: #2BAE66; /* 按下时背景色为更深的颜色 */\n"
"    border: 1px solid #616161; /* 按下时边框颜色调整为更深 */\n"
"    color: #FCF6F5; /* 按下时字体颜色变为淡粉色 */\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px; /* 特定按钮的圆角 */\n"
"}\n"
"")
        self.pushButton_lap.setObjectName("pushButton_lap")
        self.gridLayout_2.addWidget(self.pushButton_lap, 0, 0, 1, 1)
        self.pushButton_gama = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_gama.setMinimumSize(QtCore.QSize(300, 80))
        self.pushButton_gama.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_gama.setStyleSheet("QPushButton {\n"
"    background-color: #FCF6F5; /* 淡粉色背景 */\n"
"    color: #2BAE66; /* 深褐色文字 */\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"   /* border: 1px solid #3A6073; /* 边框颜色暂时保留为深青色 */\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    transition: box-shadow 0.5s, color 0.5s; /* 添加颜色过渡效果 */\n"
"    box-shadow: 0 0 20px #eee;\n"
"    display: block;\n"
"    margin: 15px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2BAE66; /* 悬浮时背景色变为深褐色 */\n"
"    color: #FCF6F5; /* 悬浮时字体颜色变为白色 */\n"
"    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* 增加悬浮阴影效果 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background-color: #2BAE66; /* 按下时背景色为更深的颜色 */\n"
"    border: 1px solid #616161; /* 按下时边框颜色调整为更深 */\n"
"    color: #FCF6F5; /* 按下时字体颜色变为淡粉色 */\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px; /* 特定按钮的圆角 */\n"
"}\n"
"")
        self.pushButton_gama.setObjectName("pushButton_gama")
        self.gridLayout_2.addWidget(self.pushButton_gama, 1, 1, 1, 1)
        self.pushButton_zhifangtu = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_zhifangtu.setMinimumSize(QtCore.QSize(300, 80))
        self.pushButton_zhifangtu.setMaximumSize(QtCore.QSize(200, 50))
        self.pushButton_zhifangtu.setStyleSheet("QPushButton {\n"
"    background-color: #FCF6F5; /* 淡粉色背景 */\n"
"    color: #2BAE66; /* 深褐色文字 */\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"   /* border: 1px solid #3A6073; /* 边框颜色暂时保留为深青色 */\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    transition: box-shadow 0.5s, color 0.5s; /* 添加颜色过渡效果 */\n"
"    box-shadow: 0 0 20px #eee;\n"
"    display: block;\n"
"    margin: 15px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2BAE66; /* 悬浮时背景色变为深褐色 */\n"
"    color: #FCF6F5; /* 悬浮时字体颜色变为白色 */\n"
"    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* 增加悬浮阴影效果 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background-color: #2BAE66; /* 按下时背景色为更深的颜色 */\n"
"    border: 1px solid #616161; /* 按下时边框颜色调整为更深 */\n"
"    color: #FCF6F5; /* 按下时字体颜色变为淡粉色 */\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 20px; /* 特定按钮的圆角 */\n"
"}\n"
"")
        self.pushButton_zhifangtu.setObjectName("pushButton_zhifangtu")
        self.gridLayout_2.addWidget(self.pushButton_zhifangtu, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setMinimumSize(QtCore.QSize(300, 80))
        self.frame_2.setMaximumSize(QtCore.QSize(200, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 0, 281, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(3, 0, 3, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setMinimumSize(QtCore.QSize(40, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 50))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_power_value = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_power_value.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEdit_power_value.setMaximumSize(QtCore.QSize(200, 30))
        self.lineEdit_power_value.setStyleSheet("lineEdit->setStyleSheet(\"QLineEdit { background-color: white; border: 1px solid gray; }\");")
        self.lineEdit_power_value.setObjectName("lineEdit_power_value")
        self.horizontalLayout.addWidget(self.lineEdit_power_value)
        self.gridLayout_2.addWidget(self.frame_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)

        self.retranslateUi(Formwin3)
        QtCore.QMetaObject.connectSlotsByName(Formwin3)

    def retranslateUi(self, Formwin3):
        _translate = QtCore.QCoreApplication.translate
        Formwin3.setWindowTitle(_translate("Formwin3", "Form"))
        self.pushButton_load.setText(_translate("Formwin3", "选 择 图 片"))
        self.label_jieguo.setText(_translate("Formwin3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;color:black; font-weight:600;\">结果</span></p></body></html>"))
        self.label_daichuli.setText(_translate("Formwin3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;color:black; font-weight:600;\">待处理</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Formwin3", "保 存 图 片"))
        self.pushButton_lap.setText(_translate("Formwin3", "拉普拉斯变化"))
        self.pushButton_gama.setText(_translate("Formwin3", "伽马变化"))
        self.pushButton_zhifangtu.setText(_translate("Formwin3", "直方图均衡"))
        self.label.setText(_translate("Formwin3", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">power:</span></p></body></html>"))


class Ui_Formwin4(object):
    def setupUi(self, Formwin4):
        Formwin4.setObjectName("Formwin4")
        Formwin4.resize(1100, 700)
        Formwin4.setMinimumSize(QtCore.QSize(1250, 880))
        Formwin4.setMaximumSize(QtCore.QSize(1250, 880))
        self.splitter = QtWidgets.QSplitter(Formwin4)
        self.splitter.setGeometry(QtCore.QRect(85, 180, 1100, 700))
        self.splitter.setMinimumSize(QtCore.QSize(1100, 700))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_load = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_load.setMinimumSize(QtCore.QSize(400, 60))
        self.pushButton_load.setMaximumSize(QtCore.QSize(400, 80))
        self.pushButton_load.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.gridLayout.addWidget(self.pushButton_load, 1, 0, 1, 1)
        self.label_jieguo = QtWidgets.QLabel(self.layoutWidget)
        self.label_jieguo.setMinimumSize(QtCore.QSize(400, 400))
        self.label_jieguo.setMaximumSize(QtCore.QSize(400, 400))
        self.label_jieguo.setStyleSheet("")
        self.label_jieguo.setObjectName("label_jieguo")
        self.gridLayout.addWidget(self.label_jieguo, 0, 1, 1, 1)
        self.label_daichuli = QtWidgets.QLabel(self.layoutWidget)
        self.label_daichuli.setMinimumSize(QtCore.QSize(400, 400))
        self.label_daichuli.setMaximumSize(QtCore.QSize(400, 400))
        self.label_daichuli.setStyleSheet("")
        self.label_daichuli.setObjectName("label_daichuli")
        self.gridLayout.addWidget(self.label_daichuli, 0, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(400, 60))
        self.pushButton_save.setMaximumSize(QtCore.QSize(400, 80))
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setMinimumSize(QtCore.QSize(80, 50))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_seg = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_seg.setMinimumSize(QtCore.QSize(150, 60))
        self.pushButton_seg.setMaximumSize(QtCore.QSize(200, 100))
        self.pushButton_seg.setStyleSheet("QPushButton {\n"
"    background-color: #FFFFFF; /* 白色背景 */\n"
"    color: #000000; /* 黑色文字 */\n"
"    padding: 5px;\n"
"    border-radius: 5px;\n"
"    border: 1px solid #3A6073; /* 边框颜色可以根据需要启用，此处保持注释状态 */\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    transition: box-shadow 0.5s, color 0.5s; /* 添加颜色过渡效果 */\n"
"    box-shadow: 0 0 20px #eee; /* 提供轻微的阴影，增加层次感 */\n"
"    display: block;\n"
"    margin: 5px;\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #000000; /* 悬浮时背景色变为黑色 */\n"
"    color: #FFFFFF; /* 悬浮时字体颜色变为白色 */\n"
"    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); /* 增加悬浮时的阴影效果 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background-color: #616161; /* 按下时背景色变为深灰色 */\n"
"    border: 1px solid #434343; /* 按下时边框颜色调整为深灰 */\n"
"    color: #FFFFFF; /* 按下时字体颜色保持为白色 */\n"
"}\n"
"\n"
"#button3 {\n"
"    border-radius: 50px; /* 特定按钮的圆角 */\n"
"}\n"
"")
        self.pushButton_seg.setObjectName("pushButton_seg")
        self.horizontalLayout.addWidget(self.pushButton_seg)

        self.retranslateUi(Formwin4)
        QtCore.QMetaObject.connectSlotsByName(Formwin4)

    def retranslateUi(self, Formwin4):
        _translate = QtCore.QCoreApplication.translate
        Formwin4.setWindowTitle(_translate("Formwin4", "Form"))
        self.pushButton_load.setText(_translate("Formwin4", "选择图片"))
        self.label_jieguo.setText(_translate("Formwin4", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:black;\">结果</span></p></body></html>"))
        self.label_daichuli.setText(_translate("Formwin4", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:black;\">待处理</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Formwin4", "保存图片"))
        self.pushButton_seg.setText(_translate("Formwin4", "血 管 分 割"))


class Ui_Formwin5(object):
    def setupUi(self, Formwin5):
        Formwin5.setObjectName("Formwin5")
        Formwin5.resize(1100, 700)
        Formwin5.setMinimumSize(QtCore.QSize(1250, 880))
        Formwin5.setMaximumSize(QtCore.QSize(1250, 880))
        self.splitter = QtWidgets.QSplitter(Formwin5)
        self.splitter.setGeometry(QtCore.QRect(85, 180, 1100, 700))
        self.splitter.setMinimumSize(QtCore.QSize(1100, 700))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_load = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_load.setMinimumSize(QtCore.QSize(400, 60))
        self.pushButton_load.setMaximumSize(QtCore.QSize(400, 80))
        self.pushButton_load.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.gridLayout.addWidget(self.pushButton_load, 1, 0, 1, 1)
        self.label_jieguo = QtWidgets.QLabel(self.layoutWidget)
        self.label_jieguo.setMinimumSize(QtCore.QSize(400, 400))
        self.label_jieguo.setMaximumSize(QtCore.QSize(400, 400))
        self.label_jieguo.setStyleSheet("")
        self.label_jieguo.setObjectName("label_jieguo")
        self.gridLayout.addWidget(self.label_jieguo, 0, 1, 1, 1)
        self.label_daichuli = QtWidgets.QLabel(self.layoutWidget)
        self.label_daichuli.setMinimumSize(QtCore.QSize(400, 400))
        self.label_daichuli.setMaximumSize(QtCore.QSize(400, 400))
        self.label_daichuli.setStyleSheet("")
        self.label_daichuli.setObjectName("label_daichuli")
        self.gridLayout.addWidget(self.label_daichuli, 0, 0, 1, 1)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(400, 60))
        self.pushButton_save.setMaximumSize(QtCore.QSize(400, 80))
        self.pushButton_save.setStyleSheet("QPushButton {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #bdc3c7, stop:0.51 #2c3e50, stop:1 #bdc3c7);\n"
"    border: 2px solid #bdc3c7; /* 初始状态下的边框颜色 */\n"
"    padding: 10px 45px;\n"
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setMinimumSize(QtCore.QSize(80, 50))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_pre = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_pre.setMinimumSize(QtCore.QSize(150, 80))
        self.pushButton_pre.setMaximumSize(QtCore.QSize(200, 100))
        self.pushButton_pre.setStyleSheet("QPushButton {\n"
"    background-color: #CCF2F4; /* 设置为纯色背景 */\n"
"    border: 2px solid #CCF2F4; /* 初始边框颜色与背景色一致 */\n"
"    padding: 10px 10px;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"    text-transform: uppercase;\n"
"    box-shadow: 0 0 20px #eee;\n"
"    display: block;\n"
"    margin: 5px;\n"
"    color: #31363F; /* 文字颜色为白色 */\n"
"    transition: box-shadow 0.5s, border-color 0.5s; /* 添加过渡效果 */\n"
"font-family: \"Arial\"; /* 添加字体族 */\n"
"    font-size: 24px; /* 添加字体大小 */\n"
"    font-weight: bold; /* 添加字体粗细 */\n"
"    font-style: normal; /* 添加字体风格 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #AAAAAA;\n"
"    color: white;\n"
"    border-color: darken(#CCF2F4, 10%); /* 鼠标悬浮时边框颜色变深 */\n"
"    box-shadow: 0 0 20px darken(#CCF2F4, 10%); /* 增加悬浮时的阴影效果，边框颜色变深 */\n"
"}\n"
"\n"
"QPushButton:pressed, QPushButton:checked {\n"
"    background-color: #B2E4E6; /* 按下时的背景颜色稍微变深 */\n"
"    color: #FFF; /* 按下时保持文字颜色为白色 */\n"
"}\n"
"")
        self.pushButton_pre.setObjectName("pushButton_pre")
        self.horizontalLayout.addWidget(self.pushButton_pre)

        self.retranslateUi(Formwin5)
        QtCore.QMetaObject.connectSlotsByName(Formwin5)

    def retranslateUi(self, Formwin5):
        _translate = QtCore.QCoreApplication.translate
        Formwin5.setWindowTitle(_translate("Formwin5", "Form"))
        self.pushButton_load.setText(_translate("Formwin5", "选 择 图 片"))
        self.label_jieguo.setText(_translate("Formwin5", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:black;\">结果</span></p></body></html>"))
        self.label_daichuli.setText(_translate("Formwin5", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:black;\">待处理</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Formwin5", "保 存 图 片"))
        self.pushButton_pre.setText(_translate("Formwin5", "图像预处理"))

class Ui_Formwin6(object):
    def setupUi(self, Formwin6):
        Formwin6.setObjectName("Formwin6")
        Formwin6.resize(1100, 700)
        Formwin6.setMinimumSize(QtCore.QSize(1250, 880))
        Formwin6.setMaximumSize(QtCore.QSize(1250, 880))
        self.splitter = QtWidgets.QSplitter(Formwin6)
        self.splitter.setGeometry(QtCore.QRect(85, 180, 1100, 700))
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
        self.pushButton_load.setMaximumSize(QtCore.QSize(400, 80))
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.pushButton_classical.setMinimumSize(QtCore.QSize(150, 60))
        self.pushButton_classical.setMaximumSize(QtCore.QSize(200, 100))
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
"    font-size: 24px; /* 添加字体大小 */\n"
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
        self.lineEdit_2.setMaximumSize(QtCore.QSize(300, 40))
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
        self.lineEdit_4.setMaximumSize(QtCore.QSize(300, 40))
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
        self.lineEdit_0.setMaximumSize(QtCore.QSize(300, 40))
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
        self.lineEdit_1.setMaximumSize(QtCore.QSize(300, 40))
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
        self.lineEdit_3.setMaximumSize(QtCore.QSize(300, 40))
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
        self.label.setMaximumSize(QtCore.QSize(300, 50))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Formwin6)
        QtCore.QMetaObject.connectSlotsByName(Formwin6)

    def retranslateUi(self, Formwin6):
        _translate = QtCore.QCoreApplication.translate
        Formwin6.setWindowTitle(_translate("Formwin6", "Form"))
        self.pushButton_load.setText(_translate("Formwin6", "选 择 图 片"))
        self.pushButton_classical.setText(_translate("Formwin6", "病变诊断"))
        self.label_daichuli.setText(_translate("Formwin6", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:black;\">待处理</span></p></body></html>"))
        self.lineEdit_2.setText(_translate("Formwin6", "2-Moderate"))
        self.lineEdit_4.setText(_translate("Formwin6", "4-Proliferative DR"))
        self.lineEdit_0.setWhatsThis(_translate("Formwin6", "<html><head/><body><p align=\"center\"><br/>0-No DR</p></body></html>"))
        self.lineEdit_0.setText(_translate("Formwin6", "0-No DR"))
        self.lineEdit_1.setText(_translate("Formwin6", "1-Mild"))
        self.lineEdit_3.setText(_translate("Formwin6", "3-Severe"))
        self.label.setText(_translate("Formwin6", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">诊断结果</span></p></body></html>"))
