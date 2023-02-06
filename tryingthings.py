# import torch
# from yolov5 import utils
# import torch
# import utils
# from IPython import display
# from IPython.display import clear_output
# from pathlib import Path
# import yaml
# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import glob

import torch
import os

# from IPython.display import Image  # for displaying images
# print(f"Setup complete. Using torch {torch.__version__} ({torch.cuda.get_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")

# import yaml
# with open(dataset.location + "/data.yaml", 'r') as stream:
#     num_classes = str(yaml.safe_load(stream)['nc'])

import pandas as pd
#print(pd.__version__)

#python train.py --img 416 --batch 16 --epochs 3 --data ../data.yaml --weights yolov5s.pt

#!python detect.py --weights runs/train/exp/weights/best.pt --img 416 --conf 0.1 --source ../test/images
import glob
from IPython.display import Image, display

for imageName in glob.glob('/content/yolov5/runs/detect/exp/*.jpg'): #assuming JPG
    display(Image(filename=imageName))
    print("\n")