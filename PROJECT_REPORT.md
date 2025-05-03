# NLP Final Project: Nuanced Sentiment Analysis Web App

**Live App:** [https://nlp-final-demo.streamlit.app/](https://nlp-final-demo.streamlit.app/)
**Author:** Mattew Londono  
**GitHub Repo:** [https://github.com/mattewlondono22/nlp-final-demo](https://github.com/mattewlondono22/nlp-final-demo)

## Problem Statement
Sentiment analysis is a classic NLP task, but most models struggle with nuanced, paradoxical, or ambiguous text—especially when emotions are mixed or context is subtle. My goal was to build a web app that goes beyond simple “positive vs negative” judgments and demonstrates how modern NLP models handle complex sentiment in real-world language.

## Passion Area
I am passionate about language, literature, and how technology can help us understand human emotions in text. This project combines my interest in NLP with the challenge of interpreting nuanced literary and everyday language.

## Tools and Model(s) Used
- **Model:** `cardiffnlp/twitter-roberta-base-sentiment-latest` (a RoBERTa-based model fine-tuned for sentiment analysis, known for handling nuanced and complex text better than standard models)
- **Frameworks:** Hugging Face Transformers, Streamlit (for the web UI)
- **Languages:** Python 3.10+
- **Other Tools:** GitHub for version control, Streamlit Cloud for deployment

## Model Integration
- I used the Hugging Face `pipeline` API to load the CardiffNLP RoBERTa sentiment model.
- The model was integrated into a Streamlit web app, allowing users to input any text and instantly see the predicted sentiment (POSITIVE/NEGATIVE) along with a confidence score.
- The app is live and accessible at: [https://nlp-final-demo.streamlit.app/](https://nlp-final-demo.streamlit.app/)

## Key Challenges and Solutions
- **Model Selection:** Initial experiments with SST-2 and BERT models failed to capture nuance in paradoxical quotes. I switched to the CardiffNLP RoBERTa model, which performed better on complex text.
- **Deprecation Issues:** The `return_all_scores` parameter was deprecated in the Transformers pipeline, causing issues with score breakdowns. I simplified the logic to focus on the top sentiment and its confidence.
- **Deployment:** Faced build issues with Gradio and Hugging Face Spaces. I resolved this by deploying on Streamlit Cloud, which worked seamlessly with my codebase.
- **Security:** Ensured no sensitive or binary files were exposed in the git repository by using a proper `.gitignore` and cleaning the repo.

## Future Improvements
- Train a custom model on a dataset of nuanced, paradoxical, or literary text to further improve accuracy.
- Add visualizations (e.g., confidence intervals, sentiment breakdowns) to help users interpret results.
- Support multi-sentence or document-level sentiment analysis.
- Provide more detailed explanations of the model’s reasoning for educational purposes.

## Reflection
This project deepened my understanding of both the strengths and limitations of modern NLP models. I learned that model choice and training data are critical for handling real-world language, and that user interface design is key for making NLP accessible.
