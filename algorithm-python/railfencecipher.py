from numpy import *

def encrypt():
    cnt=0
    j=0
    for i in range(len(plaintext)):
            if(cnt%2==0):
                m[j,i]=plaintext[i]
                j+=1
                if(j==depth-1):
                    cnt+=1
                    continue
            else:
                m[j,i]=plaintext[i]
                j-=1
                if(j==0):
                    cnt+=1
                    continue
    print(m)

    encrypttext=""
    for i in range(depth):
        for j in range(len(plaintext)):
            if(m[i,j] != '?'):
                encrypttext+=m[i,j]

    return encrypttext


def decrypt(encrypttext):
    m[:]='?'
    cnt=0
    j=0
    for i in range(len(plaintext)):
            if(cnt%2==0):
                m[j,i]='*'
                j+=1
                if(j==depth-1):
                    cnt+=1
                    continue
            else:
                m[j,i]='*'
                j-=1
                if(j==0):
                    cnt+=1
                    continue
    print(m)

    k=0
    for i in range(depth):
        for j in range(len(plaintext)):
            if(m[i,j] == '*'):
                m[i,j]=encrypttext[k]
                k+=1

    print(m)

    decrypttext=""
    cnt=0
    j=0
    for i in range(len(plaintext)):
            if(cnt%2==0):
                decrypttext+=m[j,i]
                j+=1
                if(j==depth-1):
                    cnt+=1
                    continue
            else:
                decrypttext+=m[j,i]
                j-=1
                if(j==0):
                    cnt+=1
                    continue

    return decrypttext

f=open("plaintext.txt","r")
plaintext=f.read()
depth=int(input("Enter depth"))
if(len(plaintext)==depth):
    print("not valid key")
    exit(-1)

m=empty((depth,len(plaintext)),dtype="str")
m[:]='?'

enc=encrypt()
print(enc)

dec=decrypt(enc)
print(dec)

depth=2
choice="no"
while(choice=="no"):
    dec=decrypt(enc)
    print(dec)
    print(depth)
    choice=input("is it correct")
    depth+=1