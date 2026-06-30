"""
main.py

Professional AI Assistant
"""

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

from ui import ChatUI
from file_handler import FileHandler
from image_handler import ImageHandler


# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:

    st.error("❌ GOOGLE_API_KEY not found.")

    st.stop()


# ==========================================
# Gemini Client
# ==========================================

client = genai.Client(api_key=api_key)


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# Load CSS
# ==========================================

try:

    with open(
        "assets/style.css",
        "r",
        encoding="utf-8"
    ) as css:

        st.markdown(
            f"<style>{css.read()}</style>",
            unsafe_allow_html=True
        )

except FileNotFoundError:

    st.warning("style.css not found.")


# ==========================================
# Session State
# ==========================================

if "messages" not in st.session_state:

    st.session_state.messages = []

if "document_text" not in st.session_state:

    st.session_state.document_text = ""

if "image_path" not in st.session_state:

    st.session_state.image_path = None


# ==========================================
# Create Upload Folder
# ==========================================

os.makedirs(
    "uploads",
    exist_ok=True
)


# ==========================================
# Create Objects
# ==========================================

ui = ChatUI()

file_handler = FileHandler()

image_handler = ImageHandler()


# ==========================================
# Header
# ==========================================

ui.page_header()


# ==========================================
# Sidebar
# ==========================================

(
    new_chat,
    uploaded_file,
    uploaded_image,
    search_text,
    model_name,
    temperature

) = ui.sidebar()


# ==========================================
# Clear Chat
# ==========================================

if new_chat:

    st.session_state.messages = []

    st.session_state.document_text = ""

    st.session_state.image_path = None

    st.rerun()


# ==========================================
# Welcome Screen
# ==========================================

if len(st.session_state.messages) == 0:

    ui.suggestion_cards()
# ==========================================
# Document Upload
# ==========================================

if uploaded_file is not None:

    try:

        path = file_handler.save_file(uploaded_file)

        st.session_state.document_text = file_handler.extract_text(path)

        ui.success("📄 Document uploaded successfully!")

        with st.expander("📄 Document Preview"):

            st.text_area(
                "Content",
                st.session_state.document_text,
                height=300
            )

    except Exception as e:

        ui.error(str(e))


# ==========================================
# Image Upload
# ==========================================

if uploaded_image is not None:

    try:

        image_path = image_handler.save_image(uploaded_image)

        st.session_state.image_path = image_path

        ui.success("🖼 Image uploaded successfully!")

        ui.image(image_path)

        if st.button("🔍 Analyze Image"):

            with ui.loading():

                result = image_handler.describe(image_path)

            st.markdown(result)

    except Exception as e:

        ui.error(str(e))


# ==========================================
# Dashboard
# ==========================================

ui.dashboard()


# ==========================================
# Display Previous Messages
# ==========================================

ui.display_messages(
    st.session_state.messages
)


# ==========================================
# Statistics
# ==========================================

ui.statistics(
    st.session_state.messages
)


# ==========================================
# Chat Input
# ==========================================

prompt = ui.chat_box()


# ==========================================
# User Message
# ==========================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    ui.user_message(prompt)


# ==========================================
# Conversation History
# ==========================================

history = ""

for message in st.session_state.messages:

    if message["role"] == "user":

        history += (
            f"User: {message['content']}\n"
        )

    else:

        history += (
            f"Assistant: {message['content']}\n"
        )


# ==========================================
# Add Uploaded Document
# ==========================================

if st.session_state.document_text:

    history += (
        "\n\nDocument:\n"
        + st.session_state.document_text
    )
# ==========================================
# AI Response
# ==========================================

if prompt:

    with st.chat_message(
        "assistant",
        avatar="🤖"
    ):

        placeholder = st.empty()

        full_response = ""

        with st.spinner("🤖 Thinking..."):

            try:

                # Generate AI Response
                response = client.models.generate_content(
                    model=model_name,
                    contents=history
                )

                answer = response.text

            except Exception as e:

                answer = f"❌ {e}"

        # -----------------------------
        # Typing Animation
        # -----------------------------

        words = answer.split()

        for word in words:

            full_response += word + " "

            placeholder.markdown(full_response + "▌")

        placeholder.markdown(full_response)

    # -----------------------------
    # Save Assistant Response
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )


# ==========================================
# Download Chat
# ==========================================

chat_text = ""

for msg in st.session_state.messages:

    if msg["role"] == "user":

        chat_text += f"User:\n{msg['content']}\n\n"

    else:

        chat_text += f"Assistant:\n{msg['content']}\n\n"

ui.download_chat(chat_text)


# ==========================================
# Footer
# ==========================================

ui.footer()


# ==========================================
# Sidebar Footer
# ==========================================

ui.sidebar_footer()


# ==========================================
# Toast Notification
# ==========================================

if uploaded_file is not None:

    ui.toast("📄 Document Ready")

if uploaded_image is not None:

    ui.toast("🖼 Image Ready")


# ==========================================
# Search Chat
# ==========================================

if search_text:

    st.markdown("## 🔍 Search Results")

    found = False

    for message in st.session_state.messages:

        if search_text.lower() in message["content"].lower():

            found = True

            with st.chat_message(message["role"]):

                st.markdown(message["content"])

    if not found:

        st.info("No matching messages found.")


# ==========================================
# Theme Information
# ==========================================

theme = ui.theme_selector()

if theme == "Light":

    st.info(
        "Light theme selected. "
        "Dark theme CSS is currently active."
    )


# ==========================================
# End
# ==========================================