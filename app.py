import streamlit as st
from transformers import pipeline

# Chatbot pipeline load kar rahe hain
chatbot = pipeline("text-generation", model="distilgpt2")

# Streamlit title & caption
st.title("💬 UjjawalGPT – Tumhara Apna Desi AI Dost 🇮🇳")
st.caption("Desi style chatbot – Hinglish me puchho, reply milega!")

# User input
user_input = st.text_input("Bhai kuch bhi puchho:")

# Response logic
if user_input:
    if "naam" in user_input.lower():
        st.write("Mera naam UjjawalGPT hai 😎")
    elif "kisne banaya" in user_input.lower():
        st.write("Ujjawal Mishra ne banaya mujhe – Desi Chatbot! 💥")
    else:
        response = chatbot(user_input, max_length=60, do_sample=True, top_k=40, top_p=0.9)[0]['generated_text']
        st.write(response[len(user_input):]
