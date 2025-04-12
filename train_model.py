from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import joblib
import os

# Create directory to save the model wrapper
os.makedirs("app/model", exist_ok=True)

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-sarcasm-twitter")
model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-sarcasm-twitter")

# Save both in a wrapper dictionary
wrapper = {"tokenizer": tokenizer, "model": model}
joblib.dump(wrapper, "app/model/sentiment_pipeline.pkl")

print("✅ Model and tokenizer saved successfully.")
