import streamlit as st
from models.model_loader import ModelLoader
from utils.preprocessing import clean_text, tokenize_text
from utils.translation import translate

# Load the translation model
# model_loader = ModelLoader()
# model = model_loader.load_model()

# Streamlit application title
st.title("Arabic to English Translator")

# Input text area for Arabic text
arabic_text = st.text_area("Enter Arabic text here:")

if st.button("Translate"):
    if arabic_text:
        # Preprocess the input text
        cleaned_text = clean_text(arabic_text)
        tokenized_text = tokenize_text(cleaned_text)

        # Translate the text
        # english_translation = translate(tokenized_text, model)

        # Display the translated text
        st.subheader("Translated English Text:")
        # st.write(english_translation)
    else:
        st.error("Please enter some Arabic text to translate.")