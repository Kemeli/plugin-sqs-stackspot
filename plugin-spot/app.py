from chalice import Chalice
import boto3
import uuid

ENDPOINT_URL_SEND ='http://host.docker.internal:4566'
ENDPOINT_URL_RECEIVE = "http://host.docker.internal:4566/_aws/sqs/messages"
QUEUE_URL = "http://queue.localhost.localstack.cloud:4566/000000000000"
QUEUE_NAME = 'MinhaFila'

app = Chalice(app_name='plugin-spot')
app.debug = True

def send_duplicate_message():
	message_body = "Hello World"
	sqs_client = boto3.client('sqs', endpoint_url=ENDPOINT_URL_SEND)

	# Gera um ID único para o atributo MessageDeduplicationId
	deduplication_id = str(uuid.uuid4())

	# Envia a primeira mensagem para a fila
	response = sqs_client.send_message(
		QueueUrl=f'{QUEUE_URL}/{QUEUE_NAME}',
		MessageBody=message_body,
		MessageDeduplicationId=deduplication_id
	)
	response = sqs_client.send_message(
		QueueUrl=f'{QUEUE_URL}/{QUEUE_NAME}',
		MessageBody=message_body,
		MessageDeduplicationId=deduplication_id
	)

@app.lambda_function()
def send_message(event, context):
	send_duplicate_message()
	return {"message": "Hello world!"}

# @app.on_sqs_message(queue='MinhaFila')
# def handler(event):
# 	for record in event:
# 		app.log.info("RECEIVED MESSAGE FROM SQS")
# 		app.log.info(record.body)

