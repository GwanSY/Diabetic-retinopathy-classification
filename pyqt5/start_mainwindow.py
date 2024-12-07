import threading
import cv2
import numpy as np
import Mainwindow
import sys
import picture_fun
from PyQt5.Qt import *
from pytorch_classification.seg_onepicture import main as Seg
from pytorch_classification.preprocess import main as Preprocess
from pytorch_classification.predict import main as Predict
# from MPRNet.Deblurring.test import main as MPRNetPredict
import qimage2ndarray
# todo 信号机制
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal as Signal

## todo
class MySignals(QObject):
    # 定义一种信号，参数是列表
    message = Signal(list)

class MainWindow(QWidget,Mainwindow.Ui_Mainwindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Checkeye")  # 设置窗口标题
        self.setWindowIcon(QIcon("icon.png"))  # 设置窗口图标，需要提供图标文件的路径

        self.stackedLayout = QStackedLayout(self.frame)

        self.page1 = FramePage1()
        self.page2 = FramePage2()
        self.page3 = FramePage3()
        self.page4 = FramePage4()
        self.page5 = FramePage5()
        self.page6 = FramePage6()


        self.stackedLayout.addWidget(self.page1)
        self.stackedLayout.addWidget(self.page2)
        self.stackedLayout.addWidget(self.page3)
        self.stackedLayout.addWidget(self.page4)
        self.stackedLayout.addWidget(self.page5)
        self.stackedLayout.addWidget(self.page6)


        self.controller()

    def controller(self):
        self.pushButton_1.clicked.connect(self.switch1)
        self.pushButton_2.clicked.connect(self.switch2)
        self.pushButton_3.clicked.connect(self.switch3)
        # self.pushButton_4.clicked.connect(self.switch4)
        self.pushButton_5.clicked.connect(self.switch5)
        self.pushButton_6.clicked.connect(self.switch6)


    def switch1(self):
        self.stackedLayout.setCurrentIndex(0)  # 索引按加入布局的顺序
    def switch2(self):
        self.stackedLayout.setCurrentIndex(1)
    def switch3(self):
        self.stackedLayout.setCurrentIndex(2)
    def switch4(self):
        self.stackedLayout.setCurrentIndex(3)
    def switch5(self):
        self.stackedLayout.setCurrentIndex(4)
    def switch6(self):
        self.stackedLayout.setCurrentIndex(5)

class FramePage1(QWidget, Mainwindow.Ui_Formwin1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_load.clicked.connect(self.openimage)
        self.pushButton_save.clicked.connect(self.saveimage)
        self.pushButton_turntoGray.clicked.connect(self.fun1)
        self.pushButton_turntotwo.clicked.connect(self.fun2)

    def openimage(self):#随便写到哪都行 那边可以读到就好饿了
        fname = QFileDialog.getOpenFileName(self, '打开图片', './', "Images (*.png *.jpg *.bmp)")
        print('fname',fname)
        if fname[0]:
            self.label_daichuli.setPixmap(QPixmap(fname[0]))
            self.label_daichuli.setWordWrap(True)
            self.label_daichuli.setScaledContents(True)

    def saveimage(self):
        nfname = QFileDialog.getSaveFileName(self, "保存图片", "./", "Images (*.png *.jpg *.bmp)")
        if nfname[0]:
            self.label_jieguo.pixmap().save(nfname[0])

    def fun1(self):
        qimg = self.label_daichuli.pixmap()
        src = qimage2mat(qimg)
        newsrc = picture_fun.gray_picture(src)
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)

    def fun2(self):
        qimg = self.label_daichuli.pixmap()
        src = qimage2mat(qimg)
        newsrc = picture_fun.erzhihua(src)
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)


class FramePage2(QWidget, Mainwindow.Ui_Formwin2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_load.clicked.connect(self.openimage)
        self.pushButton_save.clicked.connect(self.saveimage)
        self.pushButton_fun0.clicked.connect(self.fun1)
        self.pushButton_fun1.clicked.connect(self.fun2)
        self.pushButton_fun11.clicked.connect(self.fun3)

    def openimage(self):
        fname = QFileDialog.getOpenFileName(self, '打开图片', './', "Images (*.png *.jpg *.bmp)")
        if fname[0]:
            self.label_daichuli.setPixmap(QPixmap(fname[0]))
            self.label_daichuli.setWordWrap(True)
            self.label_daichuli.setScaledContents(True)

    def saveimage(self):
        nfname = QFileDialog.getSaveFileName(self, "保存图片", "./", "Images (*.png *.jpg *.bmp)")
        if nfname[0]:
            self.label_jieguo.pixmap().save(nfname[0])

    def fun1(self):
        qimg = self.label_daichuli.pixmap()
        src = qimage2mat(qimg)
        newsrc = picture_fun.flipfun(src,0)
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)

    def fun2(self):
        qimg = self.label_daichuli.pixmap()
        src = qimage2mat(qimg)
        newsrc = picture_fun.flipfun(src,1)
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)

    def fun3(self):
        qimg = self.label_daichuli.pixmap()
        src = qimage2mat(qimg)
        newsrc = picture_fun.flipfun(src,-1)
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)


class FramePage3(QWidget, Mainwindow.Ui_Formwin3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_load.clicked.connect(self.openimage)
        self.pushButton_save.clicked.connect(self.saveimage)
        self.pushButton_lap.clicked.connect(self.lap_fun)
        self.pushButton_zhifangtu.clicked.connect(self.equalhist_fun)
        self.pushButton_gama.clicked.connect(self.gama_fun)

    def openimage(self):
        fname = QFileDialog.getOpenFileName(self, '打开图片', './', "Images (*.png *.jpg *.bmp)")
        if fname[0]:
            self.label_daichuli.setPixmap(QPixmap(fname[0]))
            self.label_daichuli.setWordWrap(True)
            self.label_daichuli.setScaledContents(True)

    def saveimage(self):
        nfname = QFileDialog.getSaveFileName(self, "保存图片", "./", "Images (*.png *.jpg *.bmp)")
        if nfname[0]:
            self.label_jieguo.pixmap().save(nfname[0])

    def lap_fun(self):
        qimg = self.label_daichuli.pixmap()
        src = qimage2mat(qimg)
        newsrc = picture_fun.lap_9(src)
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)

    def equalhist_fun(self):
        qimg = self.label_daichuli.pixmap()
        if qimg is None:
            print("Error: No image loaded in label_daichuli.")
            return
        src = qimage2mat(qimg)
        debug_image("original.png", src)  # 调试原始图像
        newsrc = picture_fun.cal_equalhist(src)
        debug_image("equalized.png", newsrc)  # 调试均衡化后的图像
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)

    def gama_fun(self):
        qimg = self.label_daichuli.pixmap()
        src = qimage2mat(qimg)
        power=self.lineEdit_power_value.text()
        power=float(power)
        newsrc = picture_fun.gama_transfer(src,power)
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)

class FramePage5(QWidget, Mainwindow.Ui_Formwin5):#预处理
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_load.clicked.connect(self.openimage)
        self.pushButton_save.clicked.connect(self.saveimage)
        self.pushButton_pre.clicked.connect(self.Preprocess1)
        # self.pushButton_MPRnet.clicked.connect(self.MPRNet)
        # self.pushButton_DeblurGan.clicked.connect(self.DeblurGan)
        # self.pushButton_Deblurganv2.clicked.connect(self.DeblurGanv2)
        self.image_path = None

        # todo 信号机制实例化
        self.ms = MySignals()
        self.ms.message.connect(self.showPicRes)

    def openimage(self):
        fname = QFileDialog.getOpenFileName(self, '打开图片', './', "Images (*.png *.jpg *.bmp)")
        self.image_path= fname#"./test.jpg"
        #global_image= "./test.jpg"
        # global image_path
        # image_path="./test.jpg"
        # global output_path
        # output_path="./result"
        if fname[0]:
            self.label_daichuli.setPixmap(QPixmap(fname[0]))
            self.label_daichuli.setWordWrap(True)
            self.label_daichuli.setScaledContents(True)
        print(fname)

    def saveimage(self):
        nfname = QFileDialog.getSaveFileName(self, "保存图片", "./", "Images (*.png *.jpg *.bmp)")
        if nfname[0]:
            self.label_jieguo.pixmap().save(nfname[0])

    def process(self):
        qimg = self.label_daichuli.pixmap()
        src = qimage2mat(qimg)
        newsrc = picture_fun.process(src)
        pix = matqimage(newsrc)
        self.label_jieguo.setPixmap(pix)
        self.label_jieguo.setWordWrap(True)
        self.label_jieguo.setScaledContents(True)
#########################下面是对应方法调用的函数#################################
    def Preprocess1(self):
        # 子线程功能函数
        def runThread():
            Preprocess(self.image_path[0], ui=self)
        # 子线程启动
        threading.Thread(target=runThread).start()

    # todo 信号机制的接收函数  接收到一个列表
    def showPicRes(self, data):
        picData = data[0]
        print(picData)
        frame = picData
        label = self.label_jieguo
        # showImage = QImage(frameRGB.data, frameRGB.shape[1], frameRGB.shape[0],frameRGB.shape[1] * 3, QImage.Format_RGB888)
        # label.setPixmap(QPixmap.fromImage(showImage).scaled(label.width(), label.height(), Qt.KeepAspectRatio))
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = qimage2ndarray.array2qimage(frameRGB)
        label.setPixmap(QPixmap(img).scaled(label.width(), label.height(), Qt.KeepAspectRatio))

####################从这里开始###########################################
class FramePage4(QWidget, Mainwindow.Ui_Formwin4):#分割
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_load.clicked.connect(self.openimage)
        self.pushButton_save.clicked.connect(self.saveimage)
        self.pushButton_seg.clicked.connect(self.Seg1)
        self.image_path = None

        # todo 信号机制实例化
        self.ms = MySignals()
        self.ms.message.connect(self.showPicRes)

    def openimage(self):
        fname = QFileDialog.getOpenFileName(self, '打开图片', './', "Images (*.png *.jpg *.bmp)")
        self.image_path= fname#"./test.jpg"
        #global_image= "./test.jpg"
        # global image_path
        # image_path="./test.jpg"
        # global output_path
        # output_path="./result"
        if fname[0]:
            self.label_daichuli.setPixmap(QPixmap(fname[0]))
            self.label_daichuli.setWordWrap(True)
            self.label_daichuli.setScaledContents(True)
        print(fname)

    def saveimage(self):
        nfname = QFileDialog.getSaveFileName(self, "保存图片", "./", "Images (*.png *.jpg *.bmp)")
        if nfname[0]:
            self.label_jieguo.pixmap().save(nfname[0])

#########################下面是对应方法调用的函数#################################
    def Seg1(self):
        # 子线程功能函数
        def runThread():
            Seg(self.image_path[0], ui=self)
        # 子线程启动
        threading.Thread(target=runThread).start()

    # todo 信号机制的接收函数  接收到一个列表
    def showPicRes(self, data):
        picData = data[0]
        print(picData)
        frame = picData
        label = self.label_jieguo
        # showImage = QImage(frameRGB.data, frameRGB.shape[1], frameRGB.shape[0],frameRGB.shape[1] * 3, QImage.Format_RGB888)
        # label.setPixmap(QPixmap.fromImage(showImage).scaled(label.width(), label.height(), Qt.KeepAspectRatio))
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = qimage2ndarray.array2qimage(frameRGB)
        label.setPixmap(QPixmap(img).scaled(label.width(), label.height(), Qt.KeepAspectRatio))

########################################################################################################33
class FramePage6(QWidget, Mainwindow.Ui_Formwin6):#分类
    prediction_result_signal = pyqtSignal(int)  # 定义一个新的信号
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_load.clicked.connect(self.openimage)
        # self.pushButton_save.clicked.connect(self.saveimage)
        self.pushButton_classical.clicked.connect(self.Classicial)
        self.image_path = None

        # todo 信号机制实例化
        self.ms = MySignals()
        self.prediction_result_signal.connect(self.update_ui_based_on_prediction)

    def openimage(self):
        fname = QFileDialog.getOpenFileName(self, '打开图片', './', "Images (*.png *.jpg *.bmp)")
        self.image_path= fname#"./test.jpg"
        #global_image= "./test.jpg"
        # global image_path
        # image_path="./test.jpg"
        # global output_path
        # output_path="./result"
        if fname[0]:
            self.label_daichuli.setPixmap(QPixmap(fname[0]))
            self.label_daichuli.setWordWrap(True)
            self.label_daichuli.setScaledContents(True)
        print(fname)

    # def saveimage(self):
    #     nfname = QFileDialog.getSaveFileName(self, "保存图片", "./", "Images (*.png *.jpg *.bmp)")
    #     if nfname[0]:
    #         self.label_jieguo.pixmap().save(nfname[0])

    # def Seg(self):
    #     qimg = self.label_daichuli.pixmap()
    #     src = qimage2mat(qimg)
    #     newsrc = picture_fun.xiufu(src)
    #     pix = matqimage(newsrc)
    #     self.label_jieguo.setPixmap(pix)
    #     self.label_jieguo.setWordWrap(True)
    #     self.label_jieguo.setScaledContents(True)
#########################下面是对应方法调用的函数#################################
    def Classicial(self):
        # 子线程功能函数
        def runThread():
            Predict(self.image_path[0], ui=self)
        # 子线程启动
        threading.Thread(target=runThread).start()


    def update_ui_based_on_prediction(self, predicted_index):
        # 重置所有相关UI元素的颜色
        # default_style = "background-color: white;"
        # self.lineEdit_0.setStyleSheet(default_style)
        # self.lineEdit_1.setStyleSheet(default_style)
        # self.lineEdit_2.setStyleSheet(default_style)
        # self.lineEdit_3.setStyleSheet(default_style)
        # self.lineEdit_4.setStyleSheet(default_style)
        # self.reset_ui_elements_color()

        # 根据predicted_index来设置特定UI元素的颜色
        # 这里需要根据实际情况来编写代码
        print(f"Updating UI for predicted index: {predicted_index}")
        if predicted_index == 0:
            self.lineEdit_0.setStyleSheet("background-color: green;")
        elif predicted_index == 1:
            self.lineEdit_1.setStyleSheet("background-color: #B6D7A8;")
        elif predicted_index == 2:
            self.lineEdit_2.setStyleSheet("background-color: #F9CB9C;")
        elif predicted_index == 3:
            self.lineEdit_3.setStyleSheet("background-color: #E69138;")
        elif predicted_index == 4:
            self.lineEdit_4.setStyleSheet("background-color: #CC0000;")
        # 依此类推，为每个分类结果设置颜色

    # todo 信号机制的接收函数  接收到一个列表
    def showPicRes(self, data):
        picData = data[0]
        print(picData)
        frame = picData
        label = self.label_jieguo
        # showImage = QImage(frameRGB.data, frameRGB.shape[1], frameRGB.shape[0],frameRGB.shape[1] * 3, QImage.Format_RGB888)
        # label.setPixmap(QPixmap.fromImage(showImage).scaled(label.width(), label.height(), Qt.KeepAspectRatio))
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = qimage2ndarray.array2qimage(frameRGB)
        label.setPixmap(QPixmap(img).scaled(label.width(), label.height(), Qt.KeepAspectRatio))

####################################################################33
def qimage2mat(qtpixmap):    #qtpixmap转opencv
    qimg = qtpixmap.toImage()
    temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
    temp_shape += (4,)
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
    result = result[..., :3]
    return result

def debug_image(name, img):
    cv2.imwrite(name, img)
    print(f"{name} saved.")
def matqimage(cvimg):
    # 判断图像的通道数
    if cvimg.ndim == 2:  # 单通道图像（灰度图）
        height, width = cvimg.shape
        qimg = QImage(cvimg.data, width, height, width, QImage.Format_Grayscale8)
    else:  # 多通道图像（如BGR图像）
        height, width, channels = cvimg.shape
        # 转换为RGB格式
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        step = channels * width
        qimg = QImage(cvimg.data, width, height, step, QImage.Format_RGB888)

    # 从QImage创建QPixmap
    pix = QPixmap.fromImage(qimg)
    return pix
# def matqimage(cvimg):       #opencv转QImage
#     if cvimg.ndim==2:              #单通道
#         height, width= cvimg.shape
#         cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
#         cvimg = QImage(cvimg.data, width, height, QImage.Format_RGB888)
#         pix = QPixmap.fromImage(cvimg)
#         return pix
#     else:                          #多个通道
#         width = cvimg.shape[1]
#         height = cvimg.shape[0]
#         pixmap = QPixmap(width, height)  # 根据已知的高度和宽度新建一个空的QPixmap,
#         qimg = pixmap.toImage()         # 将pximap转换为QImage类型的qimg
#         for row in range(0, height):
#             for col in range(0, width):
#                 b = cvimg[row, col, 0]
#                 g = cvimg[row, col, 1]
#                 r = cvimg[row, col, 2]
#                 pix = qRgb(r, g, b)
#                 qimg.setPixel(col, row, pix)
#                 pix = QPixmap.fromImage(qimg)
#         return pix
def qimage2mat_equalhist(qimg):#直方图专用
    qimg = qimg.toImage()
    width = qimg.width()
    height = qimg.height()
    ptr = qimg.bits()
    ptr.setsize(qimg.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  # Assuming RGBA
    return cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)  # Convert to BGR
def matqimage_equalhist(cvimg):
    if cvimg.ndim == 2:  # 单通道图像（灰度图）
        height, width = cvimg.shape
        qimg = QImage(cvimg.data, width, height, width, QImage.Format_Grayscale8)
    else:  # 多通道图像（如BGR图像）
        height, width, channels = cvimg.shape
        # 转换为RGB格式
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        step = channels * width
        qimg = QImage(cvimg.data, width, height, step, QImage.Format_RGB888)

        # 从QImage创建QPixmap
    pix = QPixmap.fromImage(qimg)
    return pix

def matqimage_guass(cvimg):          #opencv转QImage   #guass 专用####
    if cvimg.ndim==2:                    #单通道
        height, width= cvimg.shape
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        cvimg = QImage(cvimg.data, width, height, QImage.Format_RGB888)
        pix = QPixmap.fromImage(cvimg)
        return pix
    else:                                #多个通道
        width = cvimg.shape[1]  # 获取图片宽度
        height = cvimg.shape[0]  # 获取图片高度
        pixmap = QPixmap(width, height)  # 根据已知的高度和宽度新建一个空的QPixmap,
        qimg = pixmap.toImage()  # 将pximap转换为QImage类型的qimg
        for row in range(0, height):
            for col in range(0, width):
                b = int(cvimg[row, col, 0]*255)            #高斯加噪归一化了 要*255
                g = int(cvimg[row, col, 1]*255)
                r = int(cvimg[row, col, 2]*255)
                pix = qRgb(r, g, b)
                qimg.setPixel(col, row, pix)
                pix = QPixmap.fromImage(qimg)
        return pix  # 转换完成，返回

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())