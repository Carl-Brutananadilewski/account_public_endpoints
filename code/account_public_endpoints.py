import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    response = []
    addresses = ec2.describe_addresses()
    for eip_dict in addresses['Addresses']:
        response.append(eip_dict['PublicIp'])

    return(response)
