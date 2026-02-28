import streamlit as st
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

st.set_page_config(page_title="Bhavit Smart AI", layout="centered")
st.title("🤖 Bhavit Smart AI")

# Load dataset
def load_data():
    questions = []
    answers = []
    
    with open("data.txt", "r", encoding="utf-8") as file:
        for line in file:
            if ":" in line:
                q, a = line.strip().split(":", 1)
                questions.append(q.strip())
                answers.append(a.strip())
    
    return questions, answers

questions, answers = load_data()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

def get_response(user_input):
    user_vec = vectorizer.transform([user_input])
    similarity = cosine_similarity(user_vec, X)
    index = np.argmax(similarity)
    
    if similarity[0][index] < 0.3:
        return "I don't understand yet. Teach me more!"
    
    return answers[index]

# Display old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)

    reply = get_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    
    with st.chat_message("assistant"):
        st.write(reply)
