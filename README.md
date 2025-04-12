# 🤖 Sarcasm Detector Bot

An MLOps-ready sarcasm detection API using a HuggingFace T5 model, FastAPI for serving predictions, Docker for containerization, and GitHub Actions for CI/CD. This project automatically trains the model, packages it, serves it with FastAPI, and tests its behavior using a sample input.

---

## 📌 Features
- 🔍 Detects **sarcasm** using `mrm8488/t5-base-finetuned-sarcasm-twitter`
- 🚀 Dockerized FastAPI app for deployment anywhere
- 🔄 GitHub Actions CI/CD pipeline that:
  - Trains and serializes the model
  - Uploads the model as an artifact
  - Builds and runs the API in a container
  - Sends a test input and **asserts expected output**

---

## 🧱 Project Structure
```
sarcasm-detector/
├── app/
│   ├── main.py                # FastAPI application
│   ├── model/                 # Contains saved model (.pkl)
│   └── requirements.txt       # Python dependencies
├── train_model.py            # Loads and saves the sarcasm detection model
├── test_model.py             # Sends test request to API and validates output
├── Dockerfile                # Dockerfile for containerizing the backend
├── requirements.txt          # Root-level dependencies
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

## 🧮 GitHub Actions CI/CD Workflow

- **Job 1:** `build-model`
  - Sets up Python
  - Installs dependencies from `requirements.txt`
  - Runs `train_model.py`
  - Uploads `.pkl` model as an artifact

- **Job 2:** `build-and-test`
  - Downloads artifact
  - Builds Docker image
  - Runs container exposing API
  - Installs test dependencies
  - Runs `test_model.py` which:
    - Sends a request to `/predict`
    - Compares the output against expected value (`"derison"`)
    - Fails the build if the output doesn’t match

✅ Automatically triggered on every `push` to `main`

---

## 📄 API Endpoint
**POST** `/predict`

**Request Body:**
```json
{
  "text": "Oh fantastic, another Monday meeting that could’ve been an email."
}
```

**Response:**
```json
{
  "input": "Oh fantastic, another Monday meeting that could’ve been an email.",
  "prediction": {
    "sarcasm": "derison"
  }
}
```

> `"derison"` means the model found sarcasm; `"normal"` means it didn't.

---