import streamlit as st
from googletrans import LANGUAGES
from translate import Translator as CustomTranslator
from gtts import gTTS
import tempfile
import shutil

# Define the Translate function
def Translate(supported_languages):
    st.subheader('Language Translation')
    input_text = st.text_area("Enter text for translation:", height=200)
    src_lang = st.selectbox("Select source language", list(supported_languages.values()))
    dest_lang = st.selectbox("Select destination language", list(supported_languages.values()))

    # Convert language name to language code for destination language
    dest_lang_code = next(code for code, name in LANGUAGES.items() if name == dest_lang)

    if st.button("Translate"):
        if input_text:
            translator = CustomTranslator(to_lang=dest_lang_code)
            translation = translator.translate(input_text)
            st.subheader("Translation Result:")
            st.write(translation)

            tts = gTTS(text=translation, lang=dest_lang_code)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts.save(tmp_file.name)

            audio_url = open(tmp_file.name, "rb").read()
            st.audio(audio_url, format="audio/mp3")


            # Clean up the temporary audio file
            shutil.unlink(tmp_file.name)

st.set_page_config(page_title='Live_Translate_Streamlit_App', page_icon='🐍', initial_sidebar_state='expanded')

try:
    Authenticator = None  # No authentication

    st.sidebar.markdown("Navigation")
    selected_page = st.sidebar.radio("Navigation", ["HOME", "LIVE TRANSLATION"])

    if selected_page == "HOME":
        st.subheader('Welcome , Translate your text for free and hear them aloud using our app')
        st.header(" ")
        st.subheader('Navigate to live translation and enter your text of your choice of language')
        st.header(" ")
        st.header(" ")
        st.header(" ")
        st.text('Created by SHYAM RAJ D [7376222IT254] for AI lab')

    elif selected_page == "LIVE TRANSLATION":
        Translate(LANGUAGES)

except Exception as e:
    st.error(f"An error occurred: {str(e)}")
