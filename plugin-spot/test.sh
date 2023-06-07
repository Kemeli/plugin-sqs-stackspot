# def send_duplicate_message():

# 	message_body = "Hello World"
# 	sqs_client = boto3.client('sqs', endpoint_url=ENDPOINT_URL_SEND)

# 	# Gera um ID único para o atributo MessageDeduplicationId
# 	deduplication_id = str(uuid.uuid4())

# 	# Envia a primeira mensagem para a fila
# 	response = sqs_client.send_message(
# 		QueueUrl=f'{QUEUE_URL}/{QUEUE_NAME}',
# 		MessageBody=message_body,
# 		MessageDeduplicationId=deduplication_id
# 	)
# 	response = sqs_client.send_message(
# 		QueueUrl=f'{QUEUE_URL}/{QUEUE_NAME}',
# 		MessageBody=message_body,
# 		MessageDeduplicationId=deduplication_id
# 	)
