import streamlit as st
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
#os.environ["OPEN_API_KEY"] =  "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"
load_dotenv()

def get_openai_response(question):
    llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY")   , temperature=0.6)
    response = llm(question)
    return response




st.title("Langchain Application")
st.header("Q&A Demo")
# Get user input
user_input = st.text_input("Ask The Question:")
response = get_openai_response(user_input)

# Button to display the input
if st.button("The Answer is:"):
    st.write("Output:", response)
