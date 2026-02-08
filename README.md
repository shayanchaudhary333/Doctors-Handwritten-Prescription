# 💊 Smart Prescription Digitizer

An AI-powered web application that translates handwritten medical prescriptions into structured digital records.

## 🚀 Features
* **OCR (Optical Character Recognition):** Extracts text from handwritten prescription images using Tesseract.
* **AI Prediction:** Uses a Deep Learning (CNN) model to identify the medicine/disease from handwriting.
* **Smart Recommendations:** Automatically suggests the correct dosage and medicine schedule based on the prediction.
* **User-Friendly Interface:** Built with Streamlit for a clean and responsive UI.

## 🛠️ Tech Stack
* **Python** (Core Logic)
* **Streamlit** (Frontend)
* **TensorFlow/Keras** (Deep Learning Model)
* **Tesseract OCR** (Text Extraction)
* **Pandas & NumPy** (Data Handling)

## 📸 How It Works
1.  Upload an image of a handwritten prescription.
2.  The app preprocesses the image (denoising & thresholding).
3.  The **CNN Model** predicts the disease or medicine name.
4.  The system displays the digitized text and the recommended medication schedule.

---
*Created by Shayan*
