import json
import boto3
import os

sns = boto3.client("sns")

TOPIC_ARN = os.environ["TOPIC_ARN"]

def lambda_handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])

        message = f"""
New Order Received

User: {body['user']}
Item: {body['item']}
Price: {body['price']}
"""

        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="Order Notification",
            Message=message
        )

    return {
        "statusCode": 200
    }