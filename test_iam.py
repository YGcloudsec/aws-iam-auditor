import boto3
iam = boto3.client('iam', region_name='us-east-1')
print(iam.list_users())
