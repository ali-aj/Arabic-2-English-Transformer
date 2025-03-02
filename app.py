import streamlit as st
import torch
from models.model_loader import load_resources, translate

# Page configuration
st.set_page_config(
    page_title="Arabic to English Translator",
    page_icon="🌍",
    layout="centered"
)

# Enhanced Custom CSS
st.markdown("""
<style>
    /* Main styling */
    .main-header {
        font-family: 'Arial', sans-serif;
        color: #2c3e50;
        padding-bottom: 10px;
        border-bottom: 2px solid #4CAF50;
        margin-bottom: 20px;
    }
    
    /* Input and button styling */
    .stTextArea label, .stButton>button {
        font-size: 1.2rem;
    }
    .stButton>button {
        background-color: #2c3e50;
        color: white;
        font-weight: bold;
        padding: 10px 25px;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1a252f;
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    
    /* Output container styling */
    .output-container {
        background-color: #f8f9fa;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    
    /* Footer styling */
    .footer {
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e0e0e0;
        text-align: center;
        color: #666;
    }
    
    /* Creator profiles */
    .creator-profiles {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 10px;
    }
    .creator-profile {
        text-align: center;
    }
    .linkedin-button {
        display: inline-block;
        background-color: #0077B5;
        color: white !important;
        text-decoration: none;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8rem;
        margin-top: 5px;
        transition: background-color 0.3s;
    }
    .linkedin-button:hover {
        background-color: #005582;
    }
    
    /* Language badges */
    .language-badge {
        background-color: #f1f1f1;
        color: #333;
        padding: 5px 10px;
        border-radius: 15px;
        margin-right: 5px;
        font-size: 0.9em;
    }
    .ar-badge {
        background-color: #4CAF50;
        color: white;
    }
    .en-badge {
        background-color: #2196F3;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# App header with animated icon
st.markdown("<h1 class='main-header'>🌍 Arabic to English Translator</h1>", unsafe_allow_html=True)
st.markdown("<p>Translate Arabic text to English using an advanced neural machine translation model.</p>", unsafe_allow_html=True)

# Sidebar information with improved formatting
with st.sidebar:
    st.markdown("### About this App")
    st.markdown("""
    This application uses a Transformer-based neural network model specifically 
    trained on Arabic-English parallel corpus to provide accurate translations.
    """)
    
    st.divider()
    
    st.markdown("### How to Use")
    st.markdown("""
    1. Type or paste Arabic text in the input area
    2. Click the 'Translate' button
    3. View the English translation in the output section
    """)
    
    st.divider()
    
    st.markdown("### Model Architecture")
    st.markdown("""
    - **Model Type**: Transformer
    - **Encoder-Decoder**: 4-layer architecture
    - **Attention Heads**: 8
    - **Model Dimension**: 512
    """)

# Load the model and resources (cached to prevent reloading)
@st.cache_resource
def load_translation_resources():
    with st.spinner("Loading translation model..."):
        try:
            return load_resources()
        except Exception as e:
            st.error(f"Error loading model: {str(e)}")
            return None

# Load resources
resources = load_translation_resources()

if resources:
    model, src_tokenizer, tgt_tokenizer, device = resources
    
    # Visual language indicator
    st.markdown("""
    <div style="display: flex; gap: 10px; margin-bottom: 15px;">
        <span class="language-badge ar-badge">Arabic</span>
        <span>➡️</span>
        <span class="language-badge en-badge">English</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Input text area for Arabic text with placeholder
    arabic_text = st.text_area(
        "Enter Arabic text to translate:", 
        placeholder="اكتب النص العربي هنا", 
        height=150
    )
    
    # Improved button layout
    col1, col2, col3 = st.columns([2, 1, 4])
    with col1:
        translate_button = st.button("Translate")
    with col2:
        clear_button = st.button("Clear")
    
    if clear_button:
        st.session_state.arabic_text = ""
        st.session_state.translation = None
        st.rerun()
    
    if translate_button and arabic_text:
        with st.spinner("Translating..."):
            try:
                # Translate the text using the function
                english_translation = translate(model, arabic_text, src_tokenizer, tgt_tokenizer, device)
                
                # Store in session state
                st.session_state.translation = english_translation
            except Exception as e:
                st.error(f"Translation error: {str(e)}")
    
    # Display translation result if available with improved styling
    if 'translation' in st.session_state and st.session_state.translation:
        st.markdown("<div class='output-container'>", unsafe_allow_html=True)
        st.markdown("### Translation Result")
        st.markdown(f"<p style='font-size: 1.2rem; font-weight: 500;'>{st.session_state.translation}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.error("Failed to load translation model. Please check the console for errors.")

# Footer with developer credits
st.markdown("""
<div class="footer">
    <p>Developed by:</p>
    <div class="creator-profiles">
        <div class="creator-profile">
            <p><strong>Ali Mustafa</strong></p>
            <a href="https://www.linkedin.com/in/alii-mustafa-" class="linkedin-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg> LinkedIn
            </a>
        </div>
        <div class="creator-profile">
            <p><strong>Fasih Zaidi</strong></p>
            <a href="https://www.linkedin.com/in/syed-fasih-zaidi-60643a255/" class="linkedin-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg> LinkedIn
            </a>
        </div>
    </div>
    <p style="margin-top: 20px; font-size: 0.8rem;">© 2025 Arabic-English Neural Machine Translation</p>
</div>
""", unsafe_allow_html=True)
