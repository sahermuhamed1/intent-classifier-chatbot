# 🤖 Intent Classification Chatbot

**Intent Detection using BERT deployed by Fast API in a Flask Application**  
This project uses a fine-tuned BERT model that is an encoder only model without a decoder used to detect user intent from text inputs (e.g., chatbot queries). It provides a lightweight Flask API to classify input sentences into predefined intent categories.

### 🌐 Access the **Chatbot Application** from [HERE](https://huggingface.co/spaces/SaherMuhamed/intent-classifier-chatbot)
### 🤗 Access the **Huggingface pretrained Model** from [HERE](https://huggingface.co/SaherMuhamed/bert-intention-classifier)


## 🔧 Features

- ✅ Pretrained BERT fine-tuned on [CLINC150](https://huggingface.co/datasets/clinc_oos)
- 🧠 Real-time intent classification from natural text
- 🌐 REST API using Flask
- 🤖 Easy to integrate with chatbots, voice assistants, or NLP systems

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


## 🚀 Example

### Request
```bash
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


## ⚙️ Tech Stack

- **Backend**: FastAPI, PyTorch, Transformers
- **Frontend**: HTML, CSS, JavaScript
- **Model**: BERT-base fine-tuned on CLINC150
- **Deployment**: Docker, Hugging Face Spaces

## 🧑🏻‍💻 Usage

1. Run the Dockerfile as a container to set up the environment.  
2. Load the pretrained Intent BERT model and tokenizer by executing *`model/api/api.py`*
2. Start the FastAPI server by running *`model/api/start_server.py`*.  
3. (Optional) Test the FastAPI endpoint by running *`model/api/test.py`*.  
4. Run the Flask web application by executing *`src/main.py`*.  


## 🙋🏻‍♂️ Author

**Saher Muhamed**
- Email: sahermuhamed176@gmail.com
