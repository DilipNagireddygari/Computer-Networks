import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).


cache = {}


dst_ip = str(input("Enter Cache IP: "))

s = socket.socket()
print ("Socket successfully created")

dport = 12346


s.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

s.listen(5)
print ("socket is listening")



while(True):

  serverIP = "10.0.1.3"

  dst_ip1 = str(input("Enter Server IP: "))
  t = socket.socket()
  port = 12346

  print(dst_ip1)


  t.connect((dst_ip1, port))

  req,x = s.accept()
  print('Got request from',x)
  recreq = req.recv(1024).decode()

  div = recreq.split()

  
  if(div[0]=='PUT'):
     t.send(recreq.encode())
     print('Put request sent to Server')
     serRes = t.recv(1024).decode()
     req.send(serRes.encode())
  else:
     data = div[1].split("=")
     if data[1] in cache.keys():
        req.send(('HTTP/1.1 val: '+cache[data[1]]+' 200 OK\r\n\r\n').encode())
     else:
        t.send(recreq.encode())
        print('Get request sent to Server')
        serRes = t.recv(1024).decode()
        check = serRes.split()
        cache[check[2]]=check[3]
        req.send(serRes.encode())


  req.close()