"""
utils.py

Utility functions for AI Chat Assistant
"""

import os
import json
import uuid
from datetime import datetime

# ============================
# Directories
# ============================

CHAT_DIR = "chat_history"
UPLOAD_DIR = "uploads"

os.makedirs(CHAT_DIR, exist_ok=True)
os.makedirs(UPLOAD_DIR, exist_ok=True)


# ============================
# Generate Chat ID
# ============================

def generate_chat_id():
    return str(uuid.uuid4())


# ============================
# Current Time
# ============================

def current_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


# ============================
# Save Chat
# ============================

def save_chat(chat_id, messages):

    file_path = os.path.join(
        CHAT_DIR,
        f"{chat_id}.json"
    )

    data = {
        "chat_id": chat_id,
        "updated": current_time(),
        "messages": messages
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )


# ============================
# Load Chat
# ============================

def load_chat(chat_id):

    file_path = os.path.join(
        CHAT_DIR,
        f"{chat_id}.json"
    )

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data["messages"]


# ============================
# List Chats
# ============================

def list_chats():

    chats = []

    for file in os.listdir(CHAT_DIR):

        if file.endswith(".json"):

            chats.append(
                file.replace(".json", "")
            )

    chats.sort(reverse=True)

    return chats


# ============================
# Delete Chat
# ============================

def delete_chat(chat_id):

    file_path = os.path.join(
        CHAT_DIR,
        f"{chat_id}.json"
    )

    if os.path.exists(file_path):
        os.remove(file_path)


# ============================
# Export Chat
# ============================

def export_chat(chat_id):

    messages = load_chat(chat_id)

    export_path = os.path.join(
        CHAT_DIR,
        f"{chat_id}.txt"
    )

    with open(export_path, "w", encoding="utf-8") as f:

        for msg in messages:

            role = msg["role"].capitalize()

            f.write(f"{role}\n")
            f.write("-" * 40)
            f.write("\n")
            f.write(msg["content"])
            f.write("\n\n")

    return export_path


# ============================
# Clear Upload Folder
# ============================

def clear_uploads():

    for file in os.listdir(UPLOAD_DIR):

        path = os.path.join(
            UPLOAD_DIR,
            file
        )

        if os.path.isfile(path):
            os.remove(path)


# ============================
# File Size
# ============================

def readable_size(size):

    for unit in ["B", "KB", "MB", "GB"]:

        if size < 1024:
            return f"{size:.2f} {unit}"

        size /= 1024

    return f"{size:.2f} TB"


# ============================
# Clean Markdown
# ============================

def clean_text(text):

    if text is None:
        return ""

    return text.strip()


# ============================
# Download Button Helper
# ============================

def get_download_filename():

    return (
        "Chat_"
        + datetime.now().strftime("%Y%m%d_%H%M%S")
        + ".txt"
    )