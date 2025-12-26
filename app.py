import streamlit as st
import openai
import os

# Get OpenAI API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("Formula AI")
st.write("Type a description of the Excel formula you need:")

user_input = st.text_input("Enter your formula request:")

if st.button("Generate Formula"):
    if user_input:
        with st.spinner("Generating formula…"):
            try:
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=f"Write an Excel formula for: {user_input}",
                    max_tokens=100
                )
                formula = response.choices[0].text.strip()
                st.code(formula)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a description.")
