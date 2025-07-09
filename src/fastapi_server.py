from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(req: PredictRequest):
    # Dummy implementation for testing
    # Replace with your model inference logic
    if "alarm" in req.text.lower():
        intent = "set_alarm"
    else:
        intent = "unknown"
    return {"intent": intent}