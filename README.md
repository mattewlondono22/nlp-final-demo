# Nuanced Sentiment Analysis Demo

A web-based sentiment analysis application that accurately classifies complex text using the cardiffnlp/twitter-roberta-base-sentiment-latest model.

## Live Demo

Try the live demo at: [https://481e557e2c94ed6891.gradio.live](https://481e557e2c94ed6891.gradio.live)

## Key Features

- Real-time sentiment analysis of text input
- Confidence scores reflecting text complexity
- Uses the `cardiffnlp/twitter-roberta-base-sentiment-latest` model
- Handles nuanced and paradoxical text well
- Clean and intuitive web interface

## How to Use

1. Enter your text in the input box
2. Click "Submit" or press Enter
3. View the sentiment result and confidence score

## Technical Details

- **Model**: `cardiffnlp/twitter-roberta-base-sentiment-latest`
  - Fine-tuned RoBERTa model specifically for sentiment analysis
  - Better at handling nuanced and complex text
  - Provides confidence scores to reflect uncertainty

- **Framework**: Transformers (Hugging Face)
- **UI Framework**: Gradio
- **Dependencies**:
  - transformers
  - gradio
  - torch
  - Python 3.10+

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
