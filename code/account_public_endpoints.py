import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    response = {}
    response_addresses = []
    addresses = ec2.describe_addresses()
    for eip_dict in addresses['Addresses']:
        response_addresses.append(eip_dict['PublicIp'])
    response['elastic_ips'] = response_addresses
    return(response)
