import time
import socket

for pings in range(10):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(1.0)
    message = b'badum TSSSSSSS'
    addr = ("127.0.0.1", 2077)

    start = time.time()
    client_socket.sendto(message, addr)
    try:
        data, server = client_socket.recvfrom(1024)
        end = time.time()
        timer = end - start
        print('--------------------------------------')
        print(data)
        print(pings)
        print(timer)
    except socket.timeout:
        print('--------------------------------------')
        print('REQUEST TIMED OUT')
        print('--------------------------------------')
