import json
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('95.216.222.78', 12346))
client_socket.send(json.dumps({
    'src': 'Kaader filmist "Test3" 0:02:59.509',
    'conf': 'en,'
}).encode())
data = client_socket.recv(1024)
print(json.loads(data.decode())['final_trans'])
client_socket.close()

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('95.216.222.78', 12346))
client_socket.send(json.dumps({
    'src': 'Kaader filmist "Test3" 0:02:59.509',
    'conf': 'lv,'
}).encode())
data = client_socket.recv(1024)
print(json.loads(data.decode())['final_trans'])
client_socket.close()
