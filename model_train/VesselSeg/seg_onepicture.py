from copy import deepcopy
from PIL import Image
import pytorch_classification.seg.seg_models as models
import torch
from os.path import join
import torchvision.transforms as transforms
from pytorch_classification.seg.pre_processing import *
from typing import List  # Make sure to import List for type hinting
import os

current_path = os.path.dirname(__file__) + '/'

class ImageProcessor:
    def __init__(self, ui=None):
        self.ui = ui

    def visual(self, pred_res):
        pred_res = np.transpose(pred_res, (1, 2, 0))
        binary = deepcopy(pred_res)
        binary[binary >= 0.5] = 1
        binary[binary < 0.5] = 0
        binary = np.repeat((binary * 255).astype(np.uint8), repeats=3, axis=2)
        return binary

    def save_img(self, data, filename):
        assert (len(data.shape) == 3)  # height*width*channels
        if data.shape[2] == 1:
            data = np.reshape(data, (data.shape[0], data.shape[1]))
        img = Image.fromarray(data.astype(np.uint8))
        print(f"Saving image to: {filename}")
        img.save(filename)
        return img

    def img_transform(self, img):
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize([800, 800])
        ])
        img = transform(img)
        return img

    def process_image(self, model_path, image_path, output_path):
        device = torch.device("cpu")
        # Assuming UNetFamily is defined in models module
        net = models.UNetFamily.U_Net(1, 2).to(device)
        print('==> Loading checkpoint...')
        checkpoint = torch.load(join(model_path), map_location=device)
        net.load_state_dict(checkpoint['net'])
        net.eval()

        img = Image.open(image_path).convert('RGB')
        img = np.array(img)
        img = np.expand_dims(img, axis=0)
        img = img.transpose(0, 3, 1, 2)
        # Assuming my_PreProc is a custom preprocessing function
        img = my_PreProc(img)
        img = np.squeeze(img)
        img = self.img_transform(img)

        with torch.no_grad():
            c, w, h = img.shape
            img = img.expand(1, c, w, h)
            img = img.type(torch.FloatTensor)
            img = img.to(device)
            output = net(img)
            output = output[:, 1].data.cpu().numpy()
            vs = self.visual(output)
            self.save_img(vs, output_path)
            print(f"Image saved to {output_path}")

            # Convert processed image to BGR format for UI or further processing
            vs_bgr = cv2.cvtColor(vs, cv2.COLOR_RGB2BGR)

            # Utilize UI's signal mechanism to emit the processed image if UI is provided
            if self.ui is not None:
                self.ui.ms.message.emit([vs_bgr])
                print("Processed image emitted to UI.")

            # Optionally, return the processed image array
            return vs_bgr


def main(input_image_path:str,
         output_image_path= current_path ,
         model_path= 'pytorch_classification/seg/best_model.pth',
         ui = None  # 传入界面参数#
        ):
    # Assuming you have some UI setup code here
    processor = ImageProcessor(ui=ui)

    # Example usage
    model_path = model_path
    image_path = input_image_path
    output_path = output_image_path+'seg_output'+'.jpg'
    processor.process_image(model_path, image_path, output_path)


# if __name__ == "__main__":
#     main()

