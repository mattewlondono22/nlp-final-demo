import gradio as gr
from transformers import pipeline

# Initialize the text classification pipeline
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def classify_text(text):
    result = classifier(text)[0]
    return result['label'], result['score']

# Create Gradio interface
demo = gr.Interface(
    fn=classify_text,
    inputs=gr.Textbox(label="Enter text to classify"),
    outputs=[
        gr.Textbox(label="Classification"),
        gr.Number(label="Confidence Score")
    ],
    title="Text Classification Demo",
    description="Classify text using a fine-tuned DistilBERT model"
)

if __name__ == "__main__":
    demo.launch()
