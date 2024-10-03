import streamlit as st
from gradio_client import Client

client = Client("mssab/News_Articles_Categorization")

st.title("News Article Categorization")
st.write("Drop your articles here to categorize them.")

user_input = st.text_area("Enter your article text:")

if st.button("Categorize"):
    if user_input:
        result = client.predict(text=user_input, api_name="/predict")
        st.write("Categorized as:", result)
    else:
        st.error("Please enter some text before categorizing.")