import requests
import json

test_input = {"text": "Oh fantastic, another meeting that could’ve been an email."}

expected_label = "sarcastic"

response = requests.post("http://localhost:8000/predict", json=test_input)
res_json = response.json()

label = res_json["prediction"].get("sarcasm") or res_json["prediction"].get("sentiment")

print(f"Predicted label: {label}")
assert label.lower() == expected_label, f"❌ Test failed! Expected: {expected_label}, Got: {label}"
print("✅ Model test passed.")
