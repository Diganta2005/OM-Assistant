import streamlit as st
import os
from openai import OpenAI

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
def is_depression_related(text):
    keywords = ["depressed", "depression", "suicidal", "kill myself", "want to die", "hopeless", "worthless", "end it all"]
    return any(word in text.lower() for word in keywords)

# ====================== SIDEBAR ======================
with st.sidebar:
    st.title("⚙️ OM Settings")
    st.caption("Made with ❤️ for you")
   
    provider = st.selectbox("Choose AI Brain", ["Grok (xAI)", "OpenAI"])
   
    if provider == "Grok (xAI)":
        api_key = st.text_input("Grok API Key", type="password", value=st.secrets.get("GROK_API_KEY", ""))
        base_url = "https://api.x.ai/v1"
        model = "grok-beta"
    else:
        api_key = st.text_input("OpenAI API Key", type="password", value=st.secrets.get("OPENAI_API_KEY", ""))
        base_url = "https://api.openai.com/v1"
        model = "gpt-4o-mini"

    st.divider()
    st.info("💡 Enter your API key above to activate OM")

# ====================== CHAT HISTORY ======================
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey there! 👋 I'm **OM**, your personal cosmic AI companion.\n\nHow are you feeling today?"}
    ]

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ====================== CHAT INPUT ======================
if prompt := st.chat_input("Message OM..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("OM is thinking... 🌌"):
            
            if is_depression_related(prompt):
                response = """**I'm really sorry you're feeling this way.** 💜\n\nYou are not alone. Please reach out to someone who can support you right now.\n\n**Helplines:**\n- India: 9152987821\n- USA: 988\n- UK: 116 123"""
            else:
                try:
                    if not api_key:
                        response = "⚠️ Please enter your API key in the sidebar to talk with OM."
                    else:
                        client = OpenAI(api_key=api_key, base_url=base_url)
                        completion = client.chat.completions.create(
                            model=model,
                            messages=st.session_state.messages,
                            temperature=0.85,
                            max_tokens=700
                        )
                        response = completion.choices[0].message.content
                except Exception as e:
                    response = f"❌ Error: {str(e)[:150]}...\n\nPlease check your API key."

            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})