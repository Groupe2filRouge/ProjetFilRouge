import boto3
import os
import json
import base64
import hashlib

# The service for cloud operations
class CloudService():

    # Constructor
    def __init__(self):
        print("init CloudService")
        self.s3_client = boto3.client('s3')
        website_configuration = {'IndexDocument': {'Suffix': 'README.html'}}
        bucket_name="test-site-enzo"
        self.s3_client.put_bucket_website(Bucket='test-site-enzo', WebsiteConfiguration=website_configuration)
        bucket_policy = {'Version': '2012-10-17','Statement': [{'Sid': 'AddPerm','Effect': 'Allow','Principal': '*','Action': ['s3:GetObject'],'Resource': "arn:aws:s3:::%s/*" % bucket_name}]}
        bucket_policy = json.dumps(bucket_policy)
        self.s3_client.put_bucket_policy(Bucket="test-site-enzo", Policy=bucket_policy)
        

    # Push from local file to cloud storage
    #def push(self, bucket): #argument bucket sera utile quand on aura la BDD
    def push(self):
        destination=""
        bucket="test-site-enzo"
        path="/home/shared/converter/tmp"
        # Du code copié d'Internet, ça ne marche qu'à moitié et je ne saurais pas vraiment expliquer comment ou pourquoi ¯\_(ツ)_/¯ 
        for root, dirs, files in os.walk(path):

            for filename in files: #Voir de tester le nombre d'itérations vraiment faites...
                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, path)
                s3_path = os.path.join(destination, relative_path)

                try:
                    self.s3_client.head_object(Bucket=bucket, Key=s3_path)
                except:
                    data=open(local_path,"rb")
                    #self.s3_client.upload_fileobj(data, bucket, s3_path, ExtraArgs={'ACL': 'public-read','Metadata': {'Content-Type': 'text/html'}})
                    self.s3_client.put_object(Key=s3_path,Body=data,Bucket=bucket,ContentType='text/html') #rajouté : Body=data
                    
        return "file uploaded"