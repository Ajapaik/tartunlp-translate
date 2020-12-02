import json
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('127.0.0.1', 12346))
client_socket.send(json.dumps({
    'src': 'Tere',
    'conf': ','
}).encode())
data = client_socket.recv(1024)
print(data.decode())
