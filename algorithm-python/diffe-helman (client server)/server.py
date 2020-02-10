import socket	
import math
from random import randint,choice
import Crypto

def genrandomprime():
	while(1):
		n=randint(0,1000)	
		if isprime(n):
			break
	return n

def isprime(n):
	if(n==0 or n==1):
		return False	
	for i in range(2,int(math.ceil((n+1)/2))):
		if(n%i==0):
			return False
	return True

def getgenerator(p):
    genlist=[]
    g=-1
    for i in range(2,p-1):
        l1=[False for i in range(0,p-1)]
        j=1
        while(1):
            ans=(i**j%p)
            if(l1[ans-1]==False):
                l1[ans-1]=True
                j+=1
                if(False not in l1):
                    genlist.append(i)
                    break
            else:
                break

    #if(len(genlist)>0):
     #   g=randint(0,len(genlist))
    
    g=choice(genlist)
    return int(g)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	
port = 12336
s.bind(('172.20.10.3',port))	
s.listen(1)	

while True:
    conn,addr = s.accept()
		
    print(str(addr) + "connected")

    p=genrandomprime()
    g=getgenerator(p)
        
    x=randint(0,p)
    print("X = ",x)
    msg=str(p)+","+str(g)
    conn.send(msg.encode())
    
    msg=str((g**x)%p)
    print("R1 = ",msg)
    conn.send(msg.encode())
    
    msg=conn.recv(2048)
    msg=int(msg.decode())
    print("R2 = ",msg)	
    print((msg**x)%p)
    	
    
    	
	
