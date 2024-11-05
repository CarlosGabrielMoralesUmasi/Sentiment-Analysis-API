# Sentiment Analysis API

Esta es una API basada en FastAPI que permite realizar análisis de sentimientos en archivos de texto. Utiliza un modelo preentrenado de la biblioteca Transformers de Hugging Face para clasificar el sentimiento de un texto en una escala de 1 a 5 estrellas. La API divide textos largos en fragmentos y luego consolida los resultados en una calificación promedio para representar el sentimiento del texto completo.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Endpoints de la API](#endpoints-de-la-api)
- [Interpretación de las Estrellas](#interpretación-de-las-estrellas)
- [Ejemplo de Respuesta](#ejemplo-de-respuesta)
- [Notas](#notas)
- [Licencia](#licencia)

## Características

- Acepta archivos de texto (`.txt`) para realizar el análisis de sentimientos.
- Utiliza el modelo `nlptown/bert-base-multilingual-uncased-sentiment` que clasifica el sentimiento en una escala de 1 a 5 estrellas.
- Consolida los resultados de fragmentos de texto en una única calificación promedio de "estrellas" para representar el sentimiento general del texto completo.

## Instalación

### Prerrequisitos

- Python 3.7 o superior
- Git

### Pasos

1. Clona el repositorio:

    ```bash
    git clone https://github.com/CarlosGabrielMoralesUmasi/sentiment_analysis_api.git
    cd sentiment_analysis_api
    ```

2. Crea un entorno virtual y actívalo:

    ```bash
    python -m venv env
    # Activar el entorno virtual:
    # En Windows
    .\env\Scripts\Activate
    # En macOS/Linux
    source env/bin/activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Ejecuta el servidor de la API:

    ```bash
    uvicorn main:app --reload
    ```

   La API estará disponible en `http://127.0.0.1:8000`.

## Uso

Puedes probar la API usando [Postman](https://www.postman.com/) o a través de la documentación interactiva de FastAPI.

### Pruebas con Postman

1. Abre Postman y crea una nueva solicitud `POST`.
2. Configura la URL en `http://127.0.0.1:8000/analyze_sentiment/`.
3. En la pestaña **Body**, selecciona **form-data**.
4. Agrega una clave `file` con el **Type** configurado en `File` y sube un archivo `.txt` con el texto que deseas analizar.
5. Haz clic en **Send** para recibir la respuesta de análisis de sentimientos.

## Endpoints de la API

### `POST /analyze_sentiment/`

#### Descripción
Acepta un archivo `.txt` y realiza el análisis de sentimientos sobre el texto.

#### Parámetros
- `file`: Un archivo de texto `.txt` con el texto a analizar.

#### Respuesta
Devuelve un objeto JSON con el resultado consolidado de sentimiento para el texto completo.

## Interpretación de las Estrellas

El modelo proporciona una puntuación de sentimiento en forma de "estrellas", donde:
- **1 estrella**: Sentimiento muy negativo
- **2 estrellas**: Sentimiento negativo
- **3 estrellas**: Sentimiento neutral
- **4 estrellas**: Sentimiento positivo
- **5 estrellas**: Sentimiento muy positivo

La respuesta consolidada refleja el sentimiento general del texto en una calificación promedio de estrellas.

## Ejemplo de Respuesta

Aquí tienes un ejemplo de respuesta de la API cuando se envía un texto para analizar:

```json
{
    "sentiment": {
        "label": "4 stars",
        "average_score": 4.2
    }
}
```
### Explicación del Resultado

- `"label"`: Representa la calificación promedio de "estrellas" del sentimiento del texto completo. Esta calificación es el resultado de promediar las calificaciones de cada fragmento del texto y redondear el promedio al número entero más cercano.
- `"average_score"`: Es el puntaje promedio exacto calculado a partir de los fragmentos analizados. Este puntaje se utiliza para determinar la calificación en estrellas y proporciona un valor más preciso del sentimiento general.

## Notas

- **Modelo utilizado**: Esta API utiliza el modelo `nlptown/bert-base-multilingual-uncased-sentiment` de la biblioteca Transformers de Hugging Face. Este modelo ofrece un análisis de sentimientos en una escala de 1 a 5 estrellas, lo cual es útil para interpretar el sentimiento con mayor granularidad.
- **Límite de longitud de texto**: El modelo tiene un límite de 512 tokens, por lo que la API divide automáticamente el texto en fragmentos cuando es demasiado largo. Luego consolida los resultados de cada fragmento en una única calificación promedio para representar el sentimiento general del texto completo.
- **Interpretación de las Estrellas**:
  - **1 estrella**: Sentimiento muy negativo
  - **2 estrellas**: Sentimiento negativo
  - **3 estrellas**: Sentimiento neutral
  - **4 estrellas**: Sentimiento positivo
  - **5 estrellas**: Sentimiento muy positivo

## Licencia

Este proyecto es de código abierto y está disponible bajo la [Licencia MIT](LICENSE).
