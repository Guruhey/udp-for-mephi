import random
import socket

#udp socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('', 2077))

while True:
    rand = random.randint(0, 10)
    #poluchau i address i mess
    message, address = server_socket.recvfrom(1024)
    message = message.upper()
    if rand >= 4:
        server_socket.sendto(message, address)