import streamlit as st
import google.generativeai as genai

st.title("Flavour Fusion: AI Recipe Generator")

topic = st.text_input("Enter Recipe Topic:")
word_count = st.slider("Select Word Count:", 200, 1500, 500)

if st.button("Generate Recipe"):
    st.write("Generating recipe...")  # Placeholder
    # Call AI API here
