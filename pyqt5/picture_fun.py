import math
from PIL import Image
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
####################灰度图和二值化########################################

def gray_picture(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return img_gray

def erzhihua(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    rst = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
    return rst[1]

##################加噪###########################################################
def add_noisy(image, n=10000):    #椒盐彩色
    result = image.copy()
    w, h = image.shape[:2]
    for i in range(n):
        # 宽和高的范围内生成一个随机值，模拟表x,y坐标
        x = np.random.randint(1, w)
        y = np.random.randint(1, h)
        if np.random.randint(0, 2) == 0:
            # 生成白色噪声（盐噪声）
            result[x, y] = 0
        else:
            # 生成黑色噪声（椒噪声）
            result[x, y] = 255
    return result



####################彩色图像添加高斯噪声#######################################
def add_noise(image,mean,var):
    img = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, img.shape)
    out_img = img + noise
    if out_img.min() < 0:
        low_clip = -1
    else:
        low_clip = 0
        out_img = np.clip(out_img, low_clip, 1.0)
        out_img = out_img * 255
    return out_img


################图像锐化#####################
def lap_9(image):                                               #拉普拉斯变化
    lap_9 = np.array([[-1, -1, -1], [-1, 12, -1], [-1, -1, -1]])
    # 拉普拉斯的锐化
    image = cv2.filter2D(image, cv2.CV_8U, lap_9)
    return image

def gama_transfer(img,power1):                              #伽马变化
    if len(img.shape) == 3:
         img= img.astype(np.uint8)
    img = 255*np.power(img/255,power1)
    img = np.around(img)
    img[img>255] = 255
    out_img = img.astype(np.uint8)
    return out_img


def get_imghist(img):                                             #直方图均衡
    # 判断图像是否为三通道；
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 无 Mask，256个bins,取值范围为[0,255]
    hist = cv2.calcHist([img], [0], None, [256], [0, 255])
    return hist


def cal_equalhist(img):
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    h, w = img.shape[:2]
    grathist = get_imghist(img)

    zerosumMoment = np.zeros([256], np.uint32)
    for p in range(256):
        if p == 0:
            zerosumMoment[p] = grathist[0]
        else:
            zerosumMoment[p] = zerosumMoment[p - 1] + grathist[p]

    output_q = np.zeros([256], np.uint8)
    cofficient = 256.0 / (h * w)
    for p in range(256):
        q = cofficient * float(zerosumMoment[p]) - 1
        if q >= 0:
            output_q[p] = math.floor(q)
        else:
            output_q[p] = 0

    equalhistimage = np.zeros(img.shape, np.uint8)
    for i in range(h):
        for j in range(w):
            equalhistimage[i][j] = output_q[img[i][j]]

    return equalhistimage

################图像去噪####################################################
def boxFilterfun(image):       #方波滤波
    image=cv2.boxFilter(image,-1,(2,2),normalize=0)
    return image



def medianBlurfun(image):      #中值滤波
    image=cv2.medianBlur(image,3)
    return image



def bilateralFilterfun(image):   #双边滤波
    image=cv2.bilateralFilter(image,25,100,100)
    return image


def GaussianBlurfun(image):      #高斯滤波
    image=cv2.GaussianBlur(image,(5,5),0,0)
    return image


def blurfun(image):              #均值滤波
    image==cv2.blur(image,(5,5))
    return image


###############图像翻转####################################################
def flipfun(image,x):    #图像  水平翻转:0   垂直翻转:1  沿xy轴翻转:-1
    image = cv2.flip(image,x)
    return image


##############按位取反###################################################
def bitwise_notfun(image):
    image = cv2.bitwise_not(image)
    return image


##############轮廓检测####################################################
def morphologyExfun(image):
    kernel = np.ones((3, 3), dtype=np.uint8)
    image_gradient = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    return image_gradient


#############sift检测#######################################################
def sift_fun(image):
    sift = cv2.SIFT_create()
    kps = sift.detect(image)
    image_sift = cv2.drawKeypoints(image, kps, None, -1, cv2.DrawMatchesFlags_DEFAULT)
    return image_sift


##################平均值池化#################################################
def average_poolingfun(img, G=4):
    out = img.copy()
    H, W, C = img.shape
    Nh = int(H / G)
    Nw = int(W / G)
    for y in range(Nh):
        for x in range(Nw):
            for c in range(C):
                out[G * y:G * (y + 1), G * x:G * (x + 1), c] = np.mean(
                    out[G * y:G * (y + 1), G * x:G * (x + 1), c]).astype(np.int)
    return out

##################################修复####
def xiufu(image):
    _, mask1 = cv2.threshold(image, 245, 255, cv2.THRESH_BINARY)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    mask1 = cv2.dilate(mask1, k)
    result1 = cv2.inpaint(image, mask1[:, :, -1], 5, cv2.INPAINT_NS)
    return result1
###############散焦##########################
def GaussianBlurfun1(image):      #高斯滤波
    image=cv2.GaussianBlur(image,(1,1),0,0)
    return image


################运动模糊#####################
def yd(image_path,out_dir= "./result/yd.jpg",ui=None):
    def motion_blur(image_path, degree=50, angle=45):
        image = np.array(image_path)
        # 这里生成任意角度的运动模糊kernel的矩阵， degree越大，模糊程度越高
        M = cv2.getRotationMatrix2D((degree / 2, degree / 2), angle, 1)
        motion_blur_kernel = np.diag(np.ones(degree))
        motion_blur_kernel = cv2.warpAffine(motion_blur_kernel, M, (degree, degree))
        motion_blur_kernel = motion_blur_kernel / degree
        blurred = cv2.filter2D(image, -1, motion_blur_kernel)
        # convert to uint8
        cv2.normalize(blurred, blurred, 0, 255, cv2.NORM_MINMAX)
        blurred = np.array(blurred, dtype=np.uint8)
        return blurred

    img = cv2.imread(image_path, )
    img_ = motion_blur(img)
    cv2.waitKey()
    cv2.imwrite(os.path.join(out_dir), img_)
    if ui is not None:
        ui.ms.message.emit([img_])
    return ui

###############频谱图########################
def pinpu(image_path, ui=None):
    # 读取图像
    img = cv2.imread(image_path, 0)
    # 快速傅里叶变换算法得到频率分布
    f = np.fft.fft2(img)
    # 默认结果中心点位置是在左上角,
    # 调用fftshift()函数转移到中间位置
    fshift = np.fft.fftshift(f)
    # fft结果是复数, 其绝对值结果是振幅
    fimg = np.log(np.abs(fshift))
    # 将频谱图数据转换为 8 位无符号整数类型
    fimg_uint8 = cv2.normalize(fimg, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    # 保存频谱图为图像文件
    cv2.imwrite("fimg.png", fimg_uint8)
    if ui is not None:
        ui.ms.message.emit([fimg_uint8])
    return ui
# def pinpu(image_path,ui=None):
#         # 读取图像
#     img = cv2.imread(image_path, 0)
#         # 快速傅里叶变换算法得到频率分布s
#     f = np.fft.fft2(img)
#         # 调用fftshift()函数转移到中间位置
#     fshift = np.fft.fftshift(f)
#         # fft结果是复数, 其绝对值结果是振幅
#     fimg = np.log(np.abs(fshift))
#     fimg_list = fimg.tolist()
#     if ui is not None:
#         ui.ms.message.emit([fimg_list])
#     return ui
##################################SRGAN####
import cv2
import numpy as np
import os
from typing import List


def process(input_image_path: str, desired_size=224) -> np.ndarray:
    """
    读取、裁剪、调整大小、应用加权和和高斯模糊到输入图像，返回预处理后的图像数组。
    :param input_image_path: 输入图像的路径。
    :param desired_size: 输出图像的期望大小。
    :return: 预处理后的图像数组。
    """

    def crop_image_from_gray(img, tol=7) -> np.ndarray:
        """
        基于灰度图像和阈值裁剪RGB图像。
        :param img: 输入的RGB图像。
        :param tol: 裁剪阈值。
        :return: 裁剪后的图像。
        """
        if img.ndim == 2:
            mask = img > tol
            return img[np.ix_(mask.any(1), mask.any(0))]
        elif img.ndim == 3:
            gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            mask = gray_img > tol

            if img[:, :, 0][np.ix_(mask.any(1), mask.any(0))].shape[0] == 0:
                return img
            else:
                img = img[:, :, 0][np.ix_(mask.any(1), mask.any(0))]
                img = np.stack([img for _ in range(3)], axis=-1)
            return img

    img = cv2.imread(input_image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = crop_image_from_gray(img)
    img = cv2.resize(img, (desired_size, desired_size))
    img = cv2.addWeighted(img, 4, cv2.GaussianBlur(img, (0, 0), desired_size / 30), -4, 128)

    # 返回预处理后的图像
    return img
# 使用示例
# main('path_to_input_image.jpg', 'path_to_output_image.jpg')
##################################MPRNet####

##################################Deblurgan####

##################################Deblurgan-v2####
# def Deblurgan_v2(image):
#     _, mask1 = cv2.threshold(image, 245, 255, cv2.THRESH_BINARY)
#     k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
#     mask1 = cv2.dilate(mask1, k)
#     result1 = cv2.inpaint(image, mask1[:, :, -1], 5, cv2.INPAINT_NS)
#     return result1
##################################################
if __name__ == '__main__':
    image = cv2.imread("inpaint2.jpg")
    cv2.imshow(' ',image)
    newimage=xiufu(image)
    cv2.imshow(' ',newimage)
    cv2.waitKey(0)

