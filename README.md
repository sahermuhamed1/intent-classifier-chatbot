# 🤖 Intent Classification Chatbot

**Intent Detection API using BERT and Flask**  
This project uses a fine-tuned BERT model that is an encoder only model without a decoder used to detect user intent from text inputs (e.g., chatbot queries). It provides a lightweight Flask API to classify input sentences into predefined intent categories.


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
2. Train BERT and save the fine-tuned model by running *`training/workspace.ipynb`*.  
3. After training, the model will be saved in your base directory.  
4. Start the FastAPI server by running *`model/api/start_server.py`*.  
5. (Optional) Test the FastAPI endpoint by running *`model/api/test.py`*.  
6. Run the Flask web application by executing *`src/main.py`*.  


## 🙋🏻‍♂️ Author

**Saher Muhamed**
- Email: sahermuhamed176@gmail.com