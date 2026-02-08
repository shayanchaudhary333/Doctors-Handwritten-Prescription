import streamlit as st
import pytesseract
import cv2
import numpy as np
import pandas as pd
import pickle
from tensorflow.keras.models import load_model

# Set path to Tesseract executable (required for OCR to work)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Title of the app
st.title("Handwritten Prescription to Structured Medicine List")

# Load pre-trained model and label encoder
@st.cache_resource
def load_model_and_encoder():
    model = load_model(r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\model.h5")
    with open(r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\label_encoder.pkl", "rb") as file:
        label_encoder = pickle.load(file)
    return model, label_encoder

model, label_encoder = load_model_and_encoder()

# Load disease-medicine dataset from CSV
@st.cache_data
def load_disease_data():
    csv_path = r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\disease_data.csv"
    return pd.read_csv(csv_path)

disease_data = load_disease_data()

# Extract text from image using OCR
def extract_text_from_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)       # Convert image to grayscale
    text = pytesseract.image_to_string(gray)             # Extract text using Tesseract
    return text

# Predict disease or medicine using the trained ML model
def predict_disease(image):
    image = cv2.resize(image, (128, 128))                # Resize for model input
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)       # Convert to grayscale
    feature = np.mean(gray)                              # Use mean pixel value as feature
    input_data = np.array([[feature]], dtype=np.float32) # Model expects 2D input
    prediction = model.predict(input_data)               # Get prediction
    predicted_class = label_encoder.inverse_transform([np.argmax(prediction)])
    return predicted_class[0]

# If predicted output is a medicine, reverse-map it to corresponding disease
def reverse_medicine_to_disease(medicine_name, df):
    filtered = df[df['medicine'].str.lower() == medicine_name.lower()]
    if filtered.empty:
        return None
    return filtered['disease'].iloc[0]

# Get medicine recommendations for a given disease
def get_medicines_for_disease(disease, df):
    filtered = df[df['disease'].str.lower() == disease.lower()]
    if filtered.empty:
        return None
    return filtered[['medicine', 'dose', 'time']]

# File uploader to accept prescription image
uploaded_file = st.file_uploader("Upload Handwritten Prescription Image", type=["png", "jpg", "jpeg"])

# Main logic after file is uploaded
if uploaded_file:
    # Convert uploaded image to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Display uploaded image
    st.image(image, caption="Uploaded Prescription", use_column_width=True)

    # OCR: Extract text from the prescription image
    st.subheader("Extracted Text")
    extracted_text = extract_text_from_image(image)
    st.text_area("Detected Text", extracted_text, height=150)

    # Predict disease or medicine from the image
    st.subheader("Prediction Result")
    prediction = predict_disease(image)

    # Check if prediction is a medicine and map it back to disease
    actual_disease = reverse_medicine_to_disease(prediction, disease_data)
    if actual_disease:
        disease = actual_disease
        st.info(f"Detected as medicine: '{prediction}' → Associated disease: '{disease}'")
    else:
        disease = prediction
        st.success(f"Predicted Disease: {disease}")

    # Show medicines for the identified disease
    st.subheader("Suggested Medicines")
    meds = get_medicines_for_disease(disease, disease_data)
    if meds is not None:
        st.dataframe(meds)
    else:
        st.warning("No medicines found for the predicted disease.")
