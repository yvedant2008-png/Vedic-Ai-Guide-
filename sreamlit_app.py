import streamlit as st
from google import genai

st.title("Vedic AI Guide")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Ask me about Vedas, Upanishads, or spirituality...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.write(user_input)

    prompt = f"""
You are Vedic AI Guide.
Answer in simple language.
Use Vedic, Upanishadic, and Bhagavad Gita concepts when relevant.
Do not fake shlokas. If unsure, say you are unsure.

User question: {user_input}
"""

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    bot_reply = response.text

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    with st.chat_message("assistant"):
        st.write(bot_reply)
