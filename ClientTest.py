import socket
import keyboard as keys

HOST = '127.0.0.1'
PORT = 3450

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # connecting to server
s.connect((HOST, PORT))


data = s.recv(1024)  # checking to see if data gets received
print(f'Received {data!r}')
