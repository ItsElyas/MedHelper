# backend/app.py
from flask import Flask, jsonify

app = Flask(__name__)  # creates a Flask app

@app.route("/")         # this sets the route
def home():             # when someone visits "/", run this
    return "Welcome to the MedTracker Backend!"


@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})

@app.route("/medicine")
def status():
    return jsonify({
        "medicine_taken": False,
        "time": "10:30 AM"
    })

if __name__ == "__main__":
    app.run(debug=True)