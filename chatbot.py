from google import genai


class ChatBot:

    def __init__(self, client):
        self.client = client

    def generate_response(
        self,
        prompt,
        model="gemini-2.5-flash",
        temperature=0.7
    ):

        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "temperature": temperature
            }
        )

        return response.text