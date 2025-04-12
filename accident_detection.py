import numpy as np
import tensorflow as tf
from PIL import Image
import cv2

# Load the TFLite model and set up the interpreter
interpreter = tf.lite.Interpreter(model_path='models/tf_lite_model.tflite')
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
interpreter.allocate_tensors()

def accident_detection(image_path):
    """
    Predict accident status from an image using the TensorFlow Lite model.
    
    Args:
        image_path: Path to the input image.
    
    Returns:
        str: "Accident" or "No Accident"
    """
    try:
        # Load and preprocess the image
        img = Image.open(image_path).resize((250, 250))  # Resize to 250x250 as required
        img_array = np.array(img, dtype=np.float32)  # Convert to numpy array
        img_array = img_array / 255.0  # Normalize
        img_batch = np.expand_dims(img_array, axis=0)  # Expand dims to shape (1, 250, 250, 3)
        
        # Run inference
        interpreter.set_tensor(input_details[0]['index'], img_batch)
        interpreter.invoke()
        
        # Get the output and interpret it
        prediction = interpreter.get_tensor(output_details[0]['index'])[0]
        print("Prediction results:", prediction)  # This will give [Accident_score, Non_Accident_score]
        
        # Depending on the model output, decide the prediction
        if prediction[0] > prediction[1]:  # Check if "Accident" score is greater than "Non-Accident"
            return "Accident"
        else:
            return "No Accident"

    except Exception as e:
        print("Error during prediction:", e)
        return "Error"
