from transformers import pipeline

# Cargar el modelo de análisis de sentimientos
sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analyze_sentiment(text, max_length=512):
    # Dividir el texto en fragmentos de 512 tokens
    chunks = [text[i:i + max_length] for i in range(0, len(text), max_length)]
    results = []

    for chunk in chunks:
        result = sentiment_pipeline(chunk)
        results.extend(result)  # Agregar el resultado de cada fragmento

    return results
