# client.py
# !/usr/bin/env python
import socket
import json

TCP_IP = 'localhost'
TCP_PORT = 30000
BUFFER_SIZE = 1024


class Client:
    valor = 0

    def __init__(self):
        self.valor = 0

    def clientConnect():
        # create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = socket.gethostname()

        port = 30000

        # connection to hostname on the port.
        s.connect((host, port))

        # Receive no more than 1024 bytes
        tm = s.recv(1024)

        s.close()

        print("The time got from the server is %s" % tm)

    def clientThread(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        filename = 'testing.js'
        # filename = 'mytext.txt'     # file received
        f = open(filename, 'rb')
        print('sending data...')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                s.send(l)
                # print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                print('Successfully put the file')
                s.close()
                print('connection closed')
                break

print ("Iniciando Cliente")
print ("\n")

cliente = Client()
quit = 0     # variável auxiliar para controlar as repetições

# Menus para avaliar os comandos executados pelo usuário.

# Menu geral:
while quit != 1:
    print ("====================================")
    print ("Digite uma das instruções abaixo:")
    print ("USER - user myfile.json")
    print ("SEND - send myfile.js")
    print ("RUN - run")
    print ("QUIT - quit")
    print ("====================================")
    print ("")

    entrada = input("Digite a função desejada: ")

    # TODO autenticar usuário

    # Analisa os 5 primeiros caracteres e confere se o que foi digitado
    # pelo usuário corresponde aos comandos aceitos.
    if entrada[:5] == "user ":
        # Verifica se o arquivo de entrada possui a extensão json
        if entrada[len(entrada)-5:] == ".json":
            print ("Logando no servidor...")
            # print("return 100")
            # Receber o retorno do servidor em forma de um int o str aqui
            # servidor deve estar escutando função tipo recv()
            # sendto(string, address)
        else:
            print("[ERRO 303] - Arquivo em formato inválido.")
    elif entrada == "send": # verificar extensão
        print ("SEND")
        cliente.clientThread()
    elif entrada == "run":
        print ("Trying to run application...")
    elif entrada == "quit":
        print ("Fechando cliente!")
        quit = 1
    else:
        print ("Comando inválido")


'''    def clientThread(self):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            with open('received_file', 'wb') as f:
                print 'file opened'
                while True:
                    # print('receiving data...')
                    data = s.recv(BUFFER_SIZE)
                    print('data=%s', (data))
                    if not data:
                        f.close()
                        print 'file close()'
                        break
                    # write data to a file
                    f.write(data)

            print('Successfully get the file')
            s.close()
            print('connection closed')
'''
