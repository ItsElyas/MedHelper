from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__) # Create a Flask application

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicines.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This suppresses a warning

db = SQLAlchemy(app)    #initilizes the database

class Medicine(db.Model):   #This creats a table called 'medicine
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(20), nullable=False)
    
    def __repr__(self):
        return f'<Medicine {self.name}>'

@app.route('/', methods=['GET', 'POST']) # Defines the route for the index page
def index():    # Function to handle requests to the index page
    if request.method == 'POST':
        #add medicine tags
    return render_template('index.html')



if __name__ == "__main__":
    app.run(debug=True)