import boto3
import json
from botocore.exceptions import EndpointConnectionError

ec2 = boto3.client('ec2')

def get_ips(region):
    get_ips_response_addresses=[]
    get_ips_session = boto3.session.Session(region_name=region)
    get_ips_client = get_ips_session.client('ec2')
    try:
        get_ips_account_addresses = get_ips_client.describe_addresses()
    except EndpointConnectionError:
        return 0
    for eip_dict in get_ips_account_addresses['Addresses']:
        get_ips_response_addresses.append(eip_dict['PublicIp'])
    return get_ips_response_addresses

def lambda_handler(event, context):

    response_body = {
                    "elastic_ips": {}
    }
    regions = []

    if event['multiValueQueryStringParameters']:
        if 'regions' in event['multiValueQueryStringParameters']:
            regions = event['multiValueQueryStringParameters']['regions']
    elif event['queryStringParameters']:
        if 'regions' in event['queryStringParameters']:
            regions = event['queryStringParameters']['regions']
    else:
        regions_describe = ec2.describe_regions()
        for region_json in regions_describe['Regions']:
            regions.append(region_json['RegionName'])


    for region in regions:
        region_ips = get_ips(region)
        if region_ips:
            response_body['elastic_ips'][region] = region_ips
        else:
            return(
                {
                    "statusCode": 404,
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                    },
                    "body": f"Region {region} not found\n"
                }
            )


    response = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(response_body)
    }
    print(response_body)
    return(response)
