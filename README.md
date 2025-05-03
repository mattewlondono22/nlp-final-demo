# Nuanced Sentiment Analysis Demo

A web-based sentiment analysis application that accurately classifies complex text using the cardiffnlp/twitter-roberta-base-sentiment-latest model.

## Live Demo

Try the live demo at: [https://nlp-final-demo.streamlit.app/](https://nlp-final-demo.streamlit.app/)

## Key Features

- Real-time sentiment analysis with confidence scores
- Simple text input interface
- Clear sentiment and confidence display
- Uses the `cardiffnlp/twitter-roberta-base-sentiment-latest` model
- Handles nuanced and complex text well
- Clean and intuitive web interface

## How to Use

1. Enter your text in the input box
2. Click "Submit" or press Enter
3. View the sentiment result and confidence score

## Technical Details

- **Model**: `cardiffnlp/twitter-roberta-base-sentiment-latest`
  - Fine-tuned RoBERTa model for sentiment analysis
  - Returns POSITIVE/NEGATIVE labels with confidence scores
  - Better at handling nuanced and complex text

- **Framework**: Transformers (Hugging Face)
- **UI Framework**: Streamlit
- **Dependencies**:
  - transformers
  - streamlit
  - torch
  - Python 3.10+

## Local Development

To run locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will be available at http://localhost:8501

## License

MIT License

<!-- GitAds-Verify: C7FSSABM95U5USS4XLVDUHX3ZFYXYYDS -->

## GitAds Sponsored
[![Sponsored by GitAds](https://gitads.dev/v1/ad-serve?source=mattewlondono22/nlp-final-demo@github)](https://gitads.dev/v1/ad-track?source=mattewlondono22/nlp-final-demo@github)

