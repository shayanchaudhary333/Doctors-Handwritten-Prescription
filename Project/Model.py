# ================= IMAGE MODEL PREP AND TRAINING ===================
import os
import cv2
import pandas as pd

# ==== DATA CLEANING ====
image_folder = r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\Doctors Handwritten Prescription BD dataset\Training\training_words"
csv_path = r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\Doctors Handwritten Prescription BD dataset\Training\training_labels.csv"
clean_csv_path = r"C:\Users\Asus\OneDrive\Desktop\SHAYYU\Project\Doctors Handwritten Prescription BD dataset\Training\training_labels_cleaned.csv"

df = pd.read_csv(csv_path)
df = df.dropna(subset=['IMAGE', 'MEDICINE_NAME'])
df['IMAGE'] = df['IMAGE'].astype(str).str.strip()
df['MEDICINE_NAME'] = df['MEDICINE_NAME'].astype(str).str.strip()
df = df.drop_duplicates(subset=['IMAGE', 'MEDICINE_NAME'])

missing_images = []
corrupt_images = []
good_rows = []
for _, row in df.iterrows():
    img_file = row['IMAGE']
    img_path = os.path.join(image_folder, img_file)
    if not os.path.isfile(img_path):
        missing_images.append(img_file)
        continue
    img = cv2.imread(img_path)
    if img is None or img.size == 0:
        corrupt_images.append(img_file)
        continue
    good_rows.append(row)
clean_df = pd.DataFrame(good_rows)
clean_df.to_csv(clean_csv_path, index=False)
print(f"✅ Cleaned CSV saved as: {clean_csv_path}")
print(f"🟢 Valid entries: {len(clean_df)}")
if missing_images: print(f"⚠ Missing images: {missing_images}")
if corrupt_images: print(f"⚠ Corrupt or unreadable images: {corrupt_images}")

# ===================== MODEL TRAINING ============================
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.utils.class_weight import compute_class_weight
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, GlobalAveragePooling2D, Input
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input

label_csv = clean_csv_path
IMG_SIZE = 224

labels_df = pd.read_csv(label_csv)
labels_df.dropna(inplace=True)

data = []
labels = []
for _, row in labels_df.iterrows():
    img_path = os.path.join(image_folder, str(row['IMAGE']))
    if os.path.exists(img_path):
        img = cv2.imread(img_path)
        if img is None or img.size == 0:
            continue
        img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
        img = preprocess_input(img.astype('float32'))
        data.append(img)
        labels.append(row['MEDICINE_NAME'])
X = np.array(data)
y = np.array(labels)
print(f"Loaded {len(X)} images.")

label_enc = LabelEncoder()
y_encoded = label_enc.fit_transform(y)
y_cat = to_categorical(y_encoded)

X_train, X_test, y_train, y_test = train_test_split(
    X, y_cat, test_size=0.2, random_state=42, stratify=y_cat
)

class_weights = compute_class_weight('balanced', classes=np.unique(y_encoded), y=y_encoded)
class_weights = dict(enumerate(class_weights))

datagen = ImageDataGenerator(
    rotation_range=20,
    zoom_range=0.2,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)
datagen.fit(X_train)

base_model = EfficientNetB0(include_top=False, input_shape=(IMG_SIZE, IMG_SIZE, 3), weights='imagenet')
base_model.trainable = False

model = Sequential([
    Input(shape=(IMG_SIZE, IMG_SIZE, 3)),
    base_model,
    GlobalAveragePooling2D(),
    Dropout(0.4),
    Dense(256, activation='relu'),
    Dropout(0.3),
    Dense(y_cat.shape[1], activation='softmax')
])

model.compile(optimizer=Adam(learning_rate=0.0005),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

checkpoint = ModelCheckpoint("best_prescription_model.h5", monitor='val_accuracy', save_best_only=True, mode='max')
early_stop = EarlyStopping(monitor='val_accuracy', patience=8, restore_best_weights=True)

history = model.fit(
    datagen.flow(X_train, y_train, batch_size=32),
    epochs=50,
    validation_data=(X_test, y_test),
    class_weight=class_weights,
    callbacks=[checkpoint, early_stop]
)

loss, acc = model.evaluate(X_test, y_test)
print(f"\nFinal Test Accuracy: {acc*100:.2f}%")

plt.figure(figsize=(8,5))
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("accuracy_graph.png")
plt.show()

# ================== OPTIONAL - NLP SUGGESTION BLOCK (for text queries) =========
# Paste this block if, in future, you want a tokenized, vectorized symptom/disease text matcher.
# It runs fully separately from your image-based classifier.

"""
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('punkt')

disease_df = pd.read_csv('disease_data.csv')
disease_df['Tokens'] = disease_df['disease'].apply(lambda x: " ".join(word_tokenize(str(x).lower())))
vectorizer = CountVectorizer().fit(disease_df['Tokens'])

def recommend_nlp(query):
    tokens = " ".join(word_tokenize(str(query).lower()))
    user_vec = vectorizer.transform([tokens])
    disease_vecs = vectorizer.transform(disease_df['Tokens'])
    sim = cosine_similarity(user_vec, disease_vecs)[0]
    idx = sim.argmax()
    if sim.max() > 0.3:
        row = disease_df.iloc[idx]
        return f"Medicine: {row['medicine']} | Dose: {row['dose']} | Time: {row['time']}"
    else:
        return "No suitable match found."
"""
print(labels_df['MEDICINE_NAME'].value_counts())

datagen = ImageDataGenerator(
    rotation_range=30,
    zoom_range=0.3,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.15,
    horizontal_flip=True,
    fill_mode='nearest'
)

base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

# Re-compile with a lower LR
model.compile(optimizer=Adam(learning_rate=1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Re-train for 5–15 more epochs on your data (with early stopping)
history_ft = model.fit(
    datagen.flow(X_train, y_train, batch_size=32),
    epochs=15,
    validation_data=(X_test, y_test),
    class_weight=class_weights,
    callbacks=[early_stop]
)
