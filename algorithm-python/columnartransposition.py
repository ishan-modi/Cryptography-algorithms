from numpy import *
import math


def encrypt():
    k = 0
    for x in range(i):
        for y in range(j):
            if (k < len(plaintext)):
                m[x, y] = plaintext[k]
                k += 1

    k = 0
    for y in key1:
        for x in range(i):
            m1[x, k] = m[x, y - 1]
        k += 1

    print(m1)

    encrypttext = ""
    for x in range(j):
        for y in range(i):
            encrypttext += m1[y, x]
    print(encrypttext)


def decrypt():
    key2 = [-1 for x in range(len(key1))]

    for x in range(len(key1)):
        key2[key1[x] - 1] = x + 1

    print(key2)

    k = 0
    for y in key2:
        for x in range(i):
            m2[x, k] = m1[x, y - 1]
        k += 1

    print(m2)

    encrypttext = ""
    for x in range(i):
        for y in range(j):
            encrypttext += m2[x, y]
    print(encrypttext)

f=open("plaintext.txt","r")
plaintext=f.read()

key=input("Enter a key")
l1=[]
l1=sorted(key)
key1=[]
for i in key:
    for j in range(len(l1)):
        if(l1[j]==i):
            key1.append((j+1))

print(key1)
i=math.ceil(len(plaintext)/len(key1))
j=len(key1)
m=empty((i,j),dtype="str")
m[:]="?"
m1=empty((i,j),dtype="str")
m1[:]="?"
m2=empty((i,j),dtype="str")
m2[:]="?"
encrypt()
decrypt()