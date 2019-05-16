import boto3
import json

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    print(event)
    response_body = {
                    "elastic_ips": ""
    }
    response_addresses = []
    account_addresses = ec2.describe_addresses()
    for eip_dict in account_addresses['Addresses']:
        response_addresses.append(eip_dict['PublicIp'])
    response_body["elastic_ips"]=response_addresses
    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(response_body)
    }
    return(response)
