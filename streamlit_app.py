
import streamlit as st
import random

st.set_page_config(page_title="Bhavit Mini AI", layout="centered")

st.title("🤖 Bhavit Mini AI")
st.write("Simple Local Chatbot (Lightweight Version)")

# Store conversation in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Simple response logic
def generate_response(user_input):
    responses = [
        "Interesting! Tell me more.",
        "Why do you think that?",
        "That sounds cool!",
        "I understand.",
        "Can you explain more?",
        "That's nice to hear!"
    ]
    
    if "hello" in user_input.lower():
        return "Hello Bhavit! 👋"
    elif "how are you" in user_input.lower():
        return "I am just a small AI running on your laptop 😄"
    elif "flask" in user_input.lower():
        return "Ah yes, you like Flask development!"
    else:
        return random.choice(responses)

# Show previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.write(user_input)

    # Generate response
    reply = generate_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})

    with st.chat_message("assistant"):
        st.write(reply)
