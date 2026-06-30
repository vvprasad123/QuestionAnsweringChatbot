"""
file_handler.py

Handles reading uploaded documents.
Supports:
- PDF
- DOCX
- TXT
"""

import os
import PyPDF2
from docx import Document


class FileHandler:

    def __init__(self):
        self.supported_types = [
            ".pdf",
            ".docx",
            ".txt"
        ]

    # -------------------------
    # Save Uploaded File
    # -------------------------
    def save_file(self, uploaded_file, upload_dir="uploads"):

        os.makedirs(upload_dir, exist_ok=True)

        file_path = os.path.join(
            upload_dir,
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        return file_path

    # -------------------------
    # Read TXT
    # -------------------------
    def read_txt(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    # -------------------------
    # Read DOCX
    # -------------------------
    def read_docx(self, file_path):

        doc = Document(file_path)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    # -------------------------
    # Read PDF
    # -------------------------
    def read_pdf(self, file_path):

        text = ""

        with open(file_path, "rb") as pdf:

            reader = PyPDF2.PdfReader(pdf)

            for page in reader.pages:
                extracted = page.extract_text()

                if extracted:
                    text += extracted + "\n"

        return text

    # -------------------------
    # Main Reader
    # -------------------------
    def extract_text(self, file_path):

        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".pdf":
            return self.read_pdf(file_path)

        elif extension == ".docx":
            return self.read_docx(file_path)

        elif extension == ".txt":
            return self.read_txt(file_path)

        else:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )