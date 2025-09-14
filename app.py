from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="frontend")
CORS(app)

# Serve frontend
@app.route('/')
def home():
    return send_from_directory(app.static_folder, "index.html")

# API route
@app.route('/api/check', methods=['POST'])
def check_symptoms():
    data = request.json
    age = data.get("age")
    symptoms = data.get("symptoms", [])

    risk = "Low"
    advice = "No serious issues."
    score = 20

    if "fever" in symptoms and "cough" in symptoms:
        risk = "Flu"
        advice = "Take rest and consult doctor if symptoms persist"
        score = 70
    elif "headache" in symptoms and "nausea" in symptoms:
        risk = "Migraine"
        advice = "Avoid triggers and consult neurologist"
        score = 60

    return jsonify({"risk": risk, "score": score, "advice": advice})

if __name__ == '__main__':
    app.run(debug=True)
