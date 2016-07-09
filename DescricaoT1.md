# Trabalho 1 - Serviço de Aplicação

## Objetivo

Os alunos deverão desenvolver um cliente e um servidor para receber aplicações e executá-las localmente.

O servidor deve ser capaz de executar mais de uma aplicação em paralelo.

As aplicações a serem recebidas devem ser escritas em Javascript e Node. O servidor deve verificar as dependências usando o gerenciador de pacotes _npm_.

A linguagem de programação é de livre escolha, porém, o programa deve ser compilável e executável em GNU/Linux.


## Definição do protocolo da camada de aplicação

O protocolo para autenticação, envio das aplicações e obtenção dos resultados (saida padrão das aplicações) deverá ser definido em acordo pelos alunos.

**Sugestão:** usem protocolo TCP na camada de transporte.

## Produtos

* Definição do protocolo (por toda a turma) (1,5 pontos)
* Cliente para submeter aplicações (3,0 pontos)
* Servidor para executar aplicações (5,5 pontos)


## Cronograma

* Reuniões para definição do protocolo: 04, 07 e 11/04/2016
* Definição do protocolo (por toda a turma): 12/04/2016
* Submissão da versão final no _git_: 08/05/2016
* Apresentação do software: 09/05/2016

## Observações

Notem que o trabalho 2 envolverá desenvolver a segurança dos protocolos e aplicativos. Assim, não devem ser usados _SSL_ e _HTTPS_, nem outras técnicas que envolvam criptografia.

## Referências

* [Node.js] http://nodejs.org
* [npm] https://www.npmjs.com
