FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Create necessary directories if they don't exist
RUN mkdir -p /app/model /app/intent_classifier_model /app/intent_classifier_tokenizer

# Expose the port
EXPOSE 7860

# Set environment variables
ENV PYTHONPATH=/app

# Run the FastAPI application
CMD ["uvicorn", "model.api.api:app", "--host", "0.0.0.0", "--port", "7860"]
