from chalice import Chalice
import boto3
import uuid

ENDPOINT_URL_SEND ='http://host.docker.internal:4566'
ENDPOINT_URL_RECEIVE = "http://host.docker.internal:4566/_aws/sqs/messages"
QUEUE_URL = "http://queue.localhost.localstack.cloud:4566/000000000000"
QUEUE_NAME = 'MinhaFila.fifo'
REGION = 'us-east-1'

sqs_client = boto3.client('sqs', endpoint_url=ENDPOINT_URL_SEND, region_name=REGION)

app = Chalice(app_name='plugin-spot')
app.debug = True

def send_messege_fifo(id, deduplication_id, message_body):
	message_body = "Hello World"
	deduplication_id = str(uuid.uuid4())
	id = str(uuid.uuid4())
	response = sqs_client.send_message(
		QueueUrl=f'{QUEUE_URL}/{QUEUE_NAME}',
		MessageBody=message_body,
		MessageDeduplicationId=deduplication_id,
		MessageGroupId=id
	)

def send_messege(message_body):
	response = sqs_client.send_message(
		QueueUrl=f'{QUEUE_URL}/{QUEUE_NAME}',
		MessageBody=message_body,
	)

def receive_message():
	sqs = boto3.client('sqs', endpoint_url=ENDPOINT_URL_RECEIVE)
	response = sqs.receive_message(
		QueueUrl=f'{QUEUE_URL}/{QUEUE_NAME}')
	return response

def get_firt_messagens(response):
	if 'Messages' in response:
		return str(response['Messages'][0])
	return (None)

def get_Attributes(response):
	attributes = response['Messages'][0]['Attributes']
	return attributes

def get_MessageId(response):
	attributes = response['Messages'][0]['MessageId']
	return attributes

def get_ReceiptHandle(response):
	attributes = response['Messages'][0]['ReceiptHandle']
	return attributes

def get_Body(response):
	attributes = response['Messages'][0]['Body']
	return attributes

def get_MD5OfBody(response):
	attributes = response['Messages'][0]['MD5OfBody']
	return attributes

def delete_message(receipt_handle):
	response = sqs_client.delete_message(
		QueueUrl=f'{QUEUE_URL}/{QUEUE_NAME}',
		ReceiptHandle=receipt_handle
	)
	return response
