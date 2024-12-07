import numpy as np
from copy import deepcopy
from PIL import Image
import models
import torch
from os.path import join
import torchvision.transforms as transforms
from lib.pre_processing import *
import os

def visual(pred_res): #分割结果可视化
    pred_res = data = np.transpose(pred_res,(1,2,0))

    binary = deepcopy(pred_res)
    binary[binary>=0.5]=1
    binary[binary<0.5]=0 

    binary = np.repeat((binary*255).astype(np.uint8),repeats=3,axis=2)

    return binary

def save_img(data,filename): #保存分割结果
    assert (len(data.shape)==3) #height*width*channels
    if data.shape[2]==1:  #in case it is black and white
        data = np.reshape(data,(data.shape[0],data.shape[1]))
    img = Image.fromarray(data.astype(np.uint8))  #the image is between 0-1
    img.save(filename)
    return img

def img_transform(img):
    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            #transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            #transforms.Normalize([0.5],[0.5]),
            #transforms.Resize([512,512])
            transforms.Resize([800,800])
        ]
    )
    img = transform(img)
    return img

def main(save_path, images_path):
    # #device = torch.device("cuda" if torch.cuda.is_available() and args.cuda else "cpu")
    # device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # net = models.UNetFamily.U_Net(1,2).to(device)
    # print('==> Loading checkpoint...')
    # checkpoint = torch.load(join(save_path, 'best_model.pth'),map_location='cuda:0')
    # net.load_state_dict(checkpoint['net'])
    # net.eval()
    # imgs = os.listdir(images_path)

    device = torch.device("cpu")  # 直接设置为CPU
    net = models.UNetFamily.U_Net(1, 2).to(device)  # 确保模型在CPU上
    print('==> Loading checkpoint...')
    checkpoint = torch.load(join(save_path, 'best_model.pth'), map_location=device)  # 确保在CPU上加载模型
    net.load_state_dict(checkpoint['net'])
    net.eval()
    imgs = os.listdir(images_path)
    for image_path in imgs:
        print(image_path)
        img = Image.open(images_path + image_path).convert('RGB')
        img = np.array(img)
        img = np.expand_dims(img, axis=0)
        img = img.transpose(0,3,1,2)
        #print(img.shape)
        img = my_PreProc(img)
        #print(img.shape)
        img = np.squeeze(img)
        #img = Image.open(image_path)
        img =  img_transform(img)
        with torch.no_grad():
            c, w, h = img.shape
            img = img.expand(1, c, w, h)
            img = img.type(torch.FloatTensor)
            img = img.to(device)
            output = net(img)
            output = output[:,1].data.cpu().numpy()
            vs = visual(output)
            save_img(vs, "./seg/" + image_path)
            print("saved")


if __name__ == "__main__":
    #main("./experiments/UNet_vessel_seg/", "./test_imgs/img/")
    main("./experiments/UNet_vessel_seg/", "./test/")
