import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="OM", page_icon="🌌", layout="wide")

st.markdown("""
<style>
    .main { background-color: #0a0a0a; color: #ffffff; }
    .om-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #4b0082, #8a2be2);
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
    }
    .om-name { font-size: 4.8rem; font-weight: bold; text-shadow: 0 0 30px rgba(138, 43, 226, 0.9); }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="om-header">
    <div class="om-name">OM</div>
    <p>Your Personal Cosmic AI Companion</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("OM Settings")
    provider = st.selectbox("AI Provider", ["Grok (xAI)", "OpenAI", "Ollama"])
    if provider == "Grok (xAI)":
        api_key = st.text_input("Grok API Key", type="password")
    elif provider == "OpenAI":
        api_key = st.text_input("OpenAI API Key", type="password")

st.write("### Welcome to OM 🌌")
st.write("Your personal AI assistant is ready!")
st.info("Please create the file correctly and try again.")

st.caption("OM - Personal AI Assistant")