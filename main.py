import streamlit as st 
from langchain.llms import OpenAI 

openai_api_key = st.secrets['OPENAI_API_KEY']