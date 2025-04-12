import random
import time
from vehicle_count import detect_vehicles
from accident_handler import handle_accidents
from traffic_signal_control import control_traffic_signal
from utils import get_random_image_from_folder

# Folder paths
traffic_folder = "data/traffic_eg"
accident_folder = "data/accidents_eg"

def run_cycle(direction, vehicle_count):
    """
    Runs a cycle of vehicle count, accident detection, and traffic signal control for one direction.
    """
    print(f"\nProcessing {direction} direction...")

    # Step 1: Get random image and detect vehicles
    image_path = get_random_image_from_folder(traffic_folder)
    if image_path:
        vehicle_count = detect_vehicles(image_path)
        # vehicle_count = 10
        print(f"Vehicle count for {direction}: {vehicle_count}")

    # Step 2: Set accident status as a variable (change this manually when needed)
    accident_input = 1  # Set to 1 for "Accident" or 0 for "No Accident"

    # Step 3: Handle accidents based on the variable accident_input
    accident_status = handle_accidents(accident_input, accident_folder)

    # Step 4: Control traffic signals based on vehicle count and accident status
    traffic_signal_status = control_traffic_signal(vehicle_count, accident_status)

    # Step 5: Print traffic light status and duration
    print(f"Traffic signal status for {direction}:")
    print(f"  Left     → {traffic_signal_status['left']}")
    print(f"  Right    → {traffic_signal_status['right']}")
    print(f"  Straight → {traffic_signal_status['straight']}")
    print(f"  Green light duration: {traffic_signal_status['duration']} seconds")

def main():
    directions = ["North", "East", "South", "West"]

    # while True:
    for direction in directions:
      vehicle_count = 0  # Initial vehicle count
      run_cycle(direction, vehicle_count)
      time.sleep(2)  # Wait time between each direction cycle

if __name__ == "__main__":
    main()
