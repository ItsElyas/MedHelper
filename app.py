from flask import Flask, render_template, request, redirect # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from datetime import datetime
app = Flask(__name__) # Create a Flask application

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicines.db' # Tells app where the database is located
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This suppresses a warning

db = SQLAlchemy(app)    #initilizes the database

class Medicine(db.Model):   #This creats a table called 'medicine
    id = db.Column(db.Integer, primary_key=True) # This is an int that references the ID each entry
    name = db.Column(db.String(100), nullable=False)
    dosage = db.Column(db.String(50), nullable=False)
    time = db.Column(db.Datetime, default=datetime.now(datetime.timezone.utc), nullable=True)   #FIX
    
    def __repr__(self):
        return f'<Medicine {self.name}>'

@app.route('/', methods=['POST', 'GET']) # Defines the route for the index page
def index():    # Function to handle requests to the index page
    if request.method == 'POST':
        #add medicine tags
        name = request.form['medicineName']
        dosage = request.form['medicineDose']
        
        if not name or not dosage:
            return redirect('/')
        
        exising_med = Medicine.query.filter_by(name = name).first()
        if exising_med:
            return redirect('/')
        
        new_medicine = Medicine(name=name, dosage=dosage)
        db.session.add(new_medicine)
        db.session.commit()
        return redirect('/')
    
    meds = Medicine.query.all()
    return render_template('index.html',medicines=meds)

@app.route('/delete/<int:id>')
def delete(id):
    



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
