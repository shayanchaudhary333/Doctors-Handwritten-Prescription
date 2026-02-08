import streamlit as st
import pandas as pd

# -----------------------------------
# Data Setup
# -----------------------------------
data = {
    'Disease': ['Flu', 'Cold', 'Chickenpox', 'Malaria', 'Dengue'],
    'Symptoms': [
        'fever, cough, sore throat, runny nose, muscle pain',
        'sneezing, runny nose, sore throat, coughing',
        'fever, rash, tiredness, loss of appetite',
        'fever, chills, muscle pain, headache, sweating',
        'fever, headache, muscle pain, rash'
    ],
    'Description': [
        'A viral infection affecting the respiratory system.',
        'A mild viral infection of the nose and throat.',
        'A highly contagious viral infection causing an itchy rash.',
        'A mosquito-borne disease caused by parasites.',
        'A mosquito-borne viral infection.'
    ]
}
df = pd.DataFrame(data)

# -----------------------------------
# Streamlit Page Setup
# -----------------------------------
st.set_page_config(
    page_title="🏥 Disease Recommendation System",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# Custom CSS for style
# -----------------------------------
st.markdown("""
    <style>
    .main {
        background-color: #f7faff;
    }
    .title {
        color: #1f77b4;
        text-align: center;
        font-weight: bold;
        font-size: 2.2em;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #555;
        margin-bottom: 30px;
    }
    .result-box {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    .metric-box {
        background-color: #e8f4fd;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------
# Title Section
# -----------------------------------
st.markdown('<div class="title">🏥 Disease Recommendation System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Identify possible diseases based on your symptoms</div>', unsafe_allow_html=True)
st.markdown("---")

# -----------------------------------
# Sidebar Section
# -----------------------------------
with st.sidebar:
    st.header("ℹ️ About")
    st.write("This system helps identify possible diseases based on your entered symptoms.")
    st.warning("⚠️ Educational use only — Always consult a doctor for actual diagnosis.")
    st.markdown("---")

    st.subheader("📋 Available Symptoms")
    all_symptoms = set()
    for s in df['Symptoms']:
        all_symptoms.update([x.strip().lower() for x in s.split(',')])
    for sym in sorted(all_symptoms):
        st.write(f"• {sym.title()}")

# -----------------------------------
# Input Section
# -----------------------------------
st.subheader("🧠 Enter Your Symptoms")
user_input = st.text_input(
    "Type your symptoms separated by commas",
    placeholder="e.g., fever, cough, headache",
)

analyze = st.button("🔍 Analyze Symptoms", use_container_width=True, type="primary")

# -----------------------------------
# Logic Section
# -----------------------------------
if analyze:
    if not user_input.strip():
        st.warning("⚠️ Please enter your symptoms to get results.")
    else:
        user_symptoms = set([s.strip().lower() for s in user_input.split(',')])
        results = []

        for _, row in df.iterrows():
            disease_symptoms = set([s.strip().lower() for s in row['Symptoms'].split(',')])
            matches = len(user_symptoms.intersection(disease_symptoms))
            match_percentage = (matches / len(disease_symptoms)) * 100 if matches > 0 else 0

            if matches > 0:
                results.append({
                    'Disease': row['Disease'],
                    'Description': row['Description'],
                    'Matches': matches,
                    'Total': len(disease_symptoms),
                    'Match %': match_percentage,
                    'Matched': user_symptoms.intersection(disease_symptoms)
                })

        results.sort(key=lambda x: (x['Matches'], x['Match %']), reverse=True)

        st.markdown("---")

        if results:
            top = results[0]
            st.success(f"🎯 **Most Likely Disease:** {top['Disease']}")
            st.write(top['Description'])

            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Matched Symptoms", f"{top['Matches']}/{top['Total']}")
            with col2:
                st.metric("Match Percentage", f"{top['Match %']:.1f}%")
            with col3:
                confidence = "⭐" * min(3, top["Matches"])
                st.metric("Confidence", confidence)

            st.progress(top["Match %"] / 100)

            with st.expander("🔎 View Matched Symptoms"):
                for s in sorted(top['Matched']):
                    st.write(f"✅ {s.title()}")

            if len(results) > 1:
                st.markdown("### 🩺 Other Possible Matches")
                for r in results[1:]:
                    with st.expander(f"{r['Disease']} ({r['Match %']:.1f}% match)"):
                        st.write(f"**Description:** {r['Description']}")
                        st.write(f"**Matched Symptoms:** {', '.join([s.title() for s in r['Matched']])}")
        else:
            st.error("❌ No matching diseases found.")
            st.info("💡 Try different symptoms or check the sidebar for available ones.")

st.markdown("---")
st.caption("⚕️ *This tool is for educational use only and not a medical diagnosis tool.*")
