"""
config.py

Configuration and Gemini Client
"""

import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found.\n"
        "Create a .env file and add:\n"
        "GOOGLE_API_KEY=YOUR_API_KEY"
    )

# Gemini Client
client = genai.Client(
    api_key=GOOGLE_API_KEY
)

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