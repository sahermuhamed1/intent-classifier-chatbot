# NOTE: Make sure the FastAPI server is running at http://localhost:8000 before starting this Flask app.
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

FASTAPI_URL = "http://localhost:8000/predict"

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    user_text = ""
    if request.method == "POST":
        user_text = request.form.get("user_text", "")
        if user_text:
            try:
                response = requests.post(FASTAPI_URL, json={"message": user_text})
                if response.status_code == 200:
                    prediction = response.json().get("intent", "Unknown")
                else:
                    prediction = "Error: Unable to get prediction."
            except requests.exceptions.ConnectionError:
                prediction = (
                    "Error: Could not connect to the FastAPI server at http://localhost:8000.<br>"
                    "Please make sure the FastAPI server is running.<br>"
                    "To start it, run:<br>"
                    "<code>python model/api/start_server.py</code> from the project root."
                )
            except Exception as e:
                prediction = f"Error: {str(e)}"
    return render_template("index.html", prediction=prediction, user_text=user_text)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Call FastAPI model server
        response = requests.post(FASTAPI_URL, json={'message': message})
        
        if response.status_code == 200:
            result = response.json()
            return jsonify({'intent': result.get('intent', 'Unknown')})
        else:
            return jsonify({'error': 'Model server error'}), 500
            
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Could not connect to FastAPI server. Make sure it\'s running on port 8000.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)