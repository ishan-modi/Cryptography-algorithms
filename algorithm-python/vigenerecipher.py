import numpy as np
from itertools import product

def encrypttext(l1, l2):
    encrypt = []

    for i in range(len(l1)):
        encrypt.append(l3.__getitem__(int(findindex(l1[i]) + findindex(l2[i])) % 26))

    print("".join(encrypt))
    return encrypt

def decrypttext(encrypt,l2):
    decrypt=[]

    for i in range(len(encrypt)):
        decrypt.append(l3.__getitem__(int(findindex(encrypt[i])-findindex(l2[i]))%26))

    print("".join(decrypt))
    print()


def keylist(str):
    l2 = []
    i = 0
    j = 0
    while (i < len(l1)):
        if (j == len(str)):
            j = 0
            continue
        l2.append(str[j])
        j += 1
        i += 1
    return l2

def maxoccuring(l):
    temp={}
    for i in range(len(l)):
        if l[i] in temp:
            temp[l[i]]+=1
        else:
            temp[l[i]]=1
    return max(temp)

def max(d):
    temp=-1
    for i,j in d.items():
        if j>temp:
            temp=j
            val=i
    return val

def findindex(x):
    for i in range(len(l3)):
        if(l3[i]==x):
            return int(i)

def gcd(r1,r2):
    while(r2>0):
        q=r1//r2
        r=r1%r2
        r1=r2
        r2=r
    return r1

#l1
f=open("plaintext.txt","r")
data=f.read().lower()
l=data.split()
data="".join(l)
dataf=""
for i in data:
    if i.isalpha():
        dataf+=i

l1=list(dataf)
#l2
str=input("Enter a key")
l2=keylist(str)

#l3
l3="a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

encrypt=encrypttext(l1,l2)

decrypt=decrypttext(encrypt,l2)

#CryptAnalysis
l4=[]
d={}
n=3
for i in range(len(encrypt)):
    l4.append("".join(encrypt[i:i+n]))
print(l4)
print("".join(encrypt))

l5=[]
for i in range(len(l4)):
    if l4[i] in d:
        d[l4[i]]=i-d[l4[i]]
        l5.append(l4[i])
    else:
        d[l4[i]]=i

print(l5)
a=d[l5[0]]
b=d[l5[1]]
ans=gcd(a,b)
print(ans)
for i in range(2,len(l5)):
    ans=gcd(ans,d[l5[i]])
print(ans)

freq=['e','t','a','o','i']
str1=''
for i in range(len(freq)):
    str1+=freq[i]

char=""
for i in range(ans):
    l6=[]
    for j in range(i,len(encrypt),ans):
        l6.append(encrypt[j])
    char+=maxoccuring(l6)
print(char+'\n')

choice=''
while(1):
    for c in product(str1, repeat=len(char)):
        l7=[]
        l2=[]
        for i in range(len(c)):
            l7.append(c[i])
        print(l7)
        str = ""
        for j in range(len(char)):
            str+=l3[(findindex(char[j])-findindex(l7[j]))%26]
        print(str)
        l2 = keylist(str)
        decrypt = decrypttext(encrypt, l2)
        choice=input("is it correct ? (y/n) ")
        if choice=='y':
            break
    if choice=='y':
        break