# 🤖 CodeAlpha FAQ Chatbot

A smart chatbot that answers frequently asked questions using Natural Language Processing (NLP). Built using Python and Streamlit, this bot was created as part of the CodeAlpha Internship Program to demonstrate real-time query resolution with simplicity and effectiveness.

---

## 🚀 Features

- ✅ Automatically answers common questions
- 🧠 Uses TF-IDF and cosine similarity for matching
- 🔠 Text preprocessing with NLTK (tokenization, stopword removal, etc.)
- 🌐 Clean and simple web interface built with Streamlit
- 📂 Easily expandable via `faq_data.json`

---

## 🛠 Tech Stack

- Python
- Streamlit
- NLTK
- scikit-learn (Sklearn)

---

## 📁 Folder Structure

📦 CodeAlpha_Chatbot
┣ 📜 chatbot.py
┣ 📜 chatbot_ui.py
┣ 📜 faq_data.json
┣ 📜 requirements.txt
┗ 📜 README.md


---
## ⚙️ Setup & Run Instructions
Step 1: Clone the Repository
bash
git clone https://github.com/Stellarlaunch/CodeAlpha_Chatbot.git
cd CodeAlpha_Chatbot

Step 2: Install Dependencies
bash
pip install -r requirements.txt

Step 3: Run the Chatbot UI
bash
streamlit run chatbot_ui.py

---

📌 How It Works
Loads FAQs from faq_data.json

Cleans and tokenizes the questions

Converts questions into TF-IDF vectors

Compares user query with stored questions using cosine similarity

Returns the most relevant answer or a fallback response

---

🖼️ UI Preview
![FAQchatbot](https://github.com/Stellarlaunch/CodeAlpha_Chatbot/blob/fedb33e9cceba44a02b7f8b8c3c03bc0226ed1bb/CodeAlpha_chatbot.jpg)

---

✍️ Created By
Dhiraj Musale
Intern at CodeAlpha
GitHub: @Stellarlaunch
