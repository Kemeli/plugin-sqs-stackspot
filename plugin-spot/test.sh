awslocal cloudformation delete-stack --stack-name wagratom
awslocal  cloudformation create-stack --stack-name wagratom --template-body file://sqs-stack.yaml
awslocal sqs get-queue-url --queue-name MinhaFila.fifo
