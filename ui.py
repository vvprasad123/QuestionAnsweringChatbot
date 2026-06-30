"""
ui.py

Professional AI Assistant UI
"""

import streamlit as st


class ChatUI:

    # ==========================================
    # Page Header
    # ==========================================
    @staticmethod
    def page_header():

        st.markdown(
            """
            <div class="hero">

              
            </div>
            """,
            unsafe_allow_html=True
        )

    # ==========================================
    # Sidebar
    # ==========================================
    @staticmethod
    def sidebar():

        with st.sidebar:

            st.markdown(
                """
                <div class="sidebar-title">
                    🤖 AI Assistant
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("---")

            # New Chat
            new_chat = st.button(
                "➕ New Chat",
                use_container_width=True
            )

            st.markdown("### 🔍 Search")

            search_text = st.text_input(
                "Search conversations",
                placeholder="Search conversations...",
                label_visibility="collapsed"
            )

            st.markdown("---")

            st.markdown("### 📄 Upload Document")

            uploaded_file = st.file_uploader(
                "Choose a file",
                type=["pdf", "docx", "txt"],
                label_visibility="collapsed"
            )

            st.markdown("### 🖼 Upload Image")

            uploaded_image = st.file_uploader(
                "Choose an image",
                type=["png", "jpg", "jpeg", "webp"],
                label_visibility="collapsed"
            )

            st.markdown("---")

            st.markdown("### 🤖 AI Model")

            model_name = st.selectbox(
                "Model",
                [
                    "gemini-2.5-flash",
                    "gemini-2.5-pro"
                ],
                label_visibility="collapsed"
            )

            temperature = st.slider(
                "Temperature",
                min_value=0.0,
                max_value=2.0,
                value=0.7,
                step=0.1
            )

            st.markdown("---")

            st.info(
                """
**Professional AI Assistant**

✅ Gemini AI

✅ File Upload

✅ Image Analysis

✅ Chat Memory

✅ Markdown Support
                """
            )

            return (
                new_chat,
                uploaded_file,
                uploaded_image,
                search_text,
                model_name,
                temperature
            )

    # ==========================================
    # Welcome Screen
    # ==========================================
    @staticmethod
    def welcome():

        st.markdown(
            """
            <div class="glass-card">

                <div class="hero">

                    <h1>Welcome 👋</h1>

                    <p>
                        Ask anything or upload a document/image to get started.
                    </p>

                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    # ==========================================
    # Empty State
    # ==========================================
    @staticmethod
    def empty_state():

        st.markdown(
            """
            <div class="glass-card">

                <h2 align="center">
                    🤖 AI Assistant
                </h2>

                <br>

                <p align="center">

                💬 Ask Questions

                <br><br>

                📄 Analyze Documents

                <br><br>

                🖼 Analyze Images

                <br><br>

                💻 Generate Code

                <br><br>

                📊 Data Analysis

                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # ==========================================
    # Chat Input
    # ==========================================
    @staticmethod
    def chat_box():

        return st.chat_input(
            "💬 Message AI Assistant..."
        )

    # ==========================================
    # Divider
    # ==========================================
    @staticmethod
    def divider():

        st.divider()

    # ==========================================
    # Loading Spinner
    # ==========================================
    @staticmethod
    def loading():

        return st.spinner(
            "🤖 Thinking..."
        )
    # ==========================================
    # Display Chat Messages
    # ==========================================
    @staticmethod
    def display_messages(messages):

        for message in messages:

            avatar = "🧑" if message["role"] == "user" else "🤖"

            with st.chat_message(
                message["role"],
                avatar=avatar
            ):

                st.markdown(message["content"])

    # ==========================================
    # User Message
    # ==========================================
    @staticmethod
    def user_message(message):

        with st.chat_message(
            "user",
            avatar="🧑"
        ):

            st.markdown(message)

    # ==========================================
    # Assistant Message
    # ==========================================
    @staticmethod
    def assistant_message(message):

        with st.chat_message(
            "assistant",
            avatar="🤖"
        ):

            st.markdown(message)

    # ==========================================
    # Success Message
    # ==========================================
    @staticmethod
    def success(text):

        st.success(text)

    # ==========================================
    # Error Message
    # ==========================================
    @staticmethod
    def error(text):

        st.error(text)

    # ==========================================
    # Warning Message
    # ==========================================
    @staticmethod
    def warning(text):

        st.warning(text)

    # ==========================================
    # Information Message
    # ==========================================
    @staticmethod
    def info(text):

        st.info(text)

    # ==========================================
    # Display Image
    # ==========================================
    @staticmethod
    def image(image):

        st.image(
            image,
            use_container_width=True
        )

    # ==========================================
    # Display Uploaded File Card
    # ==========================================
    @staticmethod
    def uploaded_file(filename):

        st.markdown(
            f"""
            <div class="upload-card">

                📄 <b>{filename}</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    # ==========================================
    # Display Uploaded Image Card
    # ==========================================
    @staticmethod
    def uploaded_image(filename):

        st.markdown(
            f"""
            <div class="upload-card">

                🖼 <b>{filename}</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    # ==========================================
    # Code Display
    # ==========================================
    @staticmethod
    def code(code, language="python"):

        st.code(
            code,
            language=language
        )

    # ==========================================
    # Statistics
    # ==========================================
    @staticmethod
    def statistics(messages):

        users = sum(
            1 for msg in messages
            if msg["role"] == "user"
        )

        assistants = sum(
            1 for msg in messages
            if msg["role"] == "assistant"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Questions",
                users
            )

        with col2:

            st.metric(
                "Responses",
                assistants
            )

    # ==========================================
    # Typing Placeholder
    # ==========================================
    @staticmethod
    def typing():

        return st.empty()

    # ==========================================
    # Response Toolbar
    # ==========================================
    @staticmethod
    def response_toolbar(index):

        c1, c2, c3 = st.columns(3)

        with c1:
            copy = st.button(
                "📋 Copy",
                key=f"copy_{index}"
            )

        with c2:
            retry = st.button(
                "🔄 Retry",
                key=f"retry_{index}"
            )

        with c3:
            like = st.button(
                "👍",
                key=f"like_{index}"
            )

        return copy, retry, like
    # ==========================================
    # Chat History
    # ==========================================
    @staticmethod
    def chat_history(chat_list):

        st.subheader("🕒 Chat History")

        if len(chat_list) == 0:
            st.caption("No previous chats")
            return None

        selected = st.selectbox(
            "Select Conversation",
            chat_list
        )

        return selected

    # ==========================================
    # Download Chat
    # ==========================================
    @staticmethod
    def download_chat(chat_text):

        st.download_button(
            label="📥 Download Chat",
            data=chat_text,
            file_name="chat_history.txt",
            mime="text/plain",
            use_container_width=True
        )

    # ==========================================
    # Theme Selector
    # ==========================================
    @staticmethod
    def theme_selector():

        theme = st.radio(
            "🎨 Theme",
            [
                "Dark",
                "Light"
            ],
            horizontal=True
        )

        return theme

    # ==========================================
    # Clear Chat
    # ==========================================
    @staticmethod
    def clear_chat():

        return st.button(
            "🗑 Clear Chat",
            use_container_width=True
        )

    # ==========================================
    # Footer
    # ==========================================
    @staticmethod
    def footer():

        st.markdown(
            """
            <br><br>

            <div class="footer">

            Built with ❤️ using

            <br>

            <b>Python • Streamlit • Google Gemini 2.5 Flash</b>

            </div>
            """,
            unsafe_allow_html=True
        )

    # ==========================================
    # Toast Notification
    # ==========================================
    @staticmethod
    def toast(message):

        st.toast(message)

    # ==========================================
    # Sidebar Footer
    # ==========================================
    @staticmethod
    def sidebar_footer():

        st.sidebar.markdown("---")

        st.sidebar.caption("🚀 AI Assistant v2.0")

        st.sidebar.caption("Powered by Google Gemini")

    # ==========================================
    # AI Suggestion Cards
    # ==========================================
    @staticmethod
    def suggestion_cards():

        st.markdown(
            """
            <div class="glass-card">

            <h3 align="center">
            🚀 Try asking
            </h3>

            </div>
            """,
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2)

        with c1:

            st.markdown(
                """
                <div class="suggestion-card">

                <div class="suggestion-title">

                💻 Programming

                </div>

                <div class="suggestion-desc">

                Generate Python, Java, C++, SQL code.

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="suggestion-card">

                <div class="suggestion-title">

                📄 Documents

                </div>

                <div class="suggestion-desc">

                Summarize and analyze uploaded files.

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:

            st.markdown(
                """
                <div class="suggestion-card">

                <div class="suggestion-title">

                🖼 Images

                </div>

                <div class="suggestion-desc">

                Explain and analyze uploaded images.

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <div class="suggestion-card">

                <div class="suggestion-title">

                🤖 AI Assistant

                </div>

                <div class="suggestion-desc">

                Ask anything and receive detailed answers.

                </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # ==========================================
    # Welcome Dashboard
    # ==========================================
    @staticmethod
    def dashboard():

        st.markdown("## ✨ AI Dashboard")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("💬 Chats", "0")

        with c2:
            st.metric("📄 Files", "0")

        with c3:
            st.metric("🖼 Images", "0")