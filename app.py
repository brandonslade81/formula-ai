import streamlit as st
import openai
import os

# Get API key from environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

st.title("Formula AI")
st.write("Type a description of the Excel formula you need:")

user_input = st.text_input("Enter your formula request:")

if st.button("Generate Formula"):
    if user_input:
        with st.spinner("Generating formula…"):
            try:
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are an Excel formula generator."},
                        {"role": "user", "content": f"Write an Excel formula for: {user_input}"}
                    ]
                )
                formula = response.choices[0].message.content.strip()
                st.code(formula)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a description.")
