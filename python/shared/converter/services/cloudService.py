import boto3
import os
import json
import base64
import hashlib

# The service for cloud operations
class CloudService():

    # Constructor
    def __init__(self): #à quoi sert cette fonction ?
        print("init CloudService")
        self.s3_client = boto3.client('s3')
        website_configuration = {'IndexDocument': {'Suffix': 'README.html'}}
        bucket_name="test-site-enzo"
        self.s3_client.put_bucket_website(Bucket='test-site-enzo', WebsiteConfiguration=website_configuration)
        bucket_policy = {'Version': '2012-10-17','Statement': [{'Sid': 'AddPerm','Effect': 'Allow','Principal': '*','Action': ['s3:GetObject'],'Resource': "arn:aws:s3:::%s/*" % bucket_name}]}
        bucket_policy = json.dumps(bucket_policy)
        self.s3_client.put_bucket_policy(Bucket="test-site-enzo", Policy=bucket_policy)
        #self.bucket = self.s3_client.Bucket('test-site-enzo')

    # Push from local file to cloud storage
    #def push(self, bucket): #argument bucket sera utile quand on aura la BDD
    def push(self):
        #s3_client.upload_file("/home/shared/tmp/README.html", "lebucketpythondalex", "keyfilename")
        destination=""
        bucket="test-site-enzo"
        path="/home/shared/converter/tmp"
        #for subdir, dirs, files in os.walk(path):  #relit récursivement le dossier des fichiers html pour le upload un par un dans une boucle
            #for file in files:
               # full_path = os.path.join(subdir, file) #semble concaténer le nom de fichier et le chemin
               # with open(full_path, 'rb') as data: #2 lignes trouvées sur Internet, par trop sûr de comment ça marche ¯\_(ツ)_/¯
                    #self.bucket.put_object(Key=full_path[len(path)+1:], Body=data)
                #self.s3_client.upload_file(full_path, "test-site-enzo", file) #ne marche pas
        for root, dirs, files in os.walk(path):

            for filename in files:

                # construct the full local path
                local_path = os.path.join(root, filename)

                # construct the full Dropbox path
                relative_path = os.path.relpath(local_path, path)
                s3_path = os.path.join(destination, relative_path)

                # relative_path = os.path.relpath(os.path.join(root, filename))

                #print 'Searching "%s" in "%s"' % (s3_path, bucket)
                try:
                    self.s3_client.head_object(Bucket=bucket, Key=s3_path)
                    #print "Path found on S3! Skipping %s..." % s3_path

                    # try:
                        # client.delete_object(Bucket=bucket, Key=s3_path)
                    # except:
                        # print "Unable to delete %s..." % s3_path
                except:
                    #print "Uploading %s..." % s3_path
                    #self.s3_client.upload_file(local_path, bucket, s3_path, ExtraArgs={'ACL': 'public-read'} )
                    data=open(local_path,"rb")
                    print(s3_path)
                    self.s3_client.upload_fileobj(data, bucket, s3_path, ExtraArgs={'ACL': 'public-read'})
                    #md = hashlib.md5(data.read().encode('utf-8')).digest()
                    #contents_md5 = base64.b64encode(md).decode('utf-8')
                    #self.s3_client.put_object(Body=data, Bucket='test-site-enzo', Key=s3_path, ContentType='text/html', ContentMD5=contents_md5)
                     

        return "file uploaded"