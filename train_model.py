from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import joblib
import os

os.makedirs("app/model", exist_ok=True)


tokenizer = AutoTokenizer.from_pretrained("mrm8488/t5-base-finetuned-sarcasm-twitter", use_fast=False)
model = AutoModelForSeq2SeqLM.from_pretrained("mrm8488/t5-base-finetuned-sarcasm-twitter")

joblib.dump({"tokenizer": tokenizer, "model": model}, "app/model/sentiment_pipeline.pkl")

print("✅ Model saved.")

#push nothing
