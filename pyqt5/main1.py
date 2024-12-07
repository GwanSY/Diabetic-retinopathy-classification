# Existing imports...
import login
import Mainwindow
from PyQt5 import QtCore, QtGui, QtWidgets
import resources_rc
import threading

import cv2
import numpy as np
from PyQt5.QtGui import QPixmap, QImage, qRgb
import subprocess
import Mainwindow
import login
from PyQt5.QtWidgets import *
import sys
import os
import picture_fun
import tempfile
from PyQt5.Qt import *
# todo 信号机制
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal as Signal

## todo
class MySignals(QObject):
    # 定义一种信号，参数是列表
    message = Signal(list)

class LoginWindow(QtWidgets.QDialog, login.Ui_Dialog):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.pushButton_login.clicked.connect(self.login)

    def login(self):
        # Implement login functionality here
        # For example:
        username = self.lineEdit_username.text()
        password = self.lineEdit_password.text()
        if username == "admin" and password == "password":
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password!")

class MainWindow(QtWidgets.QMainWindow, Mainwindow.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.controller()

    def controller(self):
        self.listWidget.itemClicked.connect(self.handle_list_item_click)

    def handle_list_item_click(self, item):
        text = item.text()
        if text == "血管分割":
            self.open_vessel_segmentation()
        elif text == "图像增强":
            self.open_image_enhancement()
        elif text == "图像预处理":
            self.open_image_preprocessing()
        elif text == "病变诊断":
            self.open_lesion_diagnosis()

    def open_vessel_segmentation(self):
        # Implement opening vessel segmentation window
        # For example:
        QtWidgets.QMessageBox.information(self, "Info", "Vessel Segmentation Window will open here.")

    def open_image_enhancement(self):
        # Implement opening image enhancement window
        # For example:
        QtWidgets.QMessageBox.information(self, "Info", "Image Enhancement Window will open here.")

    def open_image_preprocessing(self):
        # Implement opening image preprocessing window
        # For example:
        QtWidgets.QMessageBox.information(self, "Info", "Image Preprocessing Window will open here.")

    def open_lesion_diagnosis(self):
        # Implement opening lesion diagnosis window
        # For example:
        QtWidgets.QMessageBox.information(self, "Info", "Lesion Diagnosis Window will open here.")

class Application(QtWidgets.QApplication):
    def __init__(self, argv):
        super(Application, self).__init__(argv)
        self.login_window = LoginWindow()
        self.main_window = None
        self.signals = MySignals()
        self.signals.message.connect(self.handle_message)
        self.login_window.accepted.connect(self.show_main_window)
        self.login_window.show()

    def show_main_window(self):
        self.login_window.close()
        self.main_window = MainWindow()
        self.main_window.show()

    def handle_message(self, message):
        # Handle messages received from different windows
        pass

if __name__ == "__main__":
    import sys
    app = Application(sys.argv)
    sys.exit(app.exec_())
