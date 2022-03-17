

# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_objects_v2

import boto3


location_to_delete_from = 'delete/from/here'
bucket_name = '<bucket>'
max_obj_count = 100  # max keys to look for and then delete
client = boto3.client('s3', aws_access_key_id='<your_access_key_id>',
                      aws_secret_access_key='<your_secret_access_key>',
                      region_name='us-east-1'
                      )


response = client.list_objects_v2(
    Bucket=bucket_name, Delimiter=r'/', MaxKeys=10, Prefix=location_to_delete_from)

keys_to_delete = [i['Key'] for i in response['Contents']]
keys_to_delete = [{'Key': i} for i in keys_to_delete]

response = client.delete_objects(Bucket=bucket_name, Delete={
                                 'Objects': keys_to_delete, 'Quiet': True})
