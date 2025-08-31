import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('url_mapping')


def generate_short_url(long_url):
    short_url = str(uuid.uuid4())[:8]  # 生成一个8位的短链接
    table.put_item(
        Item={
            'short_url': short_url,
            'long_url': long_url
        }
    )
    return short_url


def lambda_handler(event, context):
    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'])
        long_url = body['long_url']
        short_url = generate_short_url(long_url)
        return {
            'statusCode': 200,
            'body': json.dumps({'short_url': short_url})
        }
    elif event['httpMethod'] == 'GET':
        short_url = event['pathParameters']['short_url']
        response = table.get_item(
            Key={'short_url': short_url}
        )
        if 'Item' in response:
            return {
                'statusCode': 302,
                'headers': {'Location': response['Item']['long_url']}
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'error': 'Short URL not found'})
            }

    return {
        'statusCode': 400,
        'body': json.dumps({'error': 'Unsupported method'})
    }