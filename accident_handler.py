import random
from accident_detection import accident_detection
from utils import get_random_image_from_folder
import os

def handle_accidents(accident_input, accident_folder):
    """
    Handle accident detection based on user input.

    Arguments:
    accident_input -- 1 if accident detected, 0 otherwise.
    accident_folder -- Folder containing accident and non-accident images.

    Returns:
    list: Status for the left, right, and straight lanes in the direction.
    """
    accident_status = []

    # Simulate accident detection based on input
    if accident_input == 0:
        print("No accident detected, using non-accident images for all lanes.")
        for _ in range(3):
            image_path = get_random_image_from_folder(os.path.join(accident_folder, "non_accident"))
            status = accident_detection(image_path)
            accident_status.append(status)
    else:
        print("Accident detected, using a mix of non-accident and accident images.")
        for _ in range(3):
            is_accident = random.random() < 0.33
            subfolder = "accident" if is_accident else "non_accident"
            image_path = get_random_image_from_folder(os.path.join(accident_folder, subfolder))
            status = accident_detection(image_path)
            accident_status.append(status)

    return accident_status
