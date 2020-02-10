def find(c):
   if(d.__getitem__(c)==None):
      return False
   else:
      d.__setattr__(c,(d.__getitem__(c)+1))

def Encrypt():
    endata = ""
    for i in range(len(data)):
        c = chr((ord(data[i]) + int(key1)) % 128)
        if (ord(c) <= 31 and ord(c) >= 0):
            endata += chr(ord(c) + 32)
        else:
            endata += c
    return endata


def Decrypt():
    dedata = ""
    for i in range(len(endata)):
        if ((ord(endata[i]) - int(key2) <= 31) and (ord(endata[i]) - int(key2) >= 0)):
            c1 = (ord(endata[i]) - int(key2) - 32)
            dedata += chr(c1 % 128)
        else:
            dedata += chr((ord(endata[i]) - int(key2)) % 128)
    return dedata


f = open("plaintext.txt", "r")
data = f.read()
f.close()

print("Enter key for encryption")
key1 = input()

endata = Encrypt()
en = open("encrypted.txt", "w")
en.write(endata)
en.close()

l=list(endata)
d={i:0 for i in l}
for c in l:
    if c in d:
        d[c]+=1
    else:
        d.__setitem__(c, 1)
temp=0
for c in d:
    if(d[c]>temp):
        temp=d[c]
        val=c

key2=(ord(val)-ord(' '))%128
print(key2)
dedata=Decrypt()

de = open("decrypt.txt", "w")
de.write(dedata)
de.close()