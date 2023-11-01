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

def recvf():
	global ACK
	global a
	global sq
	while a:
		ACK = socket_udp.recvfrom(1024)
		if(int(ACK[0])==sq%2):
		   a = False

def cnt():
	global a,packet,timeout,t_ct
	while a:
		time.sleep(timeout)
		if a:
			t_ct = t_ct+1
			socket_udp.sendto(packet,recieverAddressPort)




packet = ""
image = "testFile.jpg"
f = open(image,"rb")
sq=0
ACK = 1

#prerequisites
img_sz = os.path.getsize(image)
pckts = int(img_sz/1021)
t_init = time.time()
t_ct = 0

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
t_diff = time.time() - t_init
print(t_ct)
print(t_diff)
thro_put = img_sz/t_diff
print(thro_put)





