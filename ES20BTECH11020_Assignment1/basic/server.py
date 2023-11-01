import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).
Dict = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4','k5':'v5','k6':'v6'}


dst_ip = str(input("Enter Server IP: "))

s = socket.socket()
print ("Socket successfully created")

dport = 12346

s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")

while True:

	req,x = s.accept()
	print('Got request from',x)
	recreq = req.recv(1024).decode()
	div = recreq.split()


	if(div[0]=='PUT'):
		data = div[1].split("/")
		if(len(data)!=4 or data[0]!="" or data[1]!='assignment1'):
		   req.send(('HTTP/1.1 400 Bad Request\r\n\r\n').encode())
		else:
		   Dict[data[2]]=data[3]
		   req.send(('HTTP/1.1 '+data[2]+" : "+data[3]+' STORED 200 OK\r\n\r\n').encode())
	elif(div[0]=='DELETE'):
		if(div[1][13:] in Dict.keys()):
		   key = div[1].split("/")
		   del Dict[key[2]]
		   req.send(('HTTP/1.1 DELETED 200 OK\r\n\r\n').encode())

	else:
		data = div[1].split("=")
		if(len(data)!=2 or data[0]!='/assignment1?request'):
		   req.send(('HTTP/1.1 400 Bad Request\r\n\r\n').encode())
		else:
		   val = Dict[data[1]]
		   req.send(('HTTP/1.1 '+val+' 200 OK\r\n\r\n').encode())

	req.close()
  #break