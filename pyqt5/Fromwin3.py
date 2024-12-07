# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fromwin3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Formwin3(object):
    def setupUi(self, Formwin3):
        Formwin3.setObjectName("Formwin3")
        Formwin3.resize(1100, 700)
        Formwin3.setMinimumSize(QtCore.QSize(1100, 700))
        Formwin3.setMaximumSize(QtCore.QSize(1100, 700))
        self.layoutWidget = QtWidgets.QWidget(Formwin3)
        self.layoutWidget.setGeometry(QtCore.QRect(0, -4, 1101, 771))
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
"    font-size: 14px; /* 添加字体大小 */\n"
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
"    font-size: 14px; /* 添加字体大小 */\n"
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
"    font-size: 14px; /* 添加字体大小 */\n"
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
        self.label_jieguo.setText(_translate("Formwin3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">结果</span></p></body></html>"))
        self.label_daichuli.setText(_translate("Formwin3", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">待处理</span></p></body></html>"))
        self.pushButton_save.setText(_translate("Formwin3", "保 存 图 片"))
        self.pushButton_lap.setText(_translate("Formwin3", "拉普拉斯变化"))
        self.pushButton_gama.setText(_translate("Formwin3", "伽马变化"))
        self.pushButton_zhifangtu.setText(_translate("Formwin3", "直方图均衡"))
        self.label.setText(_translate("Formwin3", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">power:</span></p></body></html>"))

