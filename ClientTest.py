import socket
import threading
import keyboard as keys

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

    if keys.is_pressed('esc'):
        break

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
    if oldKeysPressed != keysPressed:
        print('test')
        if keysPressed[0]:
            if keysPressed[1]:
                wheelSpeeds = [8.75, 10]  # if forwards and left are pressed# then go full speed on the right
                # and half speed on the left
            elif keysPressed[2]:
                wheelSpeeds = [10, 8.75]
            else:
                wheelSpeeds = [10, 10]

        elif keysPressed[1]:
            wheelSpeeds = [8.25, 8.75]
        elif keysPressed[2]:
            wheelSpeeds = [8.75, 6.25]
        elif keysPressed[3]:
            wheelSpeeds = [5, 5]
        else:
            wheelSpeeds = [7.5, 7.5]

        wheelSpeedData = threading.Thread(target=sendData(wheelSpeeds), daemon=True)
    oldKeysPressed = [keysPressed[0], keysPressed[1], keysPressed[2], keysPressed[3]]  # this is to see if the keys have changed

s.shutdown(socket.SHUT_RDWR)
