import socket
import sys

HOST = '0.0.0.0'
PORT = 3450

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(conn, addr)
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if not data:
                break
            conn.sendall(data)
print('done')
