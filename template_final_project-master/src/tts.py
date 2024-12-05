import streamlit as st
from streamlit_TTS import auto_play, text_to_speech, text_to_audio
from gtts.lang import tts_langs

class Tts:
    
    def __init__(self):
        pass
    
    def texttospeech(self, messages, lang = 'en'):
        for phrase in messages[-2:]:
            audio = text_to_audio(phrase, language= lang)
            auto_play(audio)