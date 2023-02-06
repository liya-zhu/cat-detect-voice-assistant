from IPython.display import display
import pandas as pd
import torch


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom


img = 'https://www.shutterstock.com/image-photo/big-cat-group-260nw-244654435.jpg'  # or file, Path, PIL, OpenCV, numpy, list



results = model(img)

results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
results = results.pandas().xyxy[0]
display(results)

found = results[results['name'].str.contains('cat')]
print(len(found))