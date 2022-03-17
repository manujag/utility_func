

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects_v2
import boto3

client = boto3.client('s3', aws_access_key_id='<your_access_key_id>',
                      aws_secret_access_key='<your_secret_access_key>',
                      region_name='us-east-1'
                      )


response = client.list_objects_v2(
    Bucket='bkt_name', Delimiter=r'/', MaxKeys=10, Prefix='in/this/folder/')

num_files = len(response['Contents'])
