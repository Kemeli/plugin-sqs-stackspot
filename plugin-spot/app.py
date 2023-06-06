from chalice import Chalice
import boto3

app = Chalice(app_name='plugin-spot')
app.debug = True

# @app.route('/')
# def index():
#     return {'hello': 'world'}

@app.on_sqs_message(queue='MinhaFila')
def handler(event):
	for record in event:
		app.log.info("RECEIVED MESSAGE FROM SQS")
		app.log.info(record.body)

