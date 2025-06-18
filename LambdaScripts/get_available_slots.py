import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Slots')

def lambda_handler(event, context):
    try:
        response = table.scan(
            FilterExpression='isBooked = :b',
            ExpressionAttributeValues={':b': False}
        )
        slots = response.get('Items', [])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PATCH, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "message": "Available slots fetched successfully",
                "data": slots
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PATCH, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }
