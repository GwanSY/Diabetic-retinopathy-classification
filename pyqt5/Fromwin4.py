# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fromwin4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formwin4(object):
    def setupUi(self, Formwin4):
        Formwin4.setObjectName("Formwin4")
        Formwin4.resize(1100, 700)
        Formwin4.setMinimumSize(QtCore.QSize(1100, 700))
        Formwin4.setMaximumSize(QtCore.QSize(1100, 700))
        self.splitter = QtWidgets.QSplitter(Formwin4)
        self.splitter.setGeometry(QtCore.QRect(0, 0, 1100, 700))
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
        self.pushButton_seg = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_seg.setMinimumSize(QtCore.QSize(150, 60))
        self.pushButton_seg.setMaximumSize(QtCore.QSize(150, 60))
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
"    font-size: 14px; /* 添加字体大小 */\n"
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
        self.label_jieguo.setText(_translate("Formwin4", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">结果</span></p></body></html>"))
        self.label_daichuli.setText(_translate("Formwin4", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">待处理</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Formwin4", "保存图片"))
        self.pushButton_seg.setText(_translate("Formwin4", "血 管 分 割"))
