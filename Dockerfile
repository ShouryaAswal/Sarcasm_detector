# Base image with Python
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy app code
COPY ./app /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy model training script and run it
COPY train_model.py .
RUN python train_model.py

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
