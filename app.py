from flask import Flask, render_template

app = Flask(__name__) # Create a Flask application

@app.route('/') # Defines the route for the index page
def index():    # Function to handle requests to the index page
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)