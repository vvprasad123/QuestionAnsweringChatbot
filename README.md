# QuestionAnsweringChatbot

A Streamlit-based AI assistant that supports chat, document upload, image upload, and Gemini-powered responses.

## Deployment on Streamlit Community Cloud

1. Push this repository to GitHub.
2. In Streamlit Community Cloud, create a new app and select this repository.
3. Choose the branch `main`.
4. Set the main file to `main.py`.
5. Add the secret `GOOGLE_API_KEY` in Streamlit Cloud secrets.

## Local development

```bash
pip install -r requirements.txt
streamlit run main.py
```

Create a `.env` file locally with:

```env
GOOGLE_API_KEY=your_google_api_key_here
```
