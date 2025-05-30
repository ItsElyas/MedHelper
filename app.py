from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)  # creates a Flask app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medtracker.db'  # SQLite database
db = SQLAlchemy(app)  # initializes the database
# Define your database models here

class Medicine(db.Model):
     id = db.Column(db.Integer, primary_key=True)  
     name = db.Column(db.String(150), nullable=False)
     date_created = db.Column(db.DateTime, default = datetime.utcnow)  
   
     def __repr__(self):
        return f'<Medicine {self.name}>'

@app.route("/")         # this sets the route
def route():             # when someone visits "/", run this
    return "Welcome to the MedTracker Backend!"

@app.route("/homepage")
def homepage():
    return render_template("home.html")

@app.route("/medicine")
def medicine():
    return render_template("medicine.html")

@app.route("/about")
def about():
    return render_template("about.html")

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