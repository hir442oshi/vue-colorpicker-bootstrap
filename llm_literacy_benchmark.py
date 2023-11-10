from transformers import pipeline

def analyze_literacy_sentiment(student_responses):
    sentiment_task = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
    results = sentiment_task(student_responses)
    return results