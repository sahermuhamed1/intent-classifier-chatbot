#!/bin/bash

# Download model files if they don't exist
if [ ! -d "/app/intent_classifier_model" ]; then
    echo "Model files not found. Please upload your trained model to the Space."
    echo "Create the following directories and upload your model files:"
    echo "- intent_classifier_model/ (containing the trained BERT model)"
    echo "- intent_classifier_tokenizer/ (containing the tokenizer)"
fi

# Start the FastAPI application
exec uvicorn model.api.api:app --host 0.0.0.0 --port 7860