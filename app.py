import streamlit as st
from transformers import pipeline

# Use the specific CardiffNLP model for nuanced sentiment analysis
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_analyzer = pipeline("sentiment-analysis", model=MODEL_NAME)

st.title("📝 Sentiment Analysis Demo")
st.write("Enter some text, and we'll analyze its sentiment!")

user_input = st.text_area("Type your text here:")

if user_input:
    st.write("Analyzing sentiment...")
    results = sentiment_analyzer(user_input)
    for result in results:
        label = result['label']
        score = result['score']
        st.write(f"**{label}**: {score:.2%}")
