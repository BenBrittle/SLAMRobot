import socket
import RPi.GPIO as GPIO

HOST = '0.0.0.0'
PORT = 3450

# GPIO setup
GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
leftPWM = GPIO.PWM(1, 50)
leftPWM.start(7.5)
rightPWM = GPIO.PWM(26, 50)
rightPWM.start(7.5)

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
