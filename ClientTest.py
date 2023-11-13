import socket
import threading

import keyboard
import keyboard as keys
import time

HOST = '192.168.1.88'
PORT = 3450

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # connecting to server
s.connect((HOST, PORT))
print('connected')

wheelSpeeds = [1.5, 1.5]
keysPressed = [False, False, False, False]
oldKeysPressed = keysPressed


def sendData(values):  # function to send data without interrupting other code
    values = str(values)
    s.sendall(values.encode())
    data = s.recv(1024)  # checking to see if data gets received
    print(f'Received {data!r}')


Done = True


while Done == True:
    key = False
    key = keyboard.read_key()

    if key == 'esc':
        break

    if key == 'up':
        keysPressed[0] = True
    else:
        keysPressed[0] = False

    if key == 'left':
        keysPressed[1] = True
    else:
        keysPressed[1] = False

    if key == 'right':
        keysPressed[2] = True
    else:
        keysPressed[2] = False

    if key == 'down':
        keysPressed[3] = True
    else:
        keysPressed[3] = False
    if oldKeysPressed != keysPressed:
        if keysPressed[0]:
            if keysPressed[1]:
                wheelSpeeds = [8.25, 5]  # if forwards and left are pressed# then go full speed on the right
                # and half speed on the left
            elif keysPressed[2]:
                wheelSpeeds = [10, 6.25]
            else:
                wheelSpeeds = [10, 5]

        elif keysPressed[1]:
            wheelSpeeds = [6.25, 6.25]
        elif keysPressed[2]:
            wheelSpeeds = [8.75, 8.75]
        elif keysPressed[3]:
            wheelSpeeds = [5, 10]
        else:
            wheelSpeeds = [7, 7]

        socketCon = threading.Thread(sendData(wheelSpeeds))
    oldKeysPressed = [keysPressed[0], keysPressed[1], keysPressed[2], keysPressed[3]]  # this is to see if the keys have changed

s.shutdown(socket.SHUT_RDWR)
