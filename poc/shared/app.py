from flask import Flask, render_template, request
from git import Repo
import markdown
import boto3

import subprocess

import uuid

app = Flask(__name__)

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


# Checks to see if the name of the package is the run as the main package.
if __name__ == "__main__":
    # Runs the Flask application only if the main.py file is being run.
    app.run(host= '0.0.0.0')