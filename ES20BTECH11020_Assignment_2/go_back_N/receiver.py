import socket
import struct

recieverIP = "10.0.0.2"
recieverPort   = 20002
bufferSize  = 1024 #Message Buffer Size

# bytesToSend = str.encode(msgFromServer)
senderAddPort = ("10.0.0.1",20001)

# Create a UDP socket
socket_udp = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind socket to localIP and localPort
socket_udp.bind((recieverIP, recieverPort))

print("UDP socket created successfully....." )

def rem_segment(packet):
    n,f = struct.unpack('!Hs',packet)
    return [n,f]

f = open("image.jpg","wb")
sq=0

while True:
    msg,addr = socket_udp.recvfrom(bufferSize)
    fn=msg.strip()
    flag = msg[0:3]
    arr = rem_segment(flag)
    if(arr[1]=="e"):
        break
    else:
        data = msg[3:]
        if arr[0]==sq%2:
            f.write(data)
            sq=sq+1
        ack = str.encode(str(arr[0]))
        print(ack)
        socket_udp.sendto(ack, addr)
f.close()