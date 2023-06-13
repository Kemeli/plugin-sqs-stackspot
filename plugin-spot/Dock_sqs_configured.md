## plugin Create_QUEUE

O Plugin "Create_QUEUE" é uma ferramenta que permite a criação e configuração de filas SQS (Simple Queue Service) com facilidade. Com diversas opções de configuração disponíveis, esse plugin oferece flexibilidade e controle sobre o comportamento das filas. A seguir, apresentamos as principais propriedades do Plugin "Create_QUEUE":
```
QueueName:
Descrição: Nome da fila SQS.
Tipo: String.
```
```
DelaySeconds:
Descrição: Tempo de atraso, em segundos, para colocar mensagens na fila.
Tipo: Inteiro.
```
```
MessageRetentionPeriod:
Descrição: Período de retenção das mensagens na fila, em segundos.
Tipo: Inteiro.
```
```
MaximumMessageSize:
Descrição: Tamanho máximo, em bytes, para uma mensagem.
Tipo: Inteiro.
```
```
VisibilityTimeout:
Descrição: Tempo máximo, em segundos, que uma mensagem permanece invisível após ser recebida.
Tipo: Inteiro.
```
```
FifoQueue:
Descrição: Indica se a fila é uma FIFO (First-In-First-Out).
Tipo: Booleano.
```
```
ReceiveMessageWaitTimeSeconds:
Descrição: Tempo, em segundos, para esperar por uma mensagem disponível quando a fila está vazia.
Tipo: Inteiro.
```
```
DuplicateMessageDetection:
Descrição: Indica se a detecção de mensagens duplicadas está ativada.
Tipo: Booleano.
```
```
ContentBasedDeduplication:
Descrição: Indica se a deduplicação baseada em conteúdo está ativada.
Tipo: Booleano.
```
