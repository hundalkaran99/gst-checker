import streamlit as st
import anthropic

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
def ask_claude(question):
    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return message.content[0].text

st.title("GST Checker India 🇮🇳")
st.write("Enter any product and find out its GST rate instantly.")

product = st.text_input("Enter product name:")

if st.button("Check GST"):
    if product:
        with st.spinner("Checking..."):
            prompt = "What is the GST rate for " + product + " in India? Explain in 2-3 sentences."
            result = ask_claude(prompt)
            st.success(result)
    else:
        st.warning("Please enter a product name.")
