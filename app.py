from flask import Flask, jsonify, render_template

app = Flask(__name__)  # creates a Flask app

@app.route("/")         # this sets the route
def home():             # when someone visits "/", run this
    return "Welcome to the MedTracker Backend!"

@app.route("/homepage")
def homepage():
    return render_template("home.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})

@app.route("/status")
def status():
    return jsonify({
        "medicine_taken": False,
        "time": "10:30 AM"
    })

if __name__ == "__main__":
    app.run(debug=True)