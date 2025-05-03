from transformers import pipeline
import gradio as gr

# 1) Load a better model with three-way sentiment classes
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest",
    return_all_scores=True  # get scores for all classes
)

# 2) Map the raw model labels to friendly names
label_map = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

def analyze_sentiment(text):
    # Run the pipeline and grab the first (and only) item
    scores = sentiment_pipeline(text)[0]  # e.g. [{"label":"LABEL_0","score":…},…]
    
    # Build a dict of {friendly_label: score}
    breakdown = {
        label_map[item["label"]]: item["score"]
        for item in scores
        if item["label"] in label_map
    }
    
    # Pick the top class by maximum score
    top_label = max(breakdown, key=breakdown.get)
    top_score = breakdown[top_label]
    
    return top_label, top_score, breakdown

# 3) Build a Gradio UI with three outputs
demo = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(
        lines=2, placeholder="Enter text here…",
        label="Enter text to analyze"
    ),
    outputs=[
        gr.Textbox(label="Overall Sentiment"),
        gr.Number(label="Confidence Score"),
        gr.Label(num_top_classes=3, label="Probability Breakdown")
    ],
    title="Improved Sentiment Analysis",
    description=(
        "Uses a RoBERTa model fine-tuned on Twitter data for Negative/Neutral/Positive.  \n"
        "*Tip:* Check the probability breakdown to see how confident the model is in each category."
    )
)

if __name__ == "__main__":
    demo.launch(share=True, server_name="0.0.0.0", server_port=7860)
