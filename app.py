import streamlit as st
from dotenv import load_dotenv
import os
import pyttsx3

# Load environment variables (API keys)
load_dotenv()

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="OM - Your AI Companion",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CUSTOM STYLING ======================
st.markdown("""
<style>
    .main { background-color: #0a0a0a; color: #f0f0f0; }
    .om-header {
        text-align: center;
        padding: 2.5rem 0;
        background: linear-gradient(90deg, #4b0082, #8a2be2, #ff69b4);
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(138, 43, 226, 0.3);
    }
    .om-name {
        font-size: 4.8rem;
        font-weight: bold;
        text-shadow: 0 0 40px rgba(138, 43, 226, 0.8);
        margin: 0;
    }
    .stChatMessage {
        border-radius: 18px;
        padding: 14px 18px;
    }
</style>
""", unsafe_allow_html=True)

# ====================== HEADER ======================
st.markdown("""
<div class="om-header">
    <div class="om-name">OM</div>
    <p style="font-size:1.4rem; margin-top:10px;">Your Personal Cosmic AI Companion 🌌</p>
</div>
""", unsafe_allow_html=True)

# ====================== DEPRESSION SUPPORT ======================
depression_keywords = [
    "depressed", "depression", "suicidal", "kill myself", "want to die", 
    "hopeless", "worthless", "no reason to live", "end it all"
]

def is_depression_related(text):
    if not text:
        return False
    return any(word in text.lower() for word in depression_keywords)

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("⚙️ OM Settings")
    st.caption("Made with ❤️ for you")
    
    provider = st.selectbox(
        "Choose AI Brain", 
        ["Grok (xAI)", "OpenAI", "Ollama (Local)"]
    )
    
    if provider == "Grok (xAI)":
        api_key = os.getenv("GROK_API_KEY") or st.text_input("Grok API Key", type="password")
        model = "grok-beta"
    elif provider == "OpenAI":
        api_key = os.getenv("OPENAI_API_KEY") or st.text_input("OpenAI API Key", type="password")
        model = st.selectbox("Model", ["gpt-4o", "gpt-4-turbo"])
    else:
        model = "llama3.2"
        api_key = None

    voice_enabled = st.checkbox("🔊 Enable Voice Output", value=True)
    st.divider()
    st.info("OM is here to listen, help, and grow with you.")

# ====================== CHAT HISTORY ======================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant", 
            "content": "Hey there! 👋 I'm **OM**, your personal AI companion.\n\nHow are you feeling today?"
        }
    ]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ====================== USER INPUT ======================
if prompt := st.chat_input("Type your message to OM..."):
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # OM's response area
    with st.chat_message("assistant"):
        with st.spinner("OM is thinking... 🌌"):
            
            if is_depression_related(prompt):
                response = """
**I'm really sorry you're feeling this way.** 💜  

You are **not alone**, and it's okay to not be okay. Reaching out like this shows strength.

**Please consider talking to someone:**
- **USA**: Call or text **988**
- **India**: iCall Helpline → **9152987821**
- **UK**: Samaritans → **116 123**
- Global help: [iasp.info](https://www.iasp.info/resources/Crisis_Centres/)

I'm here to listen as long as you need. Would you like to tell me more?
"""
            else:
                # Normal response (you can connect real LLM here later)
                response = "I'm OM. Right now I'm running in basic mode. Once you connect an API key, I'll be able to have full conversations with you! 🌟"

            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Voice Output
            if voice_enabled:
                try:
                    engine = pyttsx3.init()
                    engine.say(response[:200])   # Limit length for voice
                    engine.runAndWait()
                except:
                    pass   # Silently ignore voice errors

# ====================== FOOTER ======================
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #888;'>OM • Your Personal AI • Built with love and Python</p>", 
    unsafe_allow_html=True
)