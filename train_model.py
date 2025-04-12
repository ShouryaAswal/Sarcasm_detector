from transformers import pipeline
import joblib
import os

os.makedirs("app/model", exist_ok=True)

pipe = pipeline("text-classification", model="AriEM/sarcasm-detector-roberta")
joblib.dump(pipe, "app/model/sentiment_pipeline.pkl")

print("✅ Model saved to app/model/sentiment_pipeline.pkl")
