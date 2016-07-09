# rc20161_02-rc20161_t1

Este repositório contém os trabalhos da disciplina de Redes de Computadores - 2016/1
do curso de Ciência da Computação da Universidade Federal de Pelotas.


## Trabalhos

**T1**: O primeiro trabalho consiste na definição de um protocolo para a camada de
aplicação e o desenvolvimento de uma aplicação *cliente-servidor*. Definição completa
disponível em: [t1_def](https://github.com/inessadl/rc20161_02/blob/master/t1_def.md)

**T2**: O segundo trabalho visa corrigir as falhas de segurança presentes no primeiro
trabalho. Adicionalmente, criar programas maliciosis para execução nas aplicações dos
colegas.


## Getting Started

Esta aplicação foi desenvolvida para o ambiente GNU/Linux. Adicionalmente, para rodá-la
em seu computador você deve ter o pacote *nodejs* instalado, e a versão 3.5.x do
Python (*python3.5.x*). Adicionalmente, para executar sob as condições de segurança propostas, *lshell* e *chroot*.


##1. Configurações de Segurança

Para execução do servidor e cliente, foi utilizado o ambiente *chroot* instalado no Ubuntu 16.04.
Através do chroot tem-se a instalação de uma distribuição Linux dentro de uma pasta do usuário. Esta
instalação possui todos os diretórios padrão (/bin, /etc, /dev, /home, /var, ...), porém, a visibilidade do sistema fica restrita à sua raiz.

Para exemplificar, temos:

/home/inessa/**trusty**.

Onde **/trusty** é o diretório que contém a distribuição Linux.

Dentro de *trusty* possuimos os seguintes diretórios:

    bin boot dev etc home lib lib64 media mnt opt proc root sbin srv sys tmp usr var

Desta forma, ao entrar no modo chroot, o usuário jamais teria acesso a pastas em hierarquia superior a estas.

Além disso, dentro do chroot foi instalado o **lshell**, que permite restringir o
acesso ao sistema. Neste trabalho o usuário pode executar apenas os comandos:

    $ node
    $ npm
    $ python
    $ python3.5

Dessa forma, garantimos que a aplicação poderá ser executada e os arquivos
recebidos do cliente não afetarão a máquina.

Links para instalação do chroot [aqui](http://packaging.ubuntu.com/pt-br/html/chroots.html) e [aqui](https://help.ubuntu.com/community/DebootstrapChroot). Lshell, [aqui](https://www.vivaolinux.com.br/dica/lshell-Limitando-ambiente-e-comandos-a-usuariosgrupos).

###1.1 chroot

Após a instalação através de algum dos links anteriores, ainda é preciso instalar mais alguns pacotes para garantir o funcionamento da aplicação. Para configurar o chroot, execute:

    $ sudo apt-get install update
    $ sudo apt-get install software-properties-common
    $ sudo apt-get install python3-software-properties (optional)
    $ sudo apt-get install build-essential
    $ sudo apt-get install gedit (optional)
    $ sudo apt-get install git (optional)
    $ sudo add-apt-repository ppa:git-core/ppa

Agora o chroot estará pronto para a instalação do nodejs:

    $ sudo apt-get install curl
    $ curl -sL https://deb.nodesource.com/setup_4.x | sudo bash -
    $ sudo apt-get install -y nodejs

###1.2 lshell

Após instalar o lshell dentro do chroot, substitua o arquivo /etc/lshell.config por [este](). Para o lshell funcionar corretamente, o usuário que for utilizá-lo precisa estar exclusivamente no grupo *lshell*.

Caso queira adicionar um novo usuário e diretamente inserí-lo neste grupo, execute:

    $ sudo useradd -g lshell <username>

##2. Execução

O cliente e o servidor devem ser executados em terminais diferentes, visto que irão rodar concomitantemente.

Abra uma janela do terminal e digite:

    $ python3.5 server.py

O servidor será iniciado e ficará aguardando conexões de clientes.

Então, abra uma segunda aba e digite:

    $ python3.5 client.py

A lista de comandos válidos está disponível na
[definição do protocolo](https://github.com/inessadl/rc20161_02/blob/master/Protocol.md) deste trabalho.


### Desenvolvedores

- André Alba - [@Deh-alba](https://github.com/Deh-alba)
- Inessa Luerce - [@inessadl](https://github.com/inessadl)

### Referências

- DebootstrapChroot - https://help.ubuntu.com/community/DebootstrapChroot
- Lshell - Limitando ambiente e comandos - https://www.vivaolinux.com.br/dica/lshell-Limitando-ambiente-e-comandos-a-usuariosgrupos
- NodeJS - http://nodejs.org
- NPM - https://www.npmjs.com
- Usando o chroot - http://packaging.ubuntu.com/pt-br/html/chroots.html
