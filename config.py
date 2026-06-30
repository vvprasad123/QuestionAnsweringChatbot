"""
config.py

Configuration and Gemini Client
"""

import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()


def get_api_key():
    """Read the API key from local env files or Streamlit Cloud secrets."""

    for key_name in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
        value = os.getenv(key_name)
        if value:
            return value

    try:
        secrets = st.secrets
        if hasattr(secrets, "get"):
            for key_name in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
                value = secrets.get(key_name)
                if isinstance(value, str) and value.strip():
                    return value.strip()
        if hasattr(secrets, "to_dict"):
            secrets_dict = secrets.to_dict()
            for key_name in ("GOOGLE_API_KEY", "GEMINI_API_KEY"):
                value = secrets_dict.get(key_name)
                if isinstance(value, str) and value.strip():
                    return value.strip()
    except Exception:
        pass

    return None


# API Key
GOOGLE_API_KEY = get_api_key()
GOOGLE_API_KEY_ERROR = None

# Gemini Client
client = None

if GOOGLE_API_KEY:
    try:
        client = genai.Client(api_key=GOOGLE_API_KEY)
    except Exception as exc:
        client = None
        GOOGLE_API_KEY = None
        GOOGLE_API_KEY_ERROR = str(exc)
else:
    GOOGLE_API_KEY_ERROR = "Missing GOOGLE_API_KEY"

# Model Name
MODEL_NAME = "gemini-2.5-flash"

# Chat Settings
SYSTEM_PROMPT = """
You are an intelligent AI assistant.

Rules:
- Give accurate answers.
- Use Markdown formatting.
- Explain code clearly.
- Answer any topic.
- If the user uploads a document, answer from that document.
- If the user uploads an image, analyze it.
- Keep responses professional.
"""

# Generation Settings
TEMPERATURE = 0.7
TOP_P = 0.95
TOP_K = 40
MAX_OUTPUT_TOKENS = 4096