# import pandas as pd

# csv_path = r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\disease_data.csv"

# try:
#     df = pd.read_csv(csv_path)
#     print("✅ File loaded successfully!")
#     print(df.head())
# except FileNotFoundError:
#     print(f"❌ File not found at: {csv_path}")

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import pickle

# ✅ Load your CSV
df = pd.read_csv(r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\disease_data.csv")

# ✅ Encode 'disease' column (Input)
le_disease = LabelEncoder()
df['disease_encoded'] = le_disease.fit_transform(df['disease'])

# ✅ Encode 'medicine' column (Output)
le_medicine = LabelEncoder()
df['medicine_encoded'] = le_medicine.fit_transform(df['medicine'])

# ✅ Prepare features (X) and labels (y)
X = df[['disease_encoded']].values
y = to_categorical(df['medicine_encoded'])

# ✅ Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ✅ Dummy model
model = Sequential()
model.add(Dense(16, activation='relu', input_shape=(1,)))
model.add(Dense(16, activation='relu'))
model.add(Dense(y.shape[1], activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
#model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# #✅ Define dummy model
# model = Sequential()
# model.add(Dense(16, activation='relu', input_shape=(1,)))
# model.add(Dense(16, activation='relu'))
# model.add(Dense(len(np.unique(y)), activation='softmax'))  # output classes = # of unique medicines

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])


# ✅ Train model
model.fit(X_train, y_train, epochs=30, verbose=1)

# ✅ Save model
model.save(r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\model.h5")

# ✅ Save label encoder
with open(r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\label_encoder.pkl", "wb") as f:
    pickle.dump(le_medicine, f)

print("✅ Dummy model and label encoder saved successfully.")

print(model.input_shape)
def predict_disease(image):
    # Resize and grayscale
    image = cv2.resize(image, (128, 128))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract a single numeric feature (example: mean pixel intensity)
    feature = np.mean(gray)

    # Prepare input for model: shape (1, 1)
    input_data = np.array([[feature]], dtype=np.float32)

    prediction = model.predict(input_data)
    predicted_class = label_encoder.inverse_transform([np.argmax(prediction)])
    return predicted_class[0]

with open(r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\label_encoder.pkl", "rb") as file:
    label_encoder = pickle.load(file)
