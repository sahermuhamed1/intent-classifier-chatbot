# 🤖 Bert Intent Chatbit

**Intent Detection API using BERT and Flask**  
This project uses a fine-tuned BERT model to detect user intent from text inputs (e.g., chatbot queries). It provides a lightweight Flask API to classify input sentences into predefined intent categories.

---

## 🔧 Features

- ✅ Pretrained BERT fine-tuned on [CLINC150](https://huggingface.co/datasets/clinc_oos)
- 🧠 Real-time intent classification from natural text
- 🌐 REST API using Flask
- 🤖 Easy to integrate with chatbots, voice assistants, or NLP systems

---

## 🚀 Example

### Request
```bash
POST /predict
Content-Type: application/json

{
  "text": "I want to book a flight"
}
