# 🌟 NLP Final Project Submission

## Title
Nuanced Sentiment Analysis Web Demo

## Live Demo Link
✅ https://1f5ad16785b5b84012.gradio.live/

## Summary (1–2 Pages)

### Overview
For my final NLP project, I built a sentiment analysis web app using Hugging Face Transformers and Gradio. The goal was to go beyond basic “positive vs negative” judgments and explore how well models handle complex, paradoxical text.

I tested the app with two quotes:
1. “War is peace. Freedom is slavery. Ignorance is strength.” (George Orwell, 1984)
2. “Life is a tragedy full of joy.”

These aren’t easy because they mix emotions—so I wanted the system to not just classify but also reflect confidence, showing where it’s unsure.

### Tools & Setup
- Hugging Face Transformers (pipeline("sentiment-analysis"))
- Gradio (for the interactive web interface)
- Python 3.10 with basic dependencies (transformers, gradio, torch)
- Model: cardiffnlp/twitter-roberta-base-sentiment-latest

### How It Works
1. User inputs text
2. Sentiment pipeline processes text using RoBERTa model
3. Returns sentiment label (positive/negative) and confidence score
4. Gradio displays results in real-time on a clean web interface

### Key Results
| Quote | Sentiment | Confidence |
|-------|-----------|------------|
| “War is peace. Freedom is slavery. Ignorance is strength.” | Negative | 55.24% |
| “Life is a tragedy full of joy.” | Negative | 48.58% |

This is much better than the default model, which initially misclassified both as positive. Now, the system not only gets the right direction but also signals uncertainty on more ambiguous lines (like the second quote).

### Challenges
1. **Model Selection**: Initial models (SST-2, BERT) misclassified complex sentiments as positive. Solution: switched to cardiffnlp/twitter-roberta-base-sentiment-latest which better handles nuanced text.
2. **Deprecation Issues**: return_all_scores was deprecated, causing nested lists that broke the app logic. Solution: removed breakdown logic and focused on single sentiment prediction.
3. **Deployment Issues**: Hugging Face Spaces had build issues. Solution: used Gradio's share=True feature to create a temporary public URL.

### What I Learned
1. Off-the-shelf models aren’t magic: you must understand how they were trained and what their label spaces are (binary vs three-class, Twitter vs SST-2, etc.).
2. Confidence scores matter, especially when text has mixed or paradoxical sentiment.
3. Gradio makes it super fast to build a user-friendly NLP demo, even without a heavy backend.

### Future Improvements
1. Train a custom model or fine-tune a RoBERTa-based sentiment classifier on nuanced, paradoxical data.
2. Expand the app to show a full probability breakdown (positive, negative, neutral) and visual graphs.
3. Handle multi-sentence or long-text sentiment with models like text-classification instead of just sentiment-analysis.

## ✅ Final Deliverables
- Live Demo Link (provided)
- Report Summary (this document)
- Code and App Tested ✅
