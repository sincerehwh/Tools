
import socket
from threading import Thread

def receiver():
	while  True:
		info = s.recvfrom(1024) 
		print(info)
		print('Receive from:%s:%s with:%s' %(info[1][0],info[1][0],info[0][0]))


def sender():
	while  True:
		send_str = input("what :")
		s.sendto(send_str.encode('utf-8'),(ip,port))


s = None
ip = ""
port = 8000

def main():

	global s
	global ip
	global port

	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((ip,port))

	th_r = Thread(target=receiver)
	th_s = Thread(target=sender)

	th_r.start()
	th_s.start()

	th_r.join()
	th_s.join()


if __name__ == "__main__":
	main()
