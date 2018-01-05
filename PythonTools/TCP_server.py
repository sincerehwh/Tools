import socket

# 创建套接字
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 监听端口
ip = '127.0.0.1'
s.bind((ip,8000))
# 设置最大监听数
s.listen(5)
print("server at %s is running..." % ip)

while True:
    sock,address = s.accept()
    print("Received ip:%s message:%s" % (address,sock) )

