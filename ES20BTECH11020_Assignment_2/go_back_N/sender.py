import socket
import struct
import time
import threading
import os

senderIP = "10.0.0.1"
senderPort   = 20001
recieverAddressPort = ("10.0.0.2", 20002)
bufferSize  = 1024 #Message Buffer Size

# Create a UDP socket at reciever side
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#socket_udp.settimeout(0.5)
timeout = 0.010

def add_segment(sq,flag):
	seg =struct.pack('!Hs',sq%2,bytes(flag,'utf-8'))
	return seg

while True:
	a = True
	data = f.read(1021)
	if data:
		seg = add_segment(sq,'c')
		packet = seg + data
	else:
		packet = add_segment(sq,'e')
		socket_udp.sendto(packet,recieverAddressPort)
		break
	
	socket_udp.sendto(packet,recieverAddressPort)
	t1 = threading.Thread(target=cnt,)
	t = threading.Thread(target=recvf,)
	t.start()
	t1.start()
	
	t.join()
	t1.join()
	print(str(ACK[0])+" "+str(sq))
	sq = sq + 1

f.close()