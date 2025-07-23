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
    time = db.Column(db.Time, nullable=True)   #FIXED
    comments = db.Column(db.String(250), nullable=True)
    taken = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f'<Medicine {self.name}>'

@app.route('/', methods=['POST', 'GET']) # Defines the route for the index page
def index():    # Function to handle requests to the index page
    if request.method == 'POST':
        #add medicine tags
        name = request.form['medicineName']
        dosage = request.form['medicineDose']
        doseTime = request.form.get('timeToTake')
        notes = request.form['Notes']
        
        if not name or not dosage:
            return redirect('/')
        
        medicine_time = None
        if doseTime:
            try:
                medicine_time = datetime.strptime(doseTime, '%H:%M').time()
            except:
                print(f"Warning: Could not parse time ",{doseTime})

        
        # exising_med = Medicine.query.filter_by(name = name).first()
        # if exising_med:
        #     return redirect('/')
        
        new_medicine = Medicine(name=name, dosage=dosage, time=medicine_time, comments=notes)
        
        
        try:
            db.session.add(new_medicine)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an error adding your medication'
            
    else:
        meds = Medicine.query.all()
        totalMedications = Medicine.query.count()
        notes = [med.comments for med in meds]
        # Need to understand this ASAP
        sorted_meds = sorted(meds, key=lambda med: med.time if med.time is not None else datetime.min.time())
        return render_template('index.html', medicines=meds, orderedMeds=sorted_meds, totalMeds=totalMedications, medNotes=notes)

@app.route('/delete/<int:id>')
def delete(id):
    medToDelete = Medicine.query.get_or_404(id)
    
    try:
        db.session.delete(medToDelete)
        db.session.commit()
        return redirect('/')
    
    except:
        return 'There was a problem deleting your medications'
    
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    medToChange = Medicine.query.get_or_404(id)
    if request.method == 'POST': 
        medToChange.name = request.form['medicineName']
        medToChange.dosage = request.form['medicineDose']
        medToChange.time = request.form['timeToTake']
        
        try:
            db.session.commit()
            return redirect('/')    
            
        except:
            return 'There was a problem changing your medications'
    else:
        return render_template('index.html',medicines=medToChange)
        


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
