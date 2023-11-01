import socket

#WRITE CODE HERE:
#1. Create a KEY-VALUE pairs (Create a dictionary OR Maintain a text file for KEY-VALUES).
Dict = {'k1':'v1','k2':'v2','k3':'v3','k4':'v4','k5':'v5','k6':'v6',}


dst_ip = str(input("Enter Server IP: "))

t = socket.socket()
print ("Socket successfully created")

dport = 12346

t.bind((dst_ip, dport))
print ("socket binded to %s" %(dport))

t.listen(5)
print ("socket is listening")

while True:

  k,x = t.accept()
  print('Got request from',x)
  recreq = k.recv(1024).decode()
  div = recreq.split()
  print(div)


  if(div[0]=='PUT'):
     data = div[1].split("/")
     print(data)
     Dict[data[2]]=data[3]
     k.send(('HTTP/1.1 PUT '+data[2]+" : "+data[3]+' 200 OK\r\n\r\n').encode())
  else:
     data = div[1].split("=")
     val = ""
     if data[1] not in Dict.keys():
      k.send(('HTTP/1.1 Value not found 400 Bad request\r\n\r\n'))
     else:
      val = Dict[data[1]]
      k.send(('HTTP/1.1 GET '+data[1]+" "+val+' 200 OK\r\n\r\n').encode())

  k.close()