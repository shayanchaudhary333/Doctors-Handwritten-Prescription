import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.tokenize import word_tokenize
from io import StringIO

# Ensure 'punkt' is downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

csv_data = """Disease,Medicine,Dosage,Time
Fever,Paracetamol,500mg,Thrice a day after food
Headache,Aspirin,300mg,Once in the morning
Cold,Cetrizine,10mg,Once before sleep
Cough,Bromhexine,5ml,Thrice daily
Body Pain,Ibuprofen,400mg,Twice a day
Diabetes,Metformin,500mg,Twice after meals
Hypertension,Amlodipine,5mg,Once daily in morning
Thyroid,Thyronorm,50mcg,Empty stomach daily
Acidity,Omeprazole,20mg,Once before breakfast
Vomiting,Ondansetron,4mg,Before meals
"""

df = pd.read_csv(StringIO(csv_data))
df['Tokens'] = df['Disease'].apply(lambda x: " ".join(word_tokenize(str(x).lower())))
vectorizer = CountVectorizer().fit(df['Tokens'])

def recommend_prescription(user_input):
    input_tokens = " ".join(word_tokenize(str(user_input).lower()))
    user_vec = vectorizer.transform([input_tokens])
    disease_vecs = vectorizer.transform(df['Tokens'])
    similarity = cosine_similarity(user_vec, disease_vecs)[0]

    if similarity.max() > 0.3:
        idx = similarity.argmax()
        row = df.iloc[idx]
        return (
            f"**Disease:** {row['Disease']}  \n"
            f"**Medicine:** {row['Medicine']}  \n"
            f"**Dosage:** {row['Dosage']}  \n"
            f"**Time:** {row['Time']}"
        )
    else:
        return "❌ No suitable match found. Please rephrase your symptoms."

st.set_page_config(page_title="AI Medicine Recognition & Advice", layout="centered")
st.title("💊 AI Medicine Recognition & Advice")
st.markdown("Enter your symptoms or disease name below to get a suggested prescription:")

user_input = st.text_input("Symptoms / Disease", "")
if st.button("Get Prescription"):
    if not user_input.strip():
        st.warning("Please enter your symptoms or condition.")
    else:
        result = recommend_prescription(user_input)
        if result.startswith("❌"):
            st.error(result)
        else:
            st.success(result)
