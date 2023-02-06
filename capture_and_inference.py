import torch
import cv2 
import boto3
import time
from pathlib import Path
from botocore.exceptions import ClientError
from IPython.display import display
import pandas as pd

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
sns = boto3.client('sns')
webcam = cv2.VideoCapture(0)
phone_num = "+16472002360" # receiver's number
camera_msg = False

while True:
    ret, frame = webcam.read()
    ##messenger.publish_text_message(phone_num,"Camera is active!")
    if (camera_msg == False):
        sns.publish(PhoneNumber = phone_num, Message='Camera is active!' )
        camera_msg = True

    

    if ret:
        cv2.imshow("detecting",frame)
        #cv2.imshow('YOLO', np.squeeze(results.render()))
        print("triggering yolov5")
        img = frame  # or file, Path, PIL, OpenCV, numpy, list

        # model.conf = 0.5  # NMS confidence threshold
        # iou = 0.45  # NMS IoU threshold
        # agnostic = False  # NMS class-agnostic
        # multi_label = False  # NMS multiple labels per box
        # classes = None  # (optional list) filter by class, i.e. = [0, 15, 16] for COCO persons, cats and dogs
        # max_det = 1000  # maximum number of detections per image
        # amp = False  # Automatic Mixed Precision (AMP) inference
        
        #print("time: ", time.time())
        results = model(img)
        #print("test print: ",results)
        results.print()
        #results.save()
        results = results.pandas().xyxy[0]
        display(results)

        found = results[results['name'].str.contains('cat')]
        num_cat = len(found)
        
        if (num_cat > 0):
            print("found: ", num_cat," cats")
            sns.publish(PhoneNumber = phone_num, Message='Cat appeared ^-^!' )
            time.sleep(2)
        # labels = results.xyxyn[0][:,-1]
        # for i in labels:
        #     print(i)

        #counter = 0
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

        #counter += 1
    
sns.publish(PhoneNumber = phone_num, Message='Camera is inactive!' )
webcam.release()
cv2.destroyAllWindows()

# def class_to_label(x):
#     return classes[int (x)]

# class SnsWrapper:
#     """Encapsulates Amazon SNS topic and subscription functions."""
#     def __init__(self, sns_resource):
#         """
#         :param sns_resource: A Boto3 Amazon SNS resource.
#         """
#         self.sns_resource = sns_resource

#     def publish_text_message(self, phone_number, message):
#         """
#         Publishes a text message directly to a phone number without need for a
#         subscription.

#         :param phone_number: The phone number that receives the message. This must be
#                              in E.164 format. For example, a United States phone
#                              number might be +12065550101.
#         :param message: The message to send.
#         :return: The ID of the message.
#         """
#         try:
#             response = self.sns_resource.meta.client.publish(
#                 PhoneNumber=phone_number, Message=message)
#             message_id = response['MessageId']
#             print("Published message to %s.", phone_number)
#         except ClientError:
#             print("Couldn't publish message to %s.", phone_number)
#             raise
#         else:
#             return message_id





# #Model
# #model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom

# # Images
# #img = 'https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?cs=srgb&dl=pexels-pixabay-45201.jpg&fm=jpg'  # or file, Path, PIL, OpenCV, numpy, list

# # Inference
# # results = model(img)

# # Results
# #results.print()  # or .show(), .save(), .crop(), .pandas(), etc.


"""
next steps
- send message when cat is detected √
- trigger smartplug
- implement alexa to detect cat

"""