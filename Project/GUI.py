import streamlit as st
import pytesseract
import cv2
import numpy as np
import pandas as pd
import pickle
import os
from tensorflow.keras.models import load_model

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Prescription Digitizer",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CSS STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
    }
    .block-container {
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DYNAMIC PATH LOADING ---
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "model.h5")
encoder_path = os.path.join(current_dir, "label_encoder.pkl")
csv_path = os.path.join(current_dir, "disease_data.csv")

# --- LOAD RESOURCES ---
@st.cache_resource
def load_model_and_encoder():
    if not os.path.exists(model_path):
        st.error(f"Error: Model file missing at {model_path}")
        return None, None
    if not os.path.exists(encoder_path):
        st.error(f"Error: Encoder file missing at {encoder_path}")
        return None, None
        
    try:
        model = load_model(model_path)
        with open(encoder_path, "rb") as file:
            label_encoder = pickle.load(file)
        return model, label_encoder
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None, None

@st.cache_data
def load_disease_data():
    if not os.path.exists(csv_path):
        st.error(f"Error: CSV file missing at {csv_path}")
        return pd.DataFrame()
    return pd.read_csv(csv_path)

# Load everything once
model, label_encoder = load_model_and_encoder()
disease_data = load_disease_data()

# --- HELPER FUNCTIONS ---

def preprocess_image_for_ocr(image):
    """
    Applies thresholding to make handwriting stand out against the background.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian Blur to reduce noise
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Adaptive thresholding is usually better for handwriting
    thresh = cv2.adaptiveThreshold(
        blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )
    return thresh

def extract_text_from_image(image):
    try:
        # Preprocess image for better OCR accuracy
        processed_img = preprocess_image_for_ocr(image)
        # Configure Tesseract to treat the image as a single block of text
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_img, config=custom_config)
        return text
    except Exception as e:
        return f"OCR Error: {e}"

def predict_disease(image):
    if model is None or label_encoder is None:
        return "Model Error"
    try:
        # Preprocessing for the CNN Model (Must match training logic)
        resized = cv2.resize(image, (128, 128))
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        feature = np.mean(gray) # Using mean pixel intensity as feature
        input_data = np.array([[feature]], dtype=np.float32)
        
        prediction = model.predict(input_data)
        predicted_idx = np.argmax(prediction)
        predicted_class = label_encoder.inverse_transform([predicted_idx])
        return predicted_class[0]
    except Exception as e:
        return f"Prediction Error: {e}"

def reverse_medicine_to_disease(medicine_name, df):
    if df.empty: return None
    # Flexible string matching (case insensitive)
    filtered = df[df['medicine'].str.lower() == str(medicine_name).lower()]
    if filtered.empty:
        return None
    return filtered['disease'].iloc[0]

def get_medicines_for_disease(disease, df):
    if df.empty: return None
    filtered = df[df['disease'].str.lower() == str(disease).lower()]
    if filtered.empty:
        return None
    return filtered[['medicine', 'dose', 'time']]

# --- MAIN UI LAYOUT ---

# Sidebar
with st.sidebar:
    st.header("Upload Prescription")
    uploaded_file = st.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])
    
    st.markdown("---")
    st.info("Tip: Ensure the handwriting is legible and the lighting is good for best results.")

# Main Content
st.title("Smart Prescription Digitizer")
st.markdown("### Translate handwritten medical notes into digital records")

if uploaded_file:
    # 1. Read Image
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    # Layout: Two columns (Image | Results)
    col1, col2 = st.columns([1, 1.5], gap="large")

    with col1:
        st.subheader("Original Image")
        st.image(image, caption="Uploaded Scan", use_column_width=True)
        
        with st.expander("Show OCR Processed Image"):
            st.image(preprocess_image_for_ocr(image), caption="Enhanced for OCR", use_column_width=True)

    with col2:
        st.subheader("Analysis Results")
        
        # 2. Extract Text (Spinner for UX)
        with st.spinner("Reading handwriting..."):
            extracted_text = extract_text_from_image(image)
        
        st.text_area("Extracted Text (OCR)", extracted_text, height=100)

        # 3. Predict Disease
        with st.spinner("Analyzing medical data..."):
            prediction = predict_disease(image)
            
            # Logic to handle Medicine vs Disease prediction
            actual_disease = reverse_medicine_to_disease(prediction, disease_data)
            
            if actual_disease:
                final_disease = actual_disease
                st.info(f"The AI detected a medicine name: '{prediction}'\n\nThis is typically used for: {final_disease.title()}")
            else:
                final_disease = prediction
                st.success(f"Predicted Condition: {final_disease.title()}")

        # 4. Show Recommendations
        st.markdown("#### Recommended Medication Schedule")
        meds = get_medicines_for_disease(final_disease, disease_data)
        
        if meds is not None:
            st.dataframe(meds, use_container_width=True, hide_index=True)
        else:
            st.warning(f"No specific medication data found for {final_disease}.")

else:
    # Empty State
    st.markdown("""
    <div style="text-align: center; color: gray; padding: 50px;">
        <h3>Upload a prescription image to get started</h3>
        <p>This AI uses Deep Learning and Tesseract OCR to interpret medical handwriting.</p>
    </div>
    """, unsafe_allow_html=True)