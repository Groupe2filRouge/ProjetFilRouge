# Import the Flask module that has been installed.
from flask import Flask, jsonify, request
import json
from service.service import Service

# Creating a new "app" by using the Flask constructor. Passes __name__ as a parameter.
app = Flask(__name__)
serv = Service()

# Annotation that allows the function to be hit at the specific URL.
@app.route("/")
# Generic Python functino that returns "Hello world!"
def index():
    return "Hello world!"
    
# Annotation that allows the function to be hit at the specific URL. Indicates a GET HTTP method.
@app.route("/boardmachine/v1.0/machines", methods=["GET"])
# Function that will run when the endpoint is hit.

# curl http://localhost:5000/boardmachine/v1.0/machines

def get_machines():
    return serv.get_machines()
    
# Annotation that allows the function to be hit at the specific URL with a parameter. Indicates a GET HTTP method.
@app.route("/boardmachine/v1.0/machines/<string:hostname>", methods=["GET"])
# This function requires a parameter from the URL.

# curl http://localhost:5000/boardmachine/v1.0/machines/Web

def get_machine(hostname):
    return serv.get_machine(hostname)
    
@app.route("/boardmachine/v1.0/machines/<string:hostname>", methods=["DELETE"])
# This function requires a parameter from the URL.

# curl -X DELETE http://localhost:5000/boardmachine/v1.0/machines/ad

def delete_machine(hostname):
    return serv.delete_machine(hostname)
    
@app.route("/boardmachine/v1.0/machines/<string:hostname>", methods=["PUT"])
# This function requires a parameter from the URL.

# curl -X PUT -H "Content-Type: application/json" -d @update-machine.txt http://localhost:5000/bordmachine/v1.0/machines/python

def update_machine(hostname):
    return serv.update_machine(hostname, request.json)
    
@app.route("/boardmachine/v1.0/machines", methods=["POST"])
# This function requires a parameter from the URL.
# $ curl -X POST -H "Content-Type: application/json" -d @create-machine.txt http://localhost:5000/boardmachine/v1.0/machines

def add_machine():
    return serv.add_machine(request.json)

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host= '0.0.0.0')
