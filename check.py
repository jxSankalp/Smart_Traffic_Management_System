import cv2
import os

# Define paths
model_path = os.path.join(os.getcwd(), "yolov3.weights")
config_path = os.path.join(os.getcwd(), "yolov3.cfg")

# Load YOLO model
net = cv2.dnn.readNet(model_path, config_path)

# Verify if model is loaded
if net.empty():
    print("Error: Failed to load YOLO model. Check file paths.")
else:
    print("YOLO model loaded successfully.")
