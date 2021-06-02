import numpy as np
import torch
import os
from torchvision import transforms

transformation = transforms.Compose(
    [transforms.ToPILImage(), transforms.ToTensor()])


def normalize(image):
    return transforms.Normalize(mean=[0.473408, 0.44432889, 0.42011778], std=[0.23041105, 0.22339764, 0.22698703])(
        transformation(image)
    )


def preprocess_image(image):

    image = normalize(image)
    return torch.unsqueeze(image, dim=0)


def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()


def inference(frame, model):

    w, h, _ = frame.shape

    image = preprocess_image(frame)

    onnx_input = {'image': to_numpy(image)}

    prediction = model.run(None, onnx_input)

    prediction = np.argmax(prediction[0][0], axis=0).astype(np.uint8)

    # print('='*60)
    # print(np.argmax(prediction[0][0], axis=0).shape)
    # print('='*60)
    # with torch.no_grad():
    #     prediction = model(image)

    # prediction = (
    #     torch.argmax(prediction[0], dim=0)
    #     .squeeze(dim=0)
    #     .numpy()
    #     .astype(np.uint8)
    # )

    return prediction
