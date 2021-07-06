#cloner => fait dans une méthode (index())
#convertir en html (respect arborescence) => fait dans convert() sans respect de l'arborescence.

#faire table des matières dans un second temps

#le clone et la conversion se font dans un répertoir temporaire qu'il faut supprimer après traitement.

#Rassembler le clone et la conversion en une seule fonction.


from flask import Flask, render_template, request
#from git import Repo
import markdown
import boto3

import subprocess

import uuid

import requests
import json

app = Flask(__name__)

WELCOME_BLOCK = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": (
            "Welcome to Slack! :wave: We're so glad you're here. :blush:\n\n"
            "*Get started by completing the steps below:*"
        ),
    },
}

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lien = request.form['git']
        subprocess.Popen(['git', 'clone', str(lien), '/home/vagrant/tmp/clone'])
        return lien
    return render_template('index.html')

# @app.route("/clone/<string:adress>", methods=["GET"])
@app.route("/md", methods=["GET"])
def convert():
    with open('/home/vagrant/tmp/clone/README.md', 'r') as f:
        text = f.read()
        html = markdown.markdown(text)

    with open('/home/shared/tmp/README.html', 'w') as f:
        f.write(html)

    return "ok"

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

@app.route("/cs3", methods=["GET"])
def cs():
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name("bucket_prefix_")
    bucket_response = boto3.resource('s3').meta.client.create_bucket(
        Bucket="lebucketpythondalex",
        CreateBucketConfiguration={
        'LocationConstraint': current_region})
    print(bucket_name, current_region)
    return bucket_name

@app.route("/push/<string:bucket>", methods=["GET"])
def push(bucket):
    s3_client = boto3.client('s3')
    s3_client.upload_file("/home/shared/tmp/README.html", "lebucketpythondalex", "keyfilename")
    return "ok"

@app.route("/github-webhook/", methods=["POST"])
def test():
    # print(request.data)
    data = json.loads(request.data)
    print ("full_name: {}".format(data['repository']['full_name']))
    print ("html_url: {}.git".format(data['repository']['html_url']))
    print ("New commit by: {}".format(data['commits'][0]['author']['name']))
    
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Welcome to Slack! :wave: We're so glad you're here. :blush:\n\n*Get started by completing the steps below:*",
            },
        },
        {"type": "divider"},
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ":white_large_square: *Add an emoji reaction to this message* :thinking_face:\nYou can quickly respond to any message on Slack with an emoji reaction. Reactions can be used for any purpose: voting, checking off to-do items, showing excitement.",
            },
        },
        {
            "type": "context",
            "elements": [
                {
                    "type": "mrkdwn",
                    "text": " :information_source: *<" + data['repository']['html_url'] +"|Learn How to Use Emoji Reactions>*",
                }
            ],
        }
    ]
    
               
    return post_message_to_slack("Text shown in popup.", blocks);

@app.route("/slack", methods=["GET"])
def slack():
    # return requests.post('https://slack.com/api/chat.postMessage', {
    #     'token': ,
    #     'channel': ,
    #     'icon_emoji': ":robot_face:",
    #     'username': "botfilrouge",
    #     "blocks": [
    #         json.dumps({
    #             "type": "section",
    #             "text": {
    #                 "type": "mrkdwn",
    #                 "text": "Hello, Assistant to the Regional Manager Dwight! *Michael Scott* wants to know where you'd like to take the Paper Company investors to dinner tonight.\n\n *Please select a restaurant:*"
    #             }
    #         })
    #     ],
    # }).json()
    blocks = [
        {  
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hello, Assistant to the Regional Manager Dwight! *Michael Scott* wants to know where you'd like to take the Paper Company investors to dinner tonight.\n\n *Please select a restaurant:*"
        }
        }
    ]

    return post_message_to_slack("Text shown in popup.", blocks);


def post_message_to_slack(text, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': 'xoxb-1883936723840-2238634768673-GXejjanSfJHnQELVQmzXihW7',
        'channel': 'C027BKQ8LSC',
        'text': text,
        'icon_emoji': ':see_no_evil:',
        'username': "botfilrouge",
        'blocks': json.dumps(blocks) if blocks else None
    }).json()	

# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host= '0.0.0.0')
