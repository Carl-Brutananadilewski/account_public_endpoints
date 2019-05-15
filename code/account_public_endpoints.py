def lambda_handler(event, context):
    print(event)
    print(context)
    response = {
        "statusCode": 200,
        "headers": {
          'Content-Type': 'text/html; charset=utf-8'
        },
        "body": '<p>Hello world!</p>'
        }
    return(response)
