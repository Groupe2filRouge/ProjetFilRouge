from flask import Flask, render_template, request

# Import services
from services.cloudService import CloudService
from services.converterService import ConverterService
from services.databaseService import DatabaseService
from services.messagingService import MessagingService
from services.gitService import GitService

# Instanciate services
cloudSrv = CloudService()
converterSrv = ConverterService()
databaseSrv = DatabaseService()
messagingSrv = MessagingService()
gitSrv = GitService()

# Create app Flask
app = Flask(__name__)

# The webhook adress for a git account
@app.route("/git-webhook/", methods=["POST"])
def webhook():
    # TODO - check for others git account (not only github)
    data = json.loads(request.data)
    print ("full_name: {}".format(data['repository']['full_name']))
    print ("html_url: {}.git".format(data['repository']['html_url']))
    print ("New commit by: {}".format(data['commits'][0]['author']['name']))

    gitSrv.clone("{}.git".format(data['repository']['html_url']))
    # converterSrv.convert()
    # cloudSrv.push("")

# The test adress for slack
@app.route("/testSlack", methods=["GET"])
def testSlack():
    return messagingSrv.testSlack();	

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host= '0.0.0.0')