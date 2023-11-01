import socket

cacheIP = "10.0.1.2"

dst_ip = str(input("Enter dstIP: "))
s = socket.socket()

print(dst_ip)

port = 12346

s.connect((dst_ip, port))

request = str(input('ENTER REQUEST'))
if(request=='GET'):
	key = str(input('ENTER KEY'))
	s.send(('GET /assignment1?request='+key+' HTTP/1.1\r\n\r\n').encode())
else:
	key = input('ENTER KEY:')
	val = input('ENTER VAL:')
	s.send(('PUT /assignment1/'+key+"/"+val+' HTTP/1.1\r\n\r\n').encode())

response = s.recv(1024).decode()
print(response)
s.close()

