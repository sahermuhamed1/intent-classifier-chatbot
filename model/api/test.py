import requests

url = "http://localhost:8000/predict"
data = {"text": "I need to add 100$ to my bank account."}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response:", response.json())
