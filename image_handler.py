"""
image_handler.py

Gemini Vision Image Handler
"""

import os
from PIL import Image
from config import client, MODEL_NAME


class ImageHandler:

    def __init__(self):

        self.supported_formats = [
            ".png",
            ".jpg",
            ".jpeg",
            ".webp"
        ]

    # -----------------------------
    # Save Uploaded Image
    # -----------------------------
    def save_image(self, uploaded_image, upload_dir="uploads"):

        os.makedirs(upload_dir, exist_ok=True)

        image_path = os.path.join(
            upload_dir,
            uploaded_image.name
        )

        with open(image_path, "wb") as f:
            f.write(uploaded_image.getbuffer())

        return image_path

    # -----------------------------
    # Open Image
    # -----------------------------
    def open_image(self, image_path):

        return Image.open(image_path)

    # -----------------------------
    # Analyze Image
    # -----------------------------
    def analyze(
        self,
        image_path,
        prompt="Describe this image in detail."
    ):

        try:

            image = self.open_image(image_path)

            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=[
                    prompt,
                    image
                ]
            )

            return response.text

        except Exception as e:

            return f"❌ Error:\n\n{e}"

    # -----------------------------
    # Describe Image
    # -----------------------------
    def describe(self, image_path):

        return self.analyze(
            image_path,
            "Describe this image in detail."
        )

    # -----------------------------
    # OCR
    # -----------------------------
    def extract_text(self, image_path):

        return self.analyze(
            image_path,
            "Extract all visible text from this image."
        )

    # -----------------------------
    # Explain Graph
    # -----------------------------
    def explain_chart(self, image_path):

        return self.analyze(
            image_path,
            "Explain this chart, graph or diagram."
        )

    # -----------------------------
    # Answer Questions
    # -----------------------------
    def ask(self, image_path, question):

        return self.analyze(
            image_path,
            question
        )