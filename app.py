from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) # Create a Flask application

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicines.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This suppresses a warning

db = SQLAlchemy(app)    #initilizes the database

@app.route('/') # Defines the route for the index page
def index():    # Function to handle requests to the index page
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)