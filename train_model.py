from transformers import pipeline
import joblib
import os

os.makedirs("app/model", exist_ok=True)

# Load HuggingFace sentiment model
pipe = pipeline("text-classification", model="cardiffnlp/twitter-roberta-base-sentiment")

# Save the pipeline
joblib.dump(pipe, "app/model/sentiment_pipeline.pkl")

print("Model saved to app/model/sentiment_pipeline.pkl")
