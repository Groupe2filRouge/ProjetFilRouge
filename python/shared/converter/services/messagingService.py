import requests
import json

#For credentials
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv('../.env')

# The service for messaging operations
class MessagingService():

    # Constructor
    def __init__(self):
        print("init MessagingService")

    # Format slack message
    def format_slack_message(self, data):
        blocks = [
            {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "New commit by: {}".format(data['commits'][0]['author']['name'])
            }
            },             
            {  
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "git_url: {}".format(data['repository']['git_url'])
            }
            }
        ]

        return self.post_message_to_slack("redacteur has pushed on GitHub !", blocks)
        

    # Post a given block message
    def post_message_to_slack(self, text, blocks = None):
        return requests.post('https://slack.com/api/chat.postMessage', {
            #'token': os.getenv('SLACK_TOKEN'),
            'token': os.getenv('SLACK_TOKEN'),
            'channel': 'C027BKQ8LSC',
            'text': text,
            'icon_emoji': ':see_no_evil:',
            'username': "botfilrouge",
            'blocks': json.dumps(blocks) if blocks else None
        }).json()	
