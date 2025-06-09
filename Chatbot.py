import nltk
import numpy as np
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import json

# Load FAQ data from JSON
with open('faq_data.json', 'r') as f:
    faqs = json.load(f)

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# ---------------- PREPROCESSING ----------------
def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    return " ".join(tokens)

# Preprocess questions
preprocessed_questions = [preprocess(q) for q in faqs.keys()]

# Vectorize questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(preprocessed_questions)

# ---------------- CHATBOT FUNCTION ----------------
def get_response(user_input):
    user_input_processed = preprocess(user_input)
    user_vec = vectorizer.transform([user_input_processed])
    similarities = cosine_similarity(user_vec, X)
    idx = np.argmax(similarities)
    if similarities[0][idx] < 0.2:
        return "Sorry, I don't understand that question."
    return list(faqs.values())[idx]

# ---------------- MAIN LOOP ----------------
if __name__ == "__main__":
    print("Welcome to the FAQ Chatbot! Type 'exit' to quit.")
    while True:
        user_question = input("You: ")
        if user_question.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_response(user_question)
        print("Bot:", response)
