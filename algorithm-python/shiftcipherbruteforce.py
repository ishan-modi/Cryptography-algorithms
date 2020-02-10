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
choice="no"
while(choice=="no"):
    dedata = Decrypt()
    print(dedata)
    choice=input("is the data above correct ?(yes or no)\n")
    if(choice=="yes"):
        break
    key2+=1

de = open("decrypt.txt", "w")
de.write(dedata)
de.close()