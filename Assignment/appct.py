import pandas as pd
import customtkinter as ctk
from tkinter import messagebox

# -----------------------------
# Data
# -----------------------------
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

# -----------------------------
# CustomTkinter App
# -----------------------------
ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("🏥 Disease Recommendation System")
root.geometry("750x700")

# -----------------------------
# Functions
# -----------------------------
def analyze_symptoms():
    user_input = entry_symptoms.get().strip()
    if not user_input:
        messagebox.showwarning("Warning", "Please enter your symptoms!")
        return

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

    # Clear old results
    for widget in frame_results.winfo_children():
        widget.destroy()

    if results:
        top = results[0]
        lbl_main = ctk.CTkLabel(frame_results, text=f"🎯 Most Likely: {top['Disease']}", 
                                font=ctk.CTkFont(size=18, weight="bold"), text_color="green")
        lbl_main.pack(pady=(5, 0))

        ctk.CTkLabel(frame_results, text=top['Description'], wraplength=500).pack(pady=3)

        # Progress Bar
        pb_label = ctk.CTkLabel(frame_results, text=f"Match Confidence: {top['Match %']:.1f}%", text_color="blue")
        pb_label.pack()
        pb = ctk.CTkProgressBar(frame_results, width=400)
        pb.set(top['Match %'] / 100)
        pb.pack(pady=5)

        # Matched Symptoms
        ctk.CTkLabel(frame_results, text="Matched Symptoms:", font=ctk.CTkFont(weight="bold")).pack(pady=(10, 0))
        for s in sorted(top['Matched']):
            ctk.CTkLabel(frame_results, text=f"✓ {s.title()}", text_color="darkgreen").pack(anchor="w", padx=30)

        if len(results) > 1:
            ctk.CTkLabel(frame_results, text="\nOther Possible Matches:", 
                         font=ctk.CTkFont(size=14, weight="bold")).pack(pady=(10, 3))
            for r in results[1:]:
                ctk.CTkLabel(frame_results, 
                             text=f"{r['Disease']} ({r['Match %']:.1f}% match)", 
                             text_color="gray").pack()
    else:
        ctk.CTkLabel(frame_results, text="❌ No matching diseases found.", text_color="red").pack()
        ctk.CTkLabel(frame_results, 
                     text="💡 Try entering different symptoms or check available ones below.",
                     text_color="gray").pack()

def clear_fields():
    entry_symptoms.delete(0, "end")
    for widget in frame_results.winfo_children():
        widget.destroy()

def toggle_theme():
    current = ctk.get_appearance_mode()
    ctk.set_appearance_mode("dark" if current == "Light" else "light")

# -----------------------------
# Header
# -----------------------------
frame_top = ctk.CTkFrame(root)
frame_top.pack(fill="x", pady=10)

lbl_title = ctk.CTkLabel(frame_top, text="🏥 Disease Recommendation System", 
                         font=ctk.CTkFont(size=22, weight="bold"))
lbl_title.pack(side="left", padx=20, pady=10)

btn_theme = ctk.CTkButton(frame_top, text="🌓 Toggle Theme", command=toggle_theme, width=130)
btn_theme.pack(side="right", padx=10, pady=10)

# -----------------------------
# Input Section
# -----------------------------
frame_input = ctk.CTkFrame(root)
frame_input.pack(fill="x", padx=20, pady=10)

ctk.CTkLabel(frame_input, text="Enter your symptoms (comma-separated):", 
             font=ctk.CTkFont(size=13)).pack(anchor="w", padx=10, pady=(5, 2))

entry_symptoms = ctk.CTkEntry(frame_input, width=600, height=35, placeholder_text="e.g., fever, cough, headache")
entry_symptoms.pack(padx=10, pady=5)

frame_buttons = ctk.CTkFrame(frame_input, fg_color="transparent")
frame_buttons.pack(pady=5)

btn_analyze = ctk.CTkButton(frame_buttons, text="🔍 Analyze", command=analyze_symptoms, width=120)
btn_analyze.grid(row=0, column=0, padx=5)

btn_clear = ctk.CTkButton(frame_buttons, text="🗑️ Clear", command=clear_fields, fg_color="#d9534f", width=120)
btn_clear.grid(row=0, column=1, padx=5)

# -----------------------------
# Results Section
# -----------------------------
frame_results = ctk.CTkScrollableFrame(root, label_text="🧠 Diagnosis Results", width=700, height=300)
frame_results.pack(padx=20, pady=10, fill="both", expand=True)

# -----------------------------
# Available Symptoms
# -----------------------------
frame_symptoms = ctk.CTkScrollableFrame(root, label_text="📋 Available Symptoms", width=700, height=200)
frame_symptoms.pack(padx=20, pady=10, fill="both")

all_symptoms = set()
for s in df['Symptoms']:
    all_symptoms.update([x.strip().lower() for x in s.split(',')])
for sym in sorted(all_symptoms):
    ctk.CTkLabel(frame_symptoms, text=f"• {sym.title()}").pack(anchor="w", padx=15)

# -----------------------------
# Footer
# -----------------------------
ctk.CTkLabel(root, 
    text="⚕️ Note: This is for educational purposes only. Always consult a healthcare professional.",
    font=ctk.CTkFont(size=11, slant="italic"), text_color="gray").pack(pady=10)

root.mainloop()
