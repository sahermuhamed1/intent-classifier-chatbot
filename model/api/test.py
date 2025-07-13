import requests

url = "http://localhost:8000/predict"
data = {"text": "just set the alarm for 7:30 am tomorrow to wake me up"}

response = requests.post(url, json=data)
print("Status code:", response.status_code)
print("Response:", response.json())
