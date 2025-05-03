# Sentiment Analysis Demo

A web-based sentiment analysis application that uses a fine-tuned RoBERTa model to classify text as positive, negative, or neutral.

## Demo

Try the live demo at: [https://1f5ad16785b5b84012.gradio.live](https://1f5ad16785b5b84012.gradio.live)

## Features

- Real-time sentiment analysis of text input
- Confidence scores for sentiment predictions
- Uses the `cardiffnlp/twitter-roberta-base-sentiment-latest` model
- Simple and intuitive web interface

## How to Use

1. Enter your text in the input box
2. Click "Submit" or press Enter
3. View the sentiment result and confidence score

## Technical Details

- **Model**: `cardiffnlp/twitter-roberta-base-sentiment-latest`
- **Framework**: Transformers (Hugging Face)
- **UI Framework**: Gradio
- **Dependencies**:
  - transformers
  - gradio
  - torch

## Local Development

To run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

The app will be available at http://127.0.0.1:7860

## License

MIT License
