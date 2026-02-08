#import libraries
import pandas as pd
import string
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
#📝 Why?
#We need pandas for data, string/re for text, stopwords to remove common words.
df = pd.read_csv("df = pd.read_csv("C:/Users/Asus/OneDrive/Desktop/SHAYYU/Tweets.csv")
print(df[['text']].head())
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # remove URLs
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = ''.join([i for i in text if not i.isdigit()])
    words = text.split()
    words = [w for w in words if w not in stopwords.words('english')]
    return ' '.join(words)

#Why? Lowercase = uniform text ,Remove URL = not useful
#Remove punctuation/numbers = noise ,Remove stopwords = no meaning for ML

#apply cleaning 
df['cleaned_text'] = df['text'].apply(clean_text)
print(df[['text', 'cleaned_text']].head())

df.to_csv("cleaned_tweets.csv", index=False)
#So that we can use the cleaned data for feature extraction and modeling later.