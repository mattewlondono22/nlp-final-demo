from transformers import pipeline
import gradio as gr

# Load the sentiment analysis pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

def analyze_sentiment(text):
    try:
        # Get the sentiment result
        result = sentiment_pipeline(text)[0]
        
        # Map the label to a friendly name
        label_map = {
            "LABEL_0": "Negative",
            "LABEL_1": "Neutral",
            "LABEL_2": "Positive"
        }
        
        # Get the label and score
        label = label_map.get(result["label"], "Unknown")
        score = result["score"]
        
        return label, score
    except Exception as e:
        return "Error", 0.0

# Create Gradio interface
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(
        lines=2, placeholder="Enter text here...",
        label="Enter text to analyze"
    ),
    outputs=[
        gr.Textbox(label="Sentiment"),
        gr.Number(label="Confidence Score")
    ],
    title="Sentiment Analysis Demo",
    description="Analyze the sentiment of text using a fine-tuned RoBERTa model."
)

if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0", server_port=7860)
