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
var = 0
while var != 1:
    print("Use um dos comandos disponíveis")
    print ("USER")
    print ("SEND")
    print ("RUN")
    print ("QUIT")

    entrada = input("Digite a função desejada:")

    if entrada[:5] == "USER ":
        # confere para ver se o arquivo de entrada é um json
        if entrada[len(entrada)-5:] == ".json":
            print ("Logando no servidor...")
            # Receber o retorno do servidor em forma de um int o str aqui
            # servidor deve estar escutando função tipo recv()
            # sendto(string, address)
        else:
            print("Arquivo de entrada invalido!")
    elif entrada == "SEND":
        print ("SEND")
        cliente.clientThread()
    elif entrada == "RUN":
        print ("RUN")
    elif entrada == "QUIT":
        print ("Fechando cliente!")
        var = 1
    else:
        print ("Comando desconhecido")


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
