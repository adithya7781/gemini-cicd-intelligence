import streamlit as st
from streamlit_option_menu import option_menu

from pages.dashboard import render
from pages.ai_chat import render as render_chat
from pages.upload_logs import render as render_upload

# ------------------ UI THEME ------------------

st.set_page_config(
    page_title="Gemini CI/CD Intelligence",
    layout="wide"
)

st.markdown("""
<style>

section[data-testid="stSidebar"] {
    background-color: #0d1117;
}

div[data-testid="metric-container"] {
    background-color: #161b22;
    border: 1px solid #30363d;
    padding: 12px;
    border-radius: 10px;
}

button[kind="primary"] {
    background-color: #7C83FD;
    color: black;
}

h1, h2, h3 {
    color: #E6EDF3;
}

</style>
""", unsafe_allow_html=True)

# ------------------ NAVIGATION ------------------

with st.sidebar:
    selected = option_menu(
        "Navigation",
        ["Dashboard", "Upload Logs", "AI Assistant"],
        icons=["speedometer", "upload", "chat-dots"],
        default_index=0
    )

# ------------------ ROUTING ------------------

if selected == "Dashboard":
    render()

elif selected == "Upload Logs":
    render_upload()

elif selected == "AI Assistant":
    render_chat()
