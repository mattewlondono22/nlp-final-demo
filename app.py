import gradio as gr
from transformers import pipeline

# Initialize the text classification pipeline
classifier = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment")

def classify_text(text):
    result = classifier(text)[0]
    return result['label'], result['score']

# Create Gradio interface
demo = gr.Interface(
    fn=classify_text,
    inputs=gr.Textbox(label="Enter text to analyze", placeholder="Type or paste text here..."),
    outputs=[
        gr.Textbox(label="Sentiment"),
        gr.Number(label="Confidence Score")
    ],
    title="Sentiment Analysis Demo",
    description="Analyze the sentiment of text using a fine-tuned RoBERTa model trained on Twitter data."
)

if __name__ == "__main__":
    demo.launch()
