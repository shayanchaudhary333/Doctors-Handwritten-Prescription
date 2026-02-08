import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.efficientnet import preprocess_input
import joblib
import os

# ✅ Model & encoder path
MODEL_PATH = r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\best_prescription_model.h5"
ENCODER_PATH = r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\label_encoder.pkl"
IMAGE_PATH = r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\Doctors Handwritten Prescription BD dataset\Training\training\check_image\check_image.png"

# ✅ Load model & label encoder
model = load_model(MODEL_PATH)
label_enc = joblib.load(ENCODER_PATH)

# ✅ Prediction function
def predict_prescription_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ Could not load image at path: {img_path}")
        return None, None

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    arr = preprocess_input(img.astype('float32'))
    arr = np.expand_dims(arr, axis=0)

    pred = model.predict(arr)
    idx = np.argmax(pred)
    label = label_enc.inverse_transform([idx])[0]
    prob = float(pred[0, idx])
    return label, prob

# ✅ Run prediction
medicine, confidence = predict_prescription_image(IMAGE_PATH)

if medicine is not None:
    print(f"✅ Predicted Medicine: {medicine} ({confidence*100:.2f}%)")
else:
    print("❌ Prediction failed.")
