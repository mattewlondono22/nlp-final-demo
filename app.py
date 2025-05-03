import streamlit as st
from transformers import pipeline
from PIL import Image

# Load the pre-trained model
classifier = pipeline("image-classification", model="julien-c/hotdog-not-hotdog")

st.title("🌭 Hot Dog? Or Not?")
st.write("Upload an image, and we'll tell you if it's a hot dog!")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Classifying...")
    predictions = classifier(image)

    for prediction in predictions:
        label = prediction['label']
        score = prediction['score']
        st.write(f"**{label}**: {score:.2%}")
