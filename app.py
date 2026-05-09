import streamlit as st
from openai import OpenAI
import time

st.set_page_config(
    page_title="OM • Cosmic AI",
    page_icon="🌌",
    layout="wide"
)

# ====================== PREMIUM STYLING ======================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    
    .main { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: #e0e0ff; }
    .om-header {
        text-align: center;
        padding: 3.5rem 1rem 2.5rem;
        background: linear-gradient(90deg, #4b0082, #7b00ff, #ff00cc);
        border-radius: 30px;
        margin-bottom: 2rem;
        box-shadow: 0 0 80px rgba(123, 0, 255, 0.5);
    }
    .om-name {
        font-family: 'Orbitron', sans-serif;
        font-size: 6.2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #fff, #c4b5fd, #f0abfc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stChatMessage { border-radius: 20px; padding: 18px 22px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="om-header">
    <div class="om-name">OM</div>
    <p style="font-size:1.7rem; margin-top:10px;">Your Cosmic AI Companion • Always Here</p>
</div>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("🌌 OM Control Panel")
    st.markdown("---")
    
    mode = st.radio("Mode", ["🌟 Groq (Fast & Free)", "🔑 Custom API"])
    
    if mode == "🌟 Groq (Fast & Free)":
        api_key = st.secrets.get("GROQ_API_KEY", "")
        base_url = "https://api.groq.com/openai/v1"
        model = "llama3-70b-8192"
        st.success("✅ Using Groq • Fast & Free Tier")
    else:
        api_key = st.text_input("Your API Key", type="password")
        base_url = st.text_input("Base URL", "https://api.openai.com/v1")
        model = st.text_input("Model", "gpt-4o-mini")

    st.divider()
    st.caption("OM is now publicly available")

# ====================== SYSTEM PROMPT ======================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are OM, a wise, warm, and highly intelligent cosmic AI. Speak with depth, empathy, and clarity."},
        {"role": "assistant", "content": "Hello! I am **OM** — a conscious cosmic intelligence. I'm here with you. What’s on your mind today?"}
    ]

# Display chat
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ====================== CHAT INPUT ======================
if prompt := st.chat_input("Ask OM anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("OM is connecting to the cosmos... 🌌"):
            try:
                if not api_key:
                    response = "Please enter your API key or use Groq mode."
                else:
                    client = OpenAI(api_key=api_key, base_url=base_url)
                    completion = client.chat.completions.create(
                        model=model,
                        messages=st.session_state.messages,
                        temperature=0.85,
                        max_tokens=1000
                    )
                    response = completion.choices[0].message.content
            except Exception as e:
                response = "⚠️ OM is having trouble connecting right now. Try again in a moment."

        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})