<<<<<<< HEAD
---
title: Intent Classifier Chatbot
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
app_port: 7860
license: apache-2.0
short_description: Intent Detection API using BERT and Flask
---

# 🤖 Bert Intent Chatbot (Encoder-Only)

**Intent Detection API using BERT and Flask**  
This project uses a fine-tuned BERT model that is an encoder only model without a decoder used to detect user intent from text inputs (e.g., chatbot queries). It provides a lightweight Flask API to classify input sentences into predefined intent categories.
=======
# 🤖 Bert Intent Chatbit

**Intent Detection API using BERT and Flask**  
This project uses a fine-tuned BERT model to detect user intent from text inputs (e.g., chatbot queries). It provides a lightweight Flask API to classify input sentences into predefined intent categories.
>>>>>>> 3b1a096760cdbb6629d54b32bf43ac1bafaafce9

---

## 🔧 Features

- ✅ Pretrained BERT fine-tuned on [CLINC150](https://huggingface.co/datasets/clinc_oos)
- 🧠 Real-time intent classification from natural text
- 🌐 REST API using Flask
- 🤖 Easy to integrate with chatbots, voice assistants, or NLP systems

---
<<<<<<< HEAD
## 📊 Dataset: CLINC150

The project uses the **CLINC150 dataset**, a benchmark dataset for intent classification in task-oriented dialogue systems.

### 🧾 Overview

- **Total intents**: 150 unique user intents
- **Domains**: 10 real-world domains (e.g., banking, travel, weather, small talk)
- **Examples**: ~22,500 utterances
- **Language**: English
- **Out-of-scope (OOS)**: Includes OOS examples to test robustness

### 📁 Dataset Splits

| Split       | Examples |
|-------------|----------|
| Train       | 7,000   |
| Validation  | 3,000    |
| Test        | 5,500    |

### 📦 Source

- Official repo: [clinc/oos-eval](https://github.com/clinc/oos-eval)
- Hugging Face: [`clinc_oos`](https://huggingface.co/datasets/clinc_oos)


---
=======

>>>>>>> 3b1a096760cdbb6629d54b32bf43ac1bafaafce9
## 🚀 Example

### Request
```bash
<<<<<<< HEAD
{
  "text": "I want to book a flight"
}
```
### Response
```bash
{
  "intent": "book_flight"
}
```

---

# Intent Classifier Chatbot

A sophisticated intent classification system built with BERT and FastAPI that can predict user intents from natural language text.

## Features

- **Advanced NLP**: Uses BERT-based transformer model for accurate intent classification
- **150+ Intent Classes**: Trained on the CLINC150 dataset with comprehensive intent coverage
- **Real-time Prediction**: FastAPI backend for fast inference
- **Clean UI**: Simple and intuitive web interface
- **Production Ready**: Dockerized for easy deployment

## How to Use

1. Enter your message in the text area
2. Click "Predict Intent" 
3. See the AI's prediction of your intent

Try examples like:
- "Set an alarm for 7am" → Alarm
- "Transfer money to John" → Transfer
- "What's the weather like?" → Weather
- "Book a flight to Paris" → Book Flight

## Model Details

- **Architecture**: BERT for Sequence Classification
- **Dataset**: CLINC150 (151 intent classes including out-of-scope)
- **Accuracy**: High performance on intent classification tasks
- **Preprocessing**: Advanced tokenization and text normalization

## Tech Stack

- **Backend**: FastAPI, PyTorch, Transformers
- **Frontend**: HTML, CSS, JavaScript
- **Model**: BERT-base fine-tuned on CLINC150
- **Deployment**: Docker, Hugging Face Spaces

## Author

**Saher Muhamed**
- GitHub: [@sahermuhamed1](https://github.com/sahermuhamed1)
- Email: sahermuhamed176@gmail.com

## 🤗 Hugging Face Spaces Configuration

To deploy this project on [Hugging Face Spaces](https://huggingface.co/spaces), you can use a `README.md` and a `config.json` file to configure your Space for inference.  
Check out the configuration reference at:  
https://huggingface.co/docs/hub/spaces-config-reference

Example `config.json` for inference API:

```json
{
  "hf_space_type": "inference",
  "python_version": "3.10",
  "sdk": "gradio",
  "entrypoint": "app.py"
}
```

- Make sure your `requirements.txt` lists all dependencies.
- The `entrypoint` should point to your main app file (e.g., `app.py` or `main.py`).
- For more details and advanced configuration, see the [Spaces config reference](https://huggingface.co/docs/hub/spaces-config-reference).
=======
POST /predict
Content-Type: application/json

{
  "text": "I want to book a flight"
}
>>>>>>> 3b1a096760cdbb6629d54b32bf43ac1bafaafce9
