# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fromwin5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formwin5(object):
    def setupUi(self, Formwin5):
        Formwin5.setObjectName("Formwin5")
        Formwin5.resize(1100, 700)
        Formwin5.setMinimumSize(QtCore.QSize(1100, 700))
        Formwin5.setMaximumSize(QtCore.QSize(1100, 700))
        self.splitter = QtWidgets.QSplitter(Formwin5)
        self.splitter.setGeometry(QtCore.QRect(-10, -10, 1100, 700))
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
        self.pushButton_load.setMaximumSize(QtCore.QSize(400, 60))
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
        self.pushButton_save.setMaximumSize(QtCore.QSize(400, 60))
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
        self.pushButton_save.setObjectName("pushButton_save")
        self.gridLayout.addWidget(self.pushButton_save, 1, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setMinimumSize(QtCore.QSize(80, 50))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_pre = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_pre.setMinimumSize(QtCore.QSize(150, 60))
        self.pushButton_pre.setMaximumSize(QtCore.QSize(150, 60))
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
"    font-size: 14px; /* 添加字体大小 */\n"
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
        self.label_jieguo.setText(_translate("Formwin5", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">结果</span></p></body></html>"))
        self.label_daichuli.setText(_translate("Formwin5", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">待处理</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Formwin5", "保 存 图 片"))
        self.pushButton_pre.setText(_translate("Formwin5", "图像预处理"))

