from fastapi import FastAPI, File, UploadFile
from models.sentiment_model import analyze_sentiment

app = FastAPI()

@app.post("/analyze_sentiment/")
async def analyze_text(file: UploadFile = File(...)):
    # Leer el archivo de texto
    content = await file.read()
    text = content.decode("utf-8")

    # Analizar el sentimiento del texto en fragmentos
    sentiment_results = analyze_sentiment(text)
    
    # Consolidar los resultados promediando las calificaciones de estrellas
    total_score = 0
    star_counts = {"1 star": 1, "2 stars": 2, "3 stars": 3, "4 stars": 4, "5 stars": 5}
    for result in sentiment_results:
        stars = result["label"]
        score = result["score"]
        total_score += star_counts[stars] * score

    # Promedio de calificación en estrellas
    average_score = total_score / len(sentiment_results)
    average_stars = round(average_score)

    # Convertir el promedio a una calificación en "stars"
    consolidated_sentiment = {
        "label": f"{average_stars} stars",
        "average_score": average_score
    }

    return {"sentiment": consolidated_sentiment}
