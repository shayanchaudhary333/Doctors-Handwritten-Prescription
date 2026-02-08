# Imports
import numpy as np
import pandas as pd
from tkinter import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from deep_translator import GoogleTranslator

# Load and prepare data
data = pd.read_csv("language.csv")
x = np.array(data['Text'])
y = np.array(data['language'])

cv = CountVectorizer()
x = cv.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
model = MultinomialNB()
model.fit(x_train, y_train)

# Define target translation languages
target_languages = {
    'en': 'English',
    'hi': 'Hindi',
    'fr': 'French',
    'es': 'Spanish',
    'bn': 'Bengali',
    'zh-CN': 'Chinese (Simplified)',
    'ar': 'Arabic',
    'ru': 'Russian'
}

# Function to run on button click
def detect_translate():
    user_input = text_entry.get()
    if not user_input.strip():
        output_label.config(text="❗ Please enter a sentence.")
        return
    
    input_vector = cv.transform([user_input])
    predicted_lang = model.predict(input_vector)[0]

    result = f"Detected Language: {predicted_lang}\n\nTranslations:\n"

    for code, lang in target_languages.items():
        try:
            translated = GoogleTranslator(source='auto', target=code).translate(user_input)
            result += f"{lang}: {translated}\n\n"

        except Exception as e:
            result += f"{lang} ({code}): Translation failed\n"

    output_label.config(text=result)

# GUI

root = Tk()
root.title("Language Detection & Translation")
root.geometry("650x550")

Label(root, text="Enter Text Below:", font=("Arial", 14)).pack(pady=10)
text_entry = Entry(root, font=("Arial", 14), width=60)
text_entry.pack(pady=5)

Button(root, text="Detect & Translate", font=("Arial", 12), command=detect_translate).pack(pady=10)

output_label = Label(root, text="", font=("Arial", 12), justify=LEFT, wraplength=600)
output_label.pack(pady=20)

root.mainloop()
