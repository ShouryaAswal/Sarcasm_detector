FROM python:3.9-slim


WORKDIR /app

COPY ./app /app
COPY train_model.py .
COPY test_model.py .

COPY ./app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN python train_model.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]