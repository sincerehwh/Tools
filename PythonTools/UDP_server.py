import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip = '127.0.0.1'
s.bind((ip,8000))

while True:
    data,add = s.recvfrom(1024)
    print('From ip: %s received data:%s '% (add,data.decode('utf-8')))



