# client.py
# !/usr/bin/env python
import socket

TCP_IP = 'localhost'
TCP_PORT = 30000
BUFFER_SIZE = 1024


class Client:
    valor = 0

    def __init__(self):
        # construtor dos valores
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

    def clientTherad(self):
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

cliente = Client()

cliente.clientTherad()