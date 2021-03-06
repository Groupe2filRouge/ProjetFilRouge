from flask import Flask, render_template, request

# Create app Flask
app = Flask(__name__)

# The main route
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # lien = request.form['git']
        return request.data
    return render_template('index.html')

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host= '0.0.0.0')