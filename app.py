from flask import Flask, render_template, request, redirect, jsonify # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from datetime import datetime, timedelta
app = Flask(__name__) # Create a Flask application


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///medicines.db' # Tells app where the database is located
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # This suppresses a warning

db = SQLAlchemy(app)    #initilizes the database

#This creates a table called Medicine for the database that stores all the data related to the medicine the user will take
class Medicine(db.Model):   
    id = db.Column(db.Integer, primary_key=True) # This is an int that references the ID each entry
    name = db.Column(db.String(100), nullable=False)    # Name of medicine
    dosage = db.Column(db.String(50), nullable=False)   # Dosage of medicine
    time = db.Column(db.Time, nullable=False)           # Time of dose for medicine
    comments = db.Column(db.String(250), nullable=True) # Comments for the medicine
    taken = db.Column(db.Boolean, default=False)        # If the med was taken that day
    missed = db.Column(db.Boolean, default=False)       # If the med wasnt taken that day
    
    def __repr__(self):
        return f'<Medicine {self.name}>'
# TODO: Must fix the time issue with the medicine showing how much time is left before taking the medicine
#INDEX ROUTE: This route is for the main page of the website. its use for it is for most of the data on the main page and 
# shows the data for the user like totalMeds taken, all meds, and the list of when to take the meds
@app.route('/', methods=['POST', 'GET']) # Defines the route for the index page
def index():
    current_time = datetime.now().strftime("%H:%M") # This is grabbing the current time but dont know how well it works   
    if request.method == 'POST':       # If the request method is post which it is since since we have the submit it grabs the data
        name = request.form['medicineName']
        dosage = request.form['medicineDose']
        doseTimeString = request.form.get('timeToTake')
        notes = request.form['Notes']
        
        if not name or not dosage:
            return redirect('/')
        #TODO: Make these variables not local so they can be used in the else to render template
        medicine_time = datetime.strptime(doseTimeString, '%H:%M').time()  # This is grabbing the dose time and converting it in hour : minuts
        # time_left = medicine_time - current_time

            
        new_medicine = Medicine(name=name, dosage=dosage, time=medicine_time, comments=notes)   # this is saving a new medicine with all the data the user added and saving it in the class and DB

        try:
            db.session.add(new_medicine)
            db.session.commit()
            return redirect('/')
        
        except:
            return 'There was an error adding your medication'
         
    else: # This else happens when the Post is done and now the data from the post will go here 
        meds = Medicine.query.all() # grabs all the medicine in the Med Class and saves it in meds
        totalMedications = Medicine.query.count()   # This just counts the meds and uses it for percentages
        med_times = [med.time for med in meds]
        notes = [med.comments for med in meds]      # saving all the notes for any meds that need them
        # Need to understand this ASAP
        sorted_meds = sorted(meds, key=lambda med: med.time if med.time is not None else datetime.min.time())
        upcoming_medsToday =[]
        return render_template('index.html', medicines=meds, orderedMeds=sorted_meds, totalMeds=totalMedications, medNotes=notes, medTimes = med_times, currentTime = current_time, medToEdit = None) # Puts all the data saved on the web

#DELETE ROUTE: This is for deleting the meds that are no longer being taking by the user
@app.route('/delete/<int:id>')
def delete(id):
    medToDelete = Medicine.query.get_or_404(id)     #grabs the med from the class using the id or gives the user an error
    
    try:
        db.session.delete(medToDelete)
        db.session.commit()
        return redirect('/')
    
    except:
        return 'There was a problem deleting your medications'

#!DOES NOT WORK:
# TODO : when clicked on then edit button it then hides all medications once showed and also opens and closes the form instantly
#EDIT ROUTE: Chooses the med you want to edit and changes what is saved in the database like the name time and dosage    
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    medToChange = Medicine.query.get_or_404(id)
    if request.method == 'POST': 
        medToChange.name = request.form['medicineName']
        medToChange.dosage = request.form['medicineDose']
        medToChange.time = datetime.strptime(request.form.get('timeToTake'), '%H:%M').time()
        
        try:
            db.session.commit()
            return redirect('/')    
            
        except:
            return 'There was a problem changing your medications'
    else:
        allMeds = Medicine.query.all()
        return render_template('index.html', medicines = allMeds, medToEdit=medToChange) 
    

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
