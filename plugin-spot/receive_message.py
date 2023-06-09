import boto3

from config import QUEUE_URL, QUEUE_NAME, ENDPOINT_URL_RECEIVE

def receive_message(event, context):
    sqs = boto3.client('sqs', endpoint_url=ENDPOINT_URL_RECEIVE)
    response = sqs.receive_message(QueueUrl={QUEUE_URL}/{QUEUE_NAME})
    return str(response)

