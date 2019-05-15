import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    responce = ec2.describe_addresses
    
    return(response)
