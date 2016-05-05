## Protocolo cliente-servidor para transferência de arquivos

### 1. Introdução

Este documento especifica um protocolo da camada de aplicação com arquitetura
*Cliente-Servidor* para transferência e execução de arquivos. Os serviços desse
protocolo rodam sobre TCP, que foi escolhido em virtude de oferecer transferência
confiável de dados. A porta utilizada pelo protocolo é a 30000.

- Porta padrão: 30000
- Arquitetura: Cliente-Servidor
- Protocolo na camada de transporte: TCP
- Padrão de caracteres: ASCII


### 2. Cliente e Servidor

A arquitetura utilizada neste protocolo é a *Cliente-Servidor*. Desta forma,
para que o cliente possa enviar algum comando ao servidor, será necessário
que uma conexão TCP (protocolo da camada de trasporte escolhido) já esteja
estabelecida entre os dois hosts. Desta forma, somente após a conexão for
estabelecida o cliente poderá enviar mensagens/comandos (descritos nas próximas
seções) deste protocolo ao servidor.


#### 2.1 O cliente

A função básica do cliente é enviar arquivos para o servidor. O servidor irá
aceitar arquivos no formatos Node ou JavaScript (.js) enviados pelo do usuário,
interpretar estes arquivos e retornar uma resposta relativa à interpretação do
arquivo e adicionalmente, uma mensagem relatando o sucesso ou erro no recebimento
do arquivo e em sua execução.

Como os dados devem ser enviados estão definidos no item 3.2 deste documento.

#### 2.2 O servidor

As funções básicas do servidor são a de aceitar conexões de múltiplos clientes,
aceitar os comandos e arquivos enviados pelos clientes. Ele também irá executar
os arquivos (se estiverem no formato adequado) e retornar o resultado da execução,
além de uma resposta relativa ao estado do envio e execução (sucesso ou erro).


### 3. Definição de comandos

Como a conexão entre o cliente e servidor já estará concreta, a comunicação entre
os dois hosts será através de comandos e retornos descritos a seguir.

Os comandos descritos nessa seção, são exclusivamente enviados pelo cliente ao
servidor. Os retornos descritos nessa seção são retornos enviados exclusivamente
do servidor para o cliente.

- **USER** - Comando para pedir autorização para conectar no servidor
- **SEND** - Comando para enviar um arquivo .js para execução no servidor
- **RUN** - Comando utilizado para executar o último arquivo enviado ao servidor
- **QUIT** - Comando utilizado para encerrar a conexão


### 3.1 - USER

Este comando é utilizado para a que o usuário faça a autenticação no servidor para
obter acesso (restrito de acordo com suas permissões) ao servidor.
O nome do usuário e sua senha deveram, obrigatoriamente, ser formados por caracteres
alfanuméricos.

#### 3.1.1 - Formato

```
user 	user.json
```

Exemplo do formato do arquivo JSON: user.json ->
```
{“usuario”:”<Meu_Usuario>”, “senha”:”<Minha_senha>”}
```


#### 3.1.2 - Retornos

- 100 - Conectado;  
- 101 - Não foi possível conectar;
- 102 - Usuário/senha incorretos;

#### 3.1.3 - Formato da mensagem

```
return <numero_do_retorno>
```

Ex:
```
return 101
```

### 3.2 - SEND

Comando utilizado para enviar arquivos para execução no servidor. O cliente poderá
enviar apenas um arquivo por vez, assim como a execução será restrita a um arquivo
por cliente simultaneamente. O arquivo que será executado no servidor consiste do
último envio válido (formato .js).


#### 3.2.1 - Formato

```
send <path_to_file>
```

Ex:
```
send toto.js
```

#### 3.2.2 - Retornos

- 200 - Arquivo recebido
- 201 - Erro ao receber o arquivo

#### 3.2.3 - Formato de mensagem

```
return <numero_do_retorno>
```

Ex.
```
return 200
```


### 3.3 - RUN

Comando utilizado para executar o último arquivo do usuário (cliente) enviado ao
servidor. Este comando poderá retornar, além de informações referentes a execução,
o resultado da aplicação executada (em formato .JSON).

#### 3.3.1 - Formato

```
run
```

#### 3.3.2 - Retornos

- 300 - Execução concluída com sucesso
- 301 - Erro ao executar o arquivo - verifique a sintaxe
- 302 - Erro: Arquivo não encontrado
- 303 - Erro: Arquivo em formato incompatível
- 304 - Erro: Dependências não encontradas
- 305 - Resultado

#### 3.3.3 - Formato da mensagem

```
return <numero_do_retorno>
```

Ex.

```
return 300

return 303
```

No caso do comando RUN, o único retorno que possui formato diferente é o retorno
305 que possui um parâmetro a mais e será detalhado na próxima subseção.

#### 3.3.4 - Retorno 305 - Resultado

O resultado é retornado ao cliente através de um arquivo no formato JSON. Neste
arquivo JSON estará contido a mensagem de retorno da execução da aplicação. O
formato para este retorno JSON é descrito a seguir:

Formato:
```
return 305 result.json
```

Conteúdo de result.json -> ```{ “result”: ”resultado_da_execucao_e_operacoes” }```

### 3.3 - QUIT

Comando utilizado para encerrar a conexão entre servidor e o cliente.

#### 3.3.1 - Formato

```
quit<parametro>
```

onde <parametro> pode ter valor 1 ou 2, sendo assim:

- quit 1 : Encerra a aplicação sem obter resultados
- quit 2 : Espera pelo resultado para encerrar a aplicação

Termina a execução, envia os retornos, e deleta os arquivos.


### 4. Descrição dos retornos

- 100 - Conectado
- 101 - Não foi possível conectar;
- 102 - Usuario/senha incorretos;
- 200 - Arquivo recebido;
- 201 - Erro ao receber o arquivo;
- 300 - Execução concluída com sucesso;
- 301 - Erro ao executar o arquivo - verifique a sintaxe
- 302 - Erro: Arquivo não encontrado
- 303 - Erro: Arquivo em formato incompatível
- 304 - Erro: Dependências não encontradas
- 305 - Resultado

### 5. Observações

-  Quando a execução de um arquivo .js encerrar, o servidor envia os retornos
correspondentes e deleta o arquivo
- Cada usuário poderá executar apenas uma aplicação (arquivo .js) no servidor
- O número máximo de arquivos sendo executados por cliente é 1
- O número máximo de clientes conectados ao servidor é 4
- Caso a conexão entre cliente-servidor seja perdida, todo o processo deverá ser
reiniciado. Desta forma, todos os arquivos deverão ser enviados novamente do
cliente ao servidor
- O tamanho máximo para o arquivo .js ser recebido é de 2Mb
