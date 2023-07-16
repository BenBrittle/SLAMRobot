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


def sendData(values):  # function to send data without interrupting other code
    s.sendall(values)
    data = s.recv(1024)  # checking to see if data gets received
    print(f'Received {data!r}')


Done = True

while Done == True:

    if keys.is_pressed('esc'):
        break
    oldKeysPressed = keysPressed  # this is to see if the keys have changed
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
    print(keysPressed, oldKeysPressed)
    if oldKeysPressed != keysPressed:
        print('test')
        if keysPressed[0]:
            if keysPressed[1]:
                wheelSpeeds = (1.75, 2)  # if forwards and left are pressed# then go full speed on the right
                # and half speed on the left
            elif keysPressed[2]:
                wheelSpeeds = (2, 1.75)
            else:
                wheelSpeeds = (2, 2)

        elif keysPressed[1]:
            wheelSpeeds = (1.25, 1.75)
        elif keysPressed[2]:
            wheelSpeeds = (1.75, 1.25)
        elif keysPressed[3]:
            wheelSpeeds = (1, 1)
        else:
            wheelSpeeds = (1.5, 1.5)

        wheelSpeedData = threading.Thread(target=sendData(wheelSpeeds), daemon=True)

s.shutdown(socket.SHUT_RDWR)
