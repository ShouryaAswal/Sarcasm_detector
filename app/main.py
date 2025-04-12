# app/main.py
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import logging

# Set up logging
logging.basicConfig(filename="predictions.log", level=logging.INFO)

app = FastAPI()

# Load model pipeline
pipe = joblib.load("app/model/sentiment_pipeline.pkl")

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    result = pipe(input.text)
    logging.info(f"Input: {input.text} | Prediction: {result}")
    return {"input": input.text, "prediction": result}
