import numpy as np
import tensorflow as tf
from utils.preprocess import preprocess_image

MODEL_PATH = "model/signs_cnn_model.keras"

model = tf.keras.models.load_model(MODEL_PATH)

CLASS_NAMES = ["0", "1", "2", "3", "4", "5"]

def predict_finger_sign(image_path):
    img = preprocess_image(image_path)
    preds = model.predict(img)
    class_index = np.argmax(preds)
    confidence = float(np.max(preds))
    
    return CLASS_NAMES[class_index], confidence
