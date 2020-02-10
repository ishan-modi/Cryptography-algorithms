import numpy as np
from math import sqrt
from math import ceil
import re

def inverse(r2):
    t1=0
    t2=1
    r1=26
    while(r2>0):
        q=r1//r2
        r=r1%r2
        r1=r2
        r2=r
        t=t1-q*t2
        t1=t2
        t2=t%26
    return t1

def determinant(arr):
    if(len(arr)==1):
        return arr[0,0]
    arr1=cofactor(arr)
    val=0
    for j in range(len(arr[0])):
        val+=arr[0,j]*arr1[0,j]
    return val

def cofactor(arr):
    arr1 = np.empty((len(arr), len(arr)), dtype=int)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            #arr1[i,j]=int(round(np.linalg.det(minor(arr,i,j))))
            arr1[i, j] = determinant(minor(arr, i, j))
            arr1[i, j] = arr1[i, j] * ((-1) ** (i+j));
    return arr1

def adjoint(arr):
    arr1=np.empty((len(arr),len(arr)),dtype=int)
    arr1[:,:]=0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr1[j,i]=arr[i,j]
    return arr1

def minor(arr,i,j):
    if(len(arr)==1):
        print(arr[i,j])
        return arr
    l=[]
    for x in range(len(arr)):
        for y in range(len(arr[i])):
            if(x!=i and y!=j):
                l.append(arr[x,y])
    return np.array(l).reshape(len(arr)-1,len(arr)-1)


def matrixmultiplication(a,b):
    arr=np.empty((n,1),dtype=int,)
    arr[:][:]=0
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[i])):
                arr[i,j]+=a[i,k]*b[k,j]
    return arr

def findindex(x):
    for i in range(len(l1)):
        if(l1[i]==x):
            return int(i)

def findvalue(x):
    x=x%26
    return l1[x]

f=open("plaintext.txt","r")
data=f.read()
data=data.lower()
list1=re.findall('[a-z]',data)

str1=input("Enter a key")

n=ceil(sqrt(len(str1)))

arr=np.empty((n,n),dtype=int)

l1="a b c d e f g h i j k l m n o p q r s t u v w x y z".split()

k=0
l=0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if(k<len(str1)):
            arr[i,j]=findindex(str1[k])
            k+=1
        else:
            arr[i,j]=findindex(l1[l])
            l+=1
print(arr)

#encrypt

l2=[]
encrypt=""
for i in range(0,len(list1),n):
    for j in range(i,i+n):
        l2.append(findindex(list1[j]))
    arr1=np.array(l2).reshape(n,1)
    l2.clear()
    ans= matrixmultiplication(arr, arr1)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            encrypt+=str(findvalue(ans[i,j]))

print(encrypt)

#decrypt

#inv=inverse(int(round(np.linalg.det(arr)%26)))
inv=inverse(determinant(arr)%26)

arr=adjoint(cofactor(arr))
arr[:,:]*=inv
arr[:,:]%=26
print(arr)

decrypt=""
l2=[]
for i in range(0,len(encrypt),n):
    for j in range(i,i+n):
        l2.append(findindex(encrypt[j]))
    arr1 = np.array(l2).reshape(n, 1)
    l2.clear()
    ans = matrixmultiplication(arr, arr1)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            decrypt += str(findvalue(ans[i, j]))

print(decrypt)