import streamlit as st
import streamlit.components.v1 as components

# --- Custom CSS ---
st.markdown("""
    <style>
    div[data-baseweb="input"] input {
        font-size: 36px !important;
        height: 70px !important;
        padding: 10px 16px !important;
    }
    label {
        font-size: 28px !important;
        font-weight: bold;
    }
    div[data-baseweb="input"] {
        width: 300px !important;
    }
    .invisible-button > button {
        visibility: hidden;
        height: 0px;
        padding: 0px;
        margin: 0px;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🇧🇷🍓🇸🇰 Memrise BBSITOS")

# --- Session State Initialization ---
if "start" not in st.session_state:
    st.session_state.start = False
if "current_word_index" not in st.session_state:
    st.session_state.current_word_index = 0
if "words" not in st.session_state:
    st.session_state.words = ["house", "car", "apple", "dog", "tree"]
if "translation_input" not in st.session_state:
    st.session_state.translation_input = ""
if "results" not in st.session_state:
    st.session_state.results = []
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# --- Start Game Function ---
def start_game():
    st.session_state.start = True
    st.session_state.current_word_index = 0
    st.session_state.results = []
    st.session_state.translation_input = ""
    st.session_state.submitted = False

# --- Submit Translation ---
def submit_translation():
    word = st.session_state.words[st.session_state.current_word_index]
    translation = st.session_state.translation_input
    st.session_state.results.append((word, translation))
    st.session_state.translation_input = ""
    st.session_state.submitted = True

    st.session_state.current_word_index += 1
    if st.session_state.current_word_index >= len(st.session_state.words):
        st.session_state.start = False  # End game
    st.rerun()

# --- Start Button ---
if not st.session_state.start:
    with st.form("start_form"):
        st.form_submit_button("Start Game", on_click=start_game)

# --- Game Loop ---
if st.session_state.start:
    current_index = st.session_state.current_word_index

    if current_index < len(st.session_state.words):
        word_to_translate = st.session_state.words[current_index]
        st.subheader(f"Translate: **{word_to_translate}**")

        with st.form("translation_form"):
            st.text_input(
                "Your translation:",
                key="translation_input",
                label_visibility="collapsed",
                placeholder="Type and press Enter",
            )

            # 👇 Auto-focus the text input using JS
            components.html("""
            <script>
                const input = window.parent.document.querySelector('input[type="text"]');
                if (input) { input.focus(); }
            </script>
            """, height=0)

            st.form_submit_button("Submit", on_click=submit_translation)

    st.write(f"Word {current_index + 1} of {len(st.session_state.words)}")

# --- Game Over ---
if not st.session_state.start and st.session_state.results:
    st.success("🏁 Game over! Here are your results:")
    for word, answer in st.session_state.results:
        st.write(f"• {word} ➜ {answer or '⛔️ No input'}")
