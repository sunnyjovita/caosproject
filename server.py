from socket import *
from threading import *

class ChatThread(Thread):
    def __init__(self, con):
        Thread.__init__(self)
        self.con=con
    def run(self):
        name=current_thread().getName()
        while True:
            if name=='Sender':
                data=input('Server')
                self.con.send(bytes(data, 'utf-8'))
            elif name=='Receiver':
                recData=self.con.recv(1024).decode()
                print('Client: ', recData)

server = socket(AF_INET, SOCK_STREAM)
server.bind(('127.0.0.1', 9000))
server.listen(4)

connection, address = server.accept()

sender = ChatThread(connection)
sender.setName('Sender')
receiver=ChatThread(connection)
receiver.setName('Receiver')

sender.start()
receiver.start()