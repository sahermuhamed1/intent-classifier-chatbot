from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from transformers import BertForSequenceClassification, BertTokenizer
import torch
import os

app = FastAPI(title="Intent Classifier API", description="BERT-based intent classification system")
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("SaherMuhamed/bert-intention-classifier")
model = AutoModelForSequenceClassification.from_pretrained("SaherMuhamed/bert-intention-classifier")

# Complete CLINC150 intent labels in exact order (151 total)
INTENT_LABELS = ['restaurant_reviews',
 'nutrition_info',
 'account_blocked',
 'oil_change_how',
 'time',
 'weather',
 'redeem_rewards',
 'interest_rate',
 'gas_type',
 'accept_reservations',
 'smart_home',
 'user_name',
 'report_lost_card',
 'repeat',
 'whisper_mode',
 'what_are_your_hobbies',
 'order',
 'jump_start',
 'schedule_meeting',
 'meeting_schedule',
 'freeze_account',
 'what_song',
 'meaning_of_life',
 'restaurant_reservation',
 'traffic',
 'make_call',
 'text',
 'bill_balance',
 'improve_credit_score',
 'change_language',
 'no',
 'measurement_conversion',
 'timer',
 'flip_coin',
 'do_you_have_pets',
 'balance',
 'tell_joke',
 'last_maintenance',
 'exchange_rate',
 'uber',
 'car_rental',
 'credit_limit',
 'oos',
 'shopping_list',
 'expiration_date',
 'routing',
 'meal_suggestion',
 'tire_change',
 'todo_list',
 'card_declined',
 'rewards_balance',
 'change_accent',
 'vaccines',
 'reminder_update',
 'food_last',
 'change_ai_name',
 'bill_due',
 'who_do_you_work_for',
 'share_location',
 'international_visa',
 'calendar',
 'translate',
 'carry_on',
 'book_flight',
 'insurance_change',
 'todo_list_update',
 'timezone',
 'cancel_reservation',
 'transactions',
 'credit_score',
 'report_fraud',
 'spending_history',
 'directions',
 'spelling',
 'insurance',
 'what_is_your_name',
 'reminder',
 'where_are_you_from',
 'distance',
 'payday',
 'flight_status',
 'find_phone',
 'greeting',
 'alarm',
 'order_status',
 'confirm_reservation',
 'cook_time',
 'damaged_card',
 'reset_settings',
 'pin_change',
 'replacement_card_duration',
 'new_card',
 'roll_dice',
 'income',
 'taxes',
 'date',
 'who_made_you',
 'pto_request',
 'tire_pressure',
 'how_old_are_you',
 'rollover_401k',
 'pto_request_status',
 'how_busy',
 'application_status',
 'recipe',
 'calendar_update',
 'play_music',
 'yes',
 'direct_deposit',
 'credit_limit_change',
 'gas',
 'pay_bill',
 'ingredients_list',
 'lost_luggage',
 'goodbye',
 'what_can_i_ask_you',
 'book_hotel',
 'are_you_a_bot',
 'next_song',
 'change_speed',
 'plug_type',
 'maybe',
 'w2',
 'oil_change_when',
 'thank_you',
 'shopping_list_update',
 'pto_balance',
 'order_checks',
 'travel_alert',
 'fun_fact',
 'sync_device',
 'schedule_maintenance',
 'apr',
 'transfer',
 'ingredient_substitution',
 'calories',
 'current_location',
 'international_fees',
 'calculator',
 'definition',
 'next_holiday',
 'update_playlist',
 'mpg',
 'min_payment',
 'change_user_name',
 'restaurant_suggestion',
 'travel_notification',
 'cancel',
 'pto_used',
 'travel_suggestion',
 'change_volume']
def int2str(idx):
    return INTENT_LABELS[idx] if 0 <= idx < len(INTENT_LABELS) else "unknown"

class Query(BaseModel):
    text: str = None
    message: str = None

# Add compatibility endpoint for both 'message' and 'text' fields
@app.post("/predict")
def predict_intent_compat(request: Query):
    """Compatibility endpoint that handles both text and message fields"""
    try:
        # Handle both 'text' and 'message' fields for compatibility
        text = request.message or request.text or ""
        
        if not text:
            return {"error": "No text or message provided"}
        
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
        with torch.no_grad():
            outputs = model(**inputs)
            prediction = outputs.logits.argmax(dim=-1).item()
            
            # Debug information
            print(f"Input: {text}")
            print(f"Raw prediction index: {prediction}")
            print(f"Total labels available: {len(INTENT_LABELS)}")
            
            intent = int2str(prediction)
            print(f"Mapped intent: {intent}")
            
        if intent == "oos":
            return {"intent": "out of scope (OOS)"}
        else:
            intent = intent.replace("_", " ").title()
            return {"intent": intent}
    except Exception as e:
        print(f"Error in prediction: {e}")
        return {"intent": "Error", "error": str(e)}



@app.get("/", response_class=HTMLResponse)
async def read_root():
    """Serve the main HTML interface"""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Intent Classifier Chatbot</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { 
                font-family: 'Segoe UI', Arial, sans-serif; 
                margin: 0; 
                background: #f7f9fa; 
                color: #222; 
            }
            .container { 
                max-width: 600px; 
                margin: 60px auto 30px auto; 
                background: #fff; 
                border-radius: 12px; 
                box-shadow: 0 4px 24px rgba(0,0,0,0.08); 
                padding: 32px 28px 24px 28px;
            }
            h1 {
                text-align: center;
                color: #2d6cdf;
                margin-bottom: 18px;
            }
            h2 {
                text-align: center;
                color: #2d6cdf;
                margin-bottom: 18px;
                font-size: 1.5em;
            }
            label {
                font-weight: 500;
                margin-bottom: 8px;
                display: block;
            }
            textarea {
                width: 100%;
                height: 100px;
                padding: 12px;
                border: 1px solid #d2d6dc;
                border-radius: 6px;
                font-size: 1em;
                margin-bottom: 18px;
                box-sizing: border-box;
                transition: border 0.2s;
            }
            textarea:focus {
                border: 1.5px solid #2d6cdf;
                outline: none;
            }
            button {
                width: 100%;
                padding: 12px;
                background: linear-gradient(90deg, #2d6cdf 60%, #4e9cff 100%);
                color: #fff;
                border: none;
                border-radius: 6px;
                font-size: 1.1em;
                font-weight: 600;
                cursor: pointer;
                transition: background 0.2s;
            }
            button:hover {
                background: linear-gradient(90deg, #1b4e9b 60%, #3578c7 100%);
            }
            .result {
                margin-top: 24px;
                font-size: 1.15em;
                background: #eaf3ff;
                border-left: 4px solid #2d6cdf;
                padding: 14px 18px;
                border-radius: 6px;
                color: #1a3a5d;
                word-break: break-word;
            }
            .info {
                margin-top: 18px;
                font-size: 0.98em;
                color: #555;
                background: #f3f6fa;
                border-radius: 6px;
                padding: 10px 14px;
            }
            footer {
                margin-top: 40px;
                text-align: center;
                color: #888;
                font-size: 0.97em;
                padding-bottom: 18px;
            }
            @media (max-width: 600px) {
                .container { padding: 18px 6px 18px 6px; }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Intent Classifier Chatbot</h1>
            <h2>Predict User Intent</h2>
            <div class="info">
                Enter a message below and click <b>Predict Intent</b> to see what the AI thinks your intent is.<br>
                <span style="color:#2d6cdf;">Try: <i>"Set an alarm for 7am"</i> or <i>"Transfer money to John"</i></span>
            </div>
            <div class="form-group">
                <label for="message">Your Message:</label>
                <textarea id="message" placeholder="Type your message here..."></textarea>
            </div>
            <button onclick="predictIntent()">Predict Intent</button>
            <div id="result" class="result" style="display: none;"></div>
        </div>
        <footer>
            Made by <b>Saher Muhamed</b><br>
            <a href="https://github.com/sahermuhamed1" target="_blank" style="color:#2d6cdf;text-decoration:none;">GitHub</a> &middot; 
            <a href="mailto:sahermuhamed176@gmail.com" style="color:#2d6cdf;text-decoration:none;">Contact</a>
        </footer>
        <script>
            function predictIntent() {
                const message = document.getElementById('message').value.trim();
                const resultDiv = document.getElementById('result');
                
                if (!message) {
                    alert('Please enter a message first!');
                    return;
                }
                
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = 'Predicting...';
                
                fetch('/predict', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({message: message})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        resultDiv.innerHTML = `<span style="color: red;">Error: ${data.error}</span>`;
                    } else {
                        resultDiv.innerHTML = `<span style="color: green;">Predicted Intent: ${data.intent || 'Unknown'}</span>`;
                    }
                })
                .catch(error => {
                    resultDiv.innerHTML = `<span style="color: red;">Error: ${error.message}</span>`;
                });
            }
        </script>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)