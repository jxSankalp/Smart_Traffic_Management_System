from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("models/yolov8n.pt")


def detect_vehicles(image_path):
    """
    Detect vehicles in the image using YOLOv8.
    
    Args:
        image_path: Path to the image file.
    
    Returns:
        int: Count of detected vehicles.
    """
    frame = cv2.imread(image_path)
    results = model(frame)
    vehicle_count = 0
    
    # Iterate through the detected objects and count vehicles
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Get class ID
            confidence = float(box.conf[0])  # Get confidence score

            if confidence > 0.5:
                # COCO IDs for vehicle classes: Car (2), Motorcycle (3), Bus (5), Truck (7)
                if class_id in [2, 3, 5, 7]:
                    vehicle_count += 1

    return vehicle_count
