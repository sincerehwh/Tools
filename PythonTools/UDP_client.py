import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data_str = input("say something:  ")

data = data_str.encode('utf-8')

s.sendto(data,('127.0.0.1',8000))
