import json
from endpoints import *

def lambda_handler(event, context):
    print(event)
    print(context)
    path = event['path'][1:]
    try:
        body = json.loads(event['body'])
    except:
        pass
    statusCode = 200
    if path == 'get_totals':
        result = get_totals()
    elif path == 'table':
        result = get_table_data()
    elif path == 'submit_inventory':
        result = submit_inventory(body)
    elif path == 'submit_order':
        result = submit_order(body)
    elif path == 'submit_sale':
        result = submit_sale(body)
    else:
        statusCode = 503
        result = f'{path} is not a valid endpoint'

    return { 
        'statusCode': statusCode,
        'body': json.dumps(result)
    }