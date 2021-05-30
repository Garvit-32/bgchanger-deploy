import numpy as np
from PIL import Image
import torch
import torch.nn as nn
import torch.onnx

# from torch.onnx import symbolic_opset9
from onnx import version_converter, helper
from deployApp.bgchanger.models.hrnet import hrnet
from deployApp.bgchanger.utility import preprocess_image

model = hrnet(2)
model.load_state_dict(
    torch.load('deployApp/bgchanger/weights/hrnetv2_hrnet18_person_dataset_120.pth')[
        "state_dict"]
)
frame = Image.open('result/image2.jpg')
frame = np.array(frame)

image = preprocess_image(frame)

with torch.no_grad():
    output = model(image)


torch.onnx.export(model, (image), 'model_onnx.onnx',
                  input_names=['image'], output_names=['output'], dynamic_axes={
    "image": {2: "width", 3: "height"},
    "output": {2: "width", 3: "height"}}, opset_version=11)
