import boto3

# The service for cloud operations
class CloudService():

    # Constructor
    def __init__(self):
        print("init CloudService")
        s3_client = boto3.client('s3')

    # Create a S3 bucket
    def createS3Bucket():
        session = boto3.session.Session()
        current_region = session.region_name
        # bucket_name = create_bucket_name("bucket_prefix_")
        bucket_name = "bucket"
        bucket_response = boto3.resource('s3').meta.client.create_bucket(
            Bucket="lebucketpythondalex",
            CreateBucketConfiguration={
            'LocationConstraint': current_region})
        print(bucket_name, current_region)
        return bucket_name