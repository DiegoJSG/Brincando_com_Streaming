import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.bind((HOST, PORT))
print(f'Aguardando conexão na porta : {PORT}')

s.listen(3)
conn, address = s.accept()

print(f'Recebendo solicitação de: {address}')

messages = [
     'Mensagem A',
     'Mensagem B',
     'Mensagem C',
     'Teste bem sucedido, Parabens!'
]

for index, message in enumerate(messages):
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(3)

    if index == len(messages) - 1:
        # Última mensagem, enviar sinalizador
        conn.send(bytes('Teste bem sucedido, Parabens!', 'utf-8'))

conn.close()

conn.close()