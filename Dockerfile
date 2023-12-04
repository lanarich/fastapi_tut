FROM python:3.11-slim

WORKDIR /vet-clin

COPY requirements.txt .

COPY main.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5555

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5555"]