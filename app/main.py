from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import logging

app = FastAPI()
pipe = joblib.load("app/model/sentiment_pipeline.pkl")


label_map = {
    "LABEL_0": "Negative",
    "LABEL_1": "Neutral",
    "LABEL_2": "Positive"
}

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    prediction = pipe(input.text)[0]
    readable = {
        "sarcasm": prediction["label"],
        "confidence": round(prediction["score"], 3)
    }

    logging.basicConfig(filename="predictions.log", level=logging.INFO)
    logging.info(f"Input: {input.text} | Prediction: {readable}")

    return {
        "input": input.text,
        "prediction": readable
    }
