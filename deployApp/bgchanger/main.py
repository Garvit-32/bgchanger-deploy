import cv2
import torch
import numpy as np
from PIL import Image
from .utility import inference
from .models.hrnet import hrnet


def process(foreground, background):

    person = Image.open(foreground)  # reads person image
    person = np.array(person)
    image = person.copy()

    bg = Image.open(background)  # reads background image
    bg = np.array(bg)
    h, w, _ = image.shape
    hh, ww, cc = bg.shape

    # comparison between size
    if ww < w and hh < h:
        # if size of background < size of person image
        bg = cv2.resize(bg, (w, h))
        # bg is resized to person image
    elif ww < w:
        # if only width of background < width of person image
        bg = cv2.resize(bg, (w, hh))
        # bg width is resized to person image width
    elif hh < h:
        # if only height of background < height of person image
        bg = cv2.resize(bg, (ww, h))
        # bg height is resized to person image height

    #model is created
    model = hrnet(2)
    model.load_state_dict(
        torch.load('./deployApp/bgchanger/hrnetv2_hrnet18_person_dataset_120.pth', map_location=torch.device("cpu"))[
            "state_dict"]
    )  # model is loaded
    model.eval()

    with torch.no_grad():  # gradients are off
        # padding of image of person , so that both background image and person image are same
        xx = ww - w
        yy = hh - h
        xx = int((abs(xx)+xx)/2)
        yy = int((abs(yy)+yy)/2)
        ori_image = np.pad(image, ((yy//2, yy - yy//2), (xx//2, xx - xx//2), (0, 0)), 'constant',
                           constant_values=0)

        # output from semantic segmentation model
        prediction = inference(person, model)
        # from numpy convert to PIL format
        prediction = Image.fromarray(prediction)

        # prediction is converted to 3D array
        seg = np.zeros_like(image)
        seg[:, :, 0] = prediction

        seg[:, :, 1] = prediction
        seg[:, :, 2] = prediction

        seg = np.pad(seg, ((yy//2, yy - yy//2), (xx//2, xx - xx//2),  (0, 0)), 'constant',
                     constant_values=0)

        # array is made by keeping person image pixel where person is present else background image pixels
        result = np.where(seg, ori_image, bg)

        final_image = Image.fromarray(result, "RGB")

        return final_image
