import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8000))


dataStr = input("Say something:")
s.send(dataStr.encode('utf-8'))

