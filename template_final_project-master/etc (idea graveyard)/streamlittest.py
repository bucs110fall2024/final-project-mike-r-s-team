import streamlit as st
from openai import OpenAI

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'input' not in st.session_state:
    st.session_state['input'] = ''
if 'stored_session' not in st.session_state:
    st.session_state['stored_session'] = []

def get_text():
    input_text = st.text_input('User: ', st.session_state['input'], key= 'input', placeholder= 'Your AI ADHD Assistant Here! Ask me anything...', label_visibility= 'hidden')
    return input_text

st.title('Personalized ADHD Bot')

api = st.sidebar.text_input('OpenAI API Key', type= 'password')
model = st.sidebar.selectbox(label='Model', options= [ 'gpt-4o-mini', 'gpt-4o', 'o1-preview', 'gpt-4-turbo'])

if api:
    client = OpenAI(api_key= api)
    
    