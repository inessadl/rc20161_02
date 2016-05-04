# server.py
import socket
import time
import os
from threading import Thread
from SocketServer import ThreadingMixIn

TCP_IP = 'localhost'
TCP_PORT = 30000
BUFFER_SIZE = 1024

class Server:
    valor = 0

    def __init__(self):
        # construtor dos valores
        self.valor

    def connect(self):
        # create a socket object
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # get local machine name
        host = socket.gethostname()

        port = 30000

        # bind to the port
        serversocket.bind((host, port))

        # queue up to 5 requests
        serversocket.listen(5)

        while True:
            # establish a connection
            clientsocket, addr = serversocket.accept()

            print("Got a connection from %s" % str(addr))
            currentTime = time.ctime(time.time()) + "\r\n"
            clientsocket.send(currentTime.encode('ascii'))
            clientsocket.close()


# connection = Server()
# connection.connect()


class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print " New thread started for "+ip+":"+str(port)

    '''def run(self):
        filename = 'testing.js'
        # filename = 'mytext.txt'     # file received
        f = open(filename, 'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                # print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break
    '''
    def run(self):
        with open('testing.js', 'wb') as f:
            print 'file opened'
            while True:
                # print('receiving data...')
                data = self.sock.recv(BUFFER_SIZE)
                # print('data=%s', (data))
                if not data:
                    f.close()
                    print 'file close()'
                    break
                # write data to a file
                f.write(data)

        print('Successfully get the file')
        # Exemplo de como enviar qualque comando para o sistema.
	os.system("npm install")
        os.system("node testing.js")
        self.sock.close()
        print('connection closed')
        print "\n"


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print "Waiting for incoming connections..."
    # (conn, (ip, port)) = tcpsock.accept()
    conn, addr = tcpsock.accept()
    print 'Got connection from ', (TCP_IP, TCP_PORT)
    newthread = ClientThread(TCP_IP, addr, conn)
    newthread.start()
    threads.append(newthread)

for t in threads:
    t.join()
