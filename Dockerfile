# Use lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all code into container
COPY ./app /app
COPY train_model.py .
COPY test_model.py .
# Change this line to point to the correct requirements.txt location
COPY ./app/requirements.txt .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Build and save the sarcasm model
RUN python train_model.py

# Expose FastAPI port
EXPOSE 8000

# Start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]