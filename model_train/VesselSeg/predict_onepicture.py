import numpy as np
from copy import deepcopy
from PIL import Image
import models
import torch
from os.path import join
import torchvision.transforms as transforms
from lib.pre_processing import *
import os


def visual(pred_res):
    pred_res = data = np.transpose(pred_res, (1, 2, 0))

    binary = deepcopy(pred_res)
    binary[binary >= 0.5] = 1
    binary[binary < 0.5] = 0

    binary = np.repeat((binary * 255).astype(np.uint8), repeats=3, axis=2)

    return binary


def save_img(data, filename):
    assert (len(data.shape) == 3)  # height*width*channels
    if data.shape[2] == 1:
        data = np.reshape(data, (data.shape[0], data.shape[1]))
    img = Image.fromarray(data.astype(np.uint8))
    img.save(filename)
    return img


def img_transform(img):
    transform = transforms.Compose(
        [
            transforms.ToTensor(),
            transforms.Resize([800, 800])
        ]
    )
    img = transform(img)
    return img


def process_image(save_path, image_path, output_path):
    device = torch.device("cpu")  # 使用CPU
    net = models.UNetFamily.U_Net(1, 2).to(device)
    print('==> Loading checkpoint...')
    checkpoint = torch.load(join(save_path, 'best_model.pth'), map_location=device)  # 确保在CPU上加载模型
    net.load_state_dict(checkpoint['net'])
    net.eval()

    img = Image.open(image_path).convert('RGB')
    img = np.array(img)
    img = np.expand_dims(img, axis=0)
    img = img.transpose(0, 3, 1, 2)
    img = my_PreProc(img)
    img = np.squeeze(img)
    img = img_transform(img)

    with torch.no_grad():
        c, w, h = img.shape
        img = img.expand(1, c, w, h)
        img = img.type(torch.FloatTensor)
        img = img.to(device)
        output = net(img)
        output = output[:, 1].data.cpu().numpy()
        vs = visual(output)
        save_img(vs, output_path)
        print(f"Image saved to {output_path}")


# 使用示例：
process_image("./experiments/UNet_vessel_seg/", "./test/test.png", "./seg/output_image.jpg")
