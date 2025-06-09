import streamlit as st
import nltk
import json
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK resources (only once)
nltk.download('punkt')
nltk.download('stopwords')

# Load FAQ data from JSON file
with open('faq_data.json', 'r') as f:
    faqs = json.load(f)

# Preprocessing function
def preprocess(text):
    tokens = word_tokenize(text.lower())
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return " ".join(tokens)

# Preprocess all questions
questions = list(faqs.keys())
preprocessed_questions = [preprocess(q) for q in questions]

# Vectorize questions
vectorizer = TfidfVectorizer().fit(preprocessed_questions)
faq_vectors = vectorizer.transform(preprocessed_questions)

# Streamlit UI setup
st.set_page_config(page_title="FAQ Chatbot 💬", page_icon="🤖")
st.title("🤖 FAQ Chatbot")
st.markdown("Ask me anything related to electric vehicles, e-commerce policies, or internships!")

# User input
user_question = st.text_input("Ask a question:")

if st.button("Get Answer"):
    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:
        user_input = preprocess(user_question)
        input_vector = vectorizer.transform([user_input])
        similarities = cosine_similarity(input_vector, faq_vectors)
        max_index = similarities.argmax()
        max_score = similarities[0][max_index]

        if max_score > 0.2:
            response = list(faqs.values())[max_index]
            st.success("Answer:")
            st.write(response)
        else:
            st.error("Sorry, I couldn't find a relevant answer.")
