from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import logging

app = FastAPI()

# Load model and tokenizer
wrapper = joblib.load("app/model/sentiment_pipeline.pkl")
tokenizer = wrapper["tokenizer"]
model = wrapper["model"]

class InputText(BaseModel):
    text: str

@app.post("/predict")
def predict(input: InputText):
    input_ids = tokenizer.encode(input.text + "</s>", return_tensors="pt")
    output = model.generate(input_ids=input_ids, max_length=3)
    label = tokenizer.decode(output[0], skip_special_tokens=True)

    logging.basicConfig(filename="predictions.log", level=logging.INFO)
    logging.info(f"Input: {input.text} | Sarcasm: {label}")

    return {
        "input": input.text,
        "prediction": {
            "sarcasm": label  # Returns "derison" or "normal"
        }
    }
