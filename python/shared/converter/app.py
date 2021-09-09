from flask import Flask, render_template, request
import json
import logging

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
log = logging.getLogger(__name__)


#delete selection
#myquery_to_delete = { "id" : "6126233411b0b7d0aaad0522" }

#insert collections
#databaseSrv.redacteurs.insert_many(liste_redacteurs)

#delete document in collection
#databaseSrv.redacteurs.delete_one(myquery_to_delete)

#delete all documents in collection
#databaseSrv.redacteurs.delete_many({})

# The webhook adress for a git account
@app.route("/github-webhook/", methods=["POST"])
def webhook():
    popup_text = "Un rédacteur vient de pousser du contenu sur GitHub"    
    data = json.loads(request.data)   
    redacteur = databaseSrv.get_redacteur_data("{}{}".format(data['repository']['clone_url'], data['repository']['ref']))  
    blocks = messagingSrv.format_slack_message(data, redacteur)    
    #import pdb;pdb.set_trace()   
    messagingSrv.post_message_to_slack(redacteur['slackToken'].strip('"'), redacteur['slackChannel'].strip('"'), popup_text, blocks);   

# The test adress for slack
@app.route("/testSlack", methods=["GET"])
def testSlack():
    return messagingSrv.format_slack_message();	

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host= '0.0.0.0', port=8080)