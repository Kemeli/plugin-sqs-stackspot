#!/bin/bash

queue_name="MinhaFila"

# Executa o comando awslocal sqs get-queue-url e captura a saída e o código de retorno
output=$(awslocal sqs get-queue-url --queue-name "$queue_name" 2>&1)
return_code=$?

# Verifica o código de retorno do comando
if [ $return_code -ne 0 ]; then
  # Verifica se a mensagem de erro indica que a fila não existe
  if [[ $output == *"NonExistentQueue"* ]]; then
    echo "A fila não existe."
  else
    echo "Ocorreu um erro: $output"
  fi
else
  queue_url=$(echo "$output" | jq -r '.QueueUrl')
  echo "A fila existe. URL da fila: $queue_url"
fi
