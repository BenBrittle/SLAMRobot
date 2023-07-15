import socket
import threading
import keyboard as keys

HOST = '127.0.0.1'
PORT = 3450

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # connecting to server
s.connect((HOST, PORT))
print('connected')

wheelSpeeds = (1.5, 1.5)
keysPressed = [False, False, False, False]


def sendData(values, sock):  # function to send data without interrupting other code
    s.sendall(values)
    data = s.recv(1024)  # checking to see if data gets received
    print(f'Received {data!r}')


def CheckKeys():
    while True:
        if keys.is_pressed('up'):
            keysPressed[0] = True
        else:
            keysPressed[0] = False

        if keys.is_pressed('left'):
            keysPressed[1] = True
        else:
            keysPressed[1] = False

        if keys.is_pressed('right'):
            keysPressed[2] = True
        else:
            keysPressed[2] = False

        if keys.is_pressed('down'):
            keysPressed[3] = True
        else:
            keysPressed[3] = False


Done = True

KeyCheck = threading.Thread(target=CheckKeys, args=(), daemon=True)
KeyCheck.start()

while Done == True:

    if keys.is_pressed('esc'):
        break

s.shutdown(socket.SHUT_RDWR)
