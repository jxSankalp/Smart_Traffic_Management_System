import os
import random

def get_random_image_from_folder(folder_path):
    """
    Get a random image from a specified folder.
    """
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    if not image_files:
        print("No images found in the folder.")
        return None
    random_image = random.choice(image_files)
    return os.path.join(folder_path, random_image)
