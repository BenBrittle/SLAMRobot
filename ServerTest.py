import socket
import RPi.GPIO as GPIO

HOST = '0.0.0.0'
PORT = 3450

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
leftPWM = GPIO.PWM(12, 50)
leftPWM.start(7.2)
rightPWM = GPIO.PWM(32, 50)
rightPWM.start(7.2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    # start listening on network
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(conn, addr)
        while True:
            data = conn.recv(20)
            conn.sendall(data)
            data = data.decode()
            if not data:
                break
            try:
                data = eval(data)
            except:
                print('error')
                break
            print(data[0])
            leftPWM.ChangeDutyCycle(float(data[0]))
            rightPWM.ChangeDutyCycle(float(data[1]))
print('done')
