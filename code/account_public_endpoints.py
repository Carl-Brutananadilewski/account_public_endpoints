import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    response_addresses = []
    addresses = ec2.describe_addresses()
    for eip_dict in addresses['Addresses']:
        response_addresses.append(eip_dict['PublicIp'])
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": ', '.join(response_addresses)
    }
    return(response)
