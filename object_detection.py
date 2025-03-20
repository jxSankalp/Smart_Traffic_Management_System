from ultralytics import YOLO
import cv2
import traffic_signal_control  # Import traffic signal logic

# Load YOLOv8 model (downloaded automatically if not available)
model = YOLO("yolov8n.pt")  # 'n' stands for nano (fast & lightweight)

def detect_objects(frame):
    # Run YOLOv8 inference
    results = model(frame)

    vehicle_count = 0  # Initialize vehicle counter

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])  # Get class ID
            confidence = float(box.conf[0])  # Get confidence score

            if confidence > 0.5:
                # COCO IDs: Car (2), Motorcycle (3), Bus (5), Truck (7)
                if class_id in [2, 3, 5, 7]:
                    vehicle_count += 1

    return vehicle_count  # Return number of detected vehicles

if __name__ == '__main__':
    # Read image/frame
    frame = cv2.imread('data/frame_0.jpg')  # Replace with actual frame
    vehicle_count = detect_objects(frame)

    # Prepare data and call traffic signal logic
    traffic_data = {'vehicle_count': vehicle_count, 'waiting_time': 30}
    traffic_signal_control.control_traffic_signal(traffic_data)  # Call function from traffic_signal.py
