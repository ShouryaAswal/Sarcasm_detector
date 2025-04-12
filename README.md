# 🤖 Sarcasm Detector Bot

A sarcasm and sentiment detection API powered by HuggingFace transformers, FastAPI, Docker, and GitHub Actions CI/CD.

Built as part of an MLOps demonstration for deploying ML models with reproducibility, automation, and testing in mind.

---

## 📌 Features
- 🔍 Detects sarcasm and sentiment using `cardiffnlp/twitter-roberta-base-sentiment`
- 🚀 Dockerized FastAPI app for deployment anywhere
- 🔄 GitHub Actions CI/CD pipeline that trains model, builds Docker image, and runs test prediction
- 📀 Model saved as artifact and reused between pipeline jobs

---

## 🧱 Project Structure
```
sarcasm-detector/
├── app/
│   ├── main.py                # FastAPI application
│   ├── model/                 # Contains saved model (.pkl)
│   └── requirements.txt       # Python dependencies
├── train_model.py            # Trains and saves the sentiment model
├── Dockerfile                # Dockerfile for the backend
├── .github/workflows/
│   └── docker-ci.yml         # GitHub Actions pipeline
```

---

## 🐳 Local Setup

### 1. Clone the Repo
```bash
git clone https://github.com/ShouryaAswal/Sarcasm_detector.git
cd Sarcasm_detector
```

### 2. Build Docker Image
```bash
docker build -t sarcasm-detector .
```

### 3. Run the Container
```bash
docker run -p 8000:8000 sarcasm-detector
```

### 4. Test the API
```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"text": "Oh wow, this is just *perfect*!"}'
```

---

## 🦪 GitHub Actions CI/CD Workflow

- **Job 1:** `build-model`
  - Sets up Python and dependencies
  - Runs `train_model.py`
  - Uploads `.pkl` file as an artifact

- **Job 2:** `build-and-test`
  - Downloads model artifact
  - Builds Docker image
  - Starts container
  - Sends test prediction request to `/predict`:
    ```bash
    curl -X POST http://localhost:8000/predict \
         -H "Content-Type: application/json" \
         -d '{"text": "Yeah, great job... not"}'
    ```
  - Shuts container down

✅ Triggered on every `push` to `main`

---

## 📄 API Endpoint
**POST** `/predict`

**Request Body:**
```json
{
  "text": "I just love getting stuck in traffic."
}
```

**Response:**
```json
{
  "input": "I just love getting stuck in traffic.",
  "prediction": {
    "sentiment": "Negative",
    "confidence": 0.934
  }
}
```

---
