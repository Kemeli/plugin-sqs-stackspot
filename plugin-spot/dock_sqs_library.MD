Documentação do Plugin "Library_sqs"

O Plugin `Library_sqs` é uma biblioteca de manipulação do `Amazon Simple Queue Service (SQS)` que simplifica o gerenciamento de filas de mensagens. Com este plugin, você pode facilmente enviar, receber, manipular e excluir mensagens e dados em uma fila SQS.

### Uso Básico
`send_message(message_body)`<br>
Envio de mensagem para a fila SQS<br>

Envio de mensagem para a fila SQS fifo<br>
`send_messege_fifo(message_body)`<br>

Decebimento de mensagens disponível na fila SQS<br>
`response = receive_message()`<br>

### Manipulaçoes basicas
`get_firt_messagens(response)`<br>
Retorna a primeira mensagem da fila SQS<br>

`get_Attributes(firtMessage)`<br>
Retorna os atributos da mensagem<br>

`get_MessageId(firtMessage)`<br>
Retorna o id da mensagem<br>

`get_ReceiptHandle(firtMessage)`<br>
Retorna o receipt handle da mensagem<br>

`get_Body(firtMessage)`<br>
Retorna o corpo da mensagem<br>

`get_MD5OfBody(firtMessage)`<br>
Retorna o MD5 da mensagem<br>

`delete_message(receipt_handle(response))`<br>
Exclui uma mensagem da fila SQS<br>
