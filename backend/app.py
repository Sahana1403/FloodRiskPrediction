from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client
import numpy as np
import tensorflow as tf
from config import TWILIO_SID, TWILIO_TOKEN, TWILIO_PHONE

app = Flask(__name__)
CORS(app)

# Load model
model = tf.keras.models.load_model("flood_model")
twilio_client = Client(TWILIO_SID, TWILIO_TOKEN)

@app.route("/")
def home():
    return jsonify({"message": "FloodGuard API running"})

@app.route("/api/v1/forecast", methods=["POST"])
def forecast():
    data = request.json
    rain_seq = np.array(data["rain_seq"]).reshape(1, -1, 1)
    static_feat = np.array(data["static_feat"]).reshape(1, -1)
    pred = model.predict([rain_seq, static_feat])[0][0]
    return jsonify({"predicted_level": float(pred)})

@app.route("/api/v1/alert", methods=["POST"])
def send_alert():
    data = request.json
    message = data["message"]
    recipients = data["recipients"]
    for num in recipients:
        twilio_client.messages.create(body=message, from_=TWILIO_PHONE, to=num)
    return jsonify({"status": "sent"})

if __name__ == "__main__":
    app.run(debug=True)
