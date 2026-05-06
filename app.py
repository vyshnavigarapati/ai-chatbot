import streamlit as st
from openai import OpenAI

client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

st.title("AI Chatbot")

user_input = st.text_input("Ask something")

if st.button("Send"):

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    st.write(response.choices[0].message.content)