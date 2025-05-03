# app.py — Simple POSITIVE/NEGATIVE Sentiment Analyzer

from transformers import pipeline
import gradio as gr

# Use a model specifically trained on nuanced sentiments
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
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
    title="Nuanced Sentiment Analysis",
    description="Uses the cardiffnlp/twitter-roberta-base-sentiment-latest model to analyze complex text sentiment."
)

if __name__ == "__main__":
    demo.launch(share=True)
