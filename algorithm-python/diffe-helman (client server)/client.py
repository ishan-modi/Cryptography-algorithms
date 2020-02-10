import socket
from random import randint

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = '172.20.10.3'
port = 12336
s.connect((IP_address, port))
message=''

message=s.recv(2048)
message=message.decode()			
print(message)
l1=list(map(int,message.split(",")))
p=l1[0]			
g=l1[1]
	
message=s.recv(2048)
message=message.decode()				
R1=int(message)
print("R1 = ",message)

y=randint(0,p)
print("Y = ",y)
message=str((g**y)%p)
print("R2 = ",message)		
s.send(message.encode())

print((R1**y)%p)
	
s.close()