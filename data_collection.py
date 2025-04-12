import cv2
import time
import os

# Global list to store saved image filenames and timestamps
image_timestamps = []

def collect_data():
    # Ensure the 'data' directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Initialize camera (0 is default for webcam)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the camera.")
        return

    print("Starting frame capture. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Failed to grab frame. Exiting...")
            break
        
        # Generate a unique filename using the current timestamp
        timestamp = int(time.time())
        filename = f'data/frame_{timestamp}.jpg'
        
        # Save the frame as an image
        cv2.imwrite(filename, frame)
        print(f"Saved: {filename}")
        
        # Keep track of the timestamp and filename
        image_timestamps.append((timestamp, filename))

        # Periodically delete images older than 5 minutes
        delete_old_images()

        # Wait 1 second before capturing the next frame
        time.sleep(1)

        # Break the loop if 'q' is pressed (optional)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Frame capture stopped.")
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def delete_old_images():
    # Get the current time
    current_time = time.time()

    # Define the age limit (5 minutes = 300 seconds)
    age_limit = 300

    global image_timestamps
    still_valid = []
    
    # Iterate through the timestamps and filenames
    for timestamp, filename in image_timestamps:
        if current_time - timestamp > age_limit:
            # Delete old files
            if os.path.exists(filename):
                print(f"Deleting old file: {filename}")
                os.remove(filename)
        else:
            # Keep valid files
            still_valid.append((timestamp, filename))
    
    # Update the global list of timestamps and filenames
    image_timestamps = still_valid

if __name__ == '__main__':
    collect_data()
