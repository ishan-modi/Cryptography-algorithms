import enchant

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
        c = chr((ord(endata[i]) - int(key2)))
        if (ord(c) <= 31 and ord(c) >= 0):
            c1 = ord(c) - 32
            dedata += chr(c1 % 128)
        else:
            dedata += chr(ord(c) % 128)
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

key2=1
cnt=0
while(True):
    d = enchant.Dict("en_US")
    dedata = Decrypt()
    print(dedata)
    l1=dedata.split(' ')
    for i in range(len(l1)):
         if(l1[i]!="" and d.check(l1[i])==True):
            cnt+=1
    if(cnt > int(len(l1)*0.7)):
        break
    key2+=1

print(dedata)
de = open("decrypt.txt", "w")
de.write(dedata)
de.close()
