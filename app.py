# app.py — Simple POSITIVE/NEGATIVE Sentiment Analyzer

from transformers import pipeline
import gradio as gr

# Use the SST-2 model: always returns POSITIVE or NEGATIVE
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text):
    # Run pipeline, get first (and only) result
    result = sentiment_pipeline(text)[0]  
    label = result["label"]              # "POSITIVE" or "NEGATIVE"
    score = result["score"]              # float between 0–1
    return label, score

# Build Gradio UI
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(lines=2, placeholder="Type a sentence…"),
    outputs=[
        gr.Textbox(label="Sentiment"),
        gr.Number(label="Confidence")
    ],
    title="Quick Sentiment Analyzer",
    description="Uses the SST-2 model for clear POSITIVE/NEGATIVE output."
)

if __name__ == "__main__":
    demo.launch()
