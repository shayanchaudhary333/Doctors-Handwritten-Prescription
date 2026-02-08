import streamlit as st
import pytesseract
from PIL import Image
import spacy
import re
import pandas as pd

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Extraction function (same logic as before)
def extract_medicine_info(text):
    dosage_pattern = re.compile(r'\b\d{1,4}\s?(mg|ml|tablet|tablets|capsule|capsules)\b', re.I)
    freq_pattern = re.compile(r'\b(once daily|twice daily|3 times daily|TID|BID|q\d+h|every \d+ hours)\b', re.I)
    doc = nlp(text)
    medicines = []
    dosages = []
    frequencies = []
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.lower()
        if any(word in chunk_text for word in ["tablet", "capsule"]) or chunk.root.ent_type_ == "DRUG":
            medicines.append(chunk.text.strip())
            after_chunk = text[chunk.end_char:]
            dosage_match = dosage_pattern.search(after_chunk)
            freq_match = freq_pattern.search(after_chunk)
            dosages.append(dosage_match.group() if dosage_match else "")
            frequencies.append(freq_match.group() if freq_match else "")
    df = pd.DataFrame({
        "Medicine Name": medicines,
        "Dosage": dosages,
        "Frequency": frequencies
    })
    return df

# Streamlit App
st.title("Prescription to Medicine List Extractor")
st.write(
    "Upload a scanned doctor’s prescription image. The app will extract the text using OCR, "
    "then use simple NLP to detect medicines, their dosages, and frequency."
)

uploaded_file = st.file_uploader("Upload Prescription Image (JPG/PNG)", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Prescription", use_column_width=True)

    # OCR
    ocr_result = pytesseract.image_to_string(img, lang='eng')
    st.subheader("Extracted Text")
    st.text_area("OCR Output", value=ocr_result, height=200)

    # NLP Extraction
    medicine_df = extract_medicine_info(ocr_result)

    st.subheader("Extracted Medicine List")
    st.write(medicine_df)
else:
    st.warning("Please upload a prescription image.")

