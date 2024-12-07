# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fromwin2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formwin2(object):
    def setupUi(self, Formwin2):
        Formwin2.setObjectName("Formwin2")
        Formwin2.resize(1100, 700)
        Formwin2.setMinimumSize(QtCore.QSize(1100, 700))
        Formwin2.setMaximumSize(QtCore.QSize(1100, 700))
        Formwin2.setStyleSheet("border-radius:20px;")
        self.layoutWidget = QtWidgets.QWidget(Formwin2)
        self.layoutWidget.setGeometry(QtCore.QRect(-1, 0, 1101, 701))
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
        self.horizontalLayout_2.addWidget(self.pushButton_load)
        self.pushButton_save = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_save.setMinimumSize(QtCore.QSize(400, 50))
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
"    font-size: 14px; /* 添加字体大小 */\n"
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
"    font-size: 14px; /* 添加字体大小 */\n"
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
"    font-size: 14px; /* 添加字体大小 */\n"
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
        self.label_daichuli.setText(_translate("Formwin2", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">待处理</span></p></body></html>"))
        self.label_jieguo.setText(_translate("Formwin2", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">结果</span></p></body></html>"))
        self.pushButton_load.setText(_translate("Formwin2", "选 择 图 片"))
        self.pushButton_save.setText(_translate("Formwin2", "保 存 图 片"))
        self.label_tips.setText(_translate("Formwin2", "<head>\n"
"<style>\n"
".center-text {\n"
"  text-align: center;\n"
"  font-size: 12pt;\n"
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

