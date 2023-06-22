import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.connect((HOST, PORT))

while True:
     data = s.recv(1024)
     message = data.decode('utf-8')
     print(data.decode('utf-8'))
     time.sleep(2)

     if message == 'Teste bem sucedido, Parabens!':
        break

s.close()
