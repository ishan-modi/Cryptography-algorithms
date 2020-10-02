def Encrypt():
	endata=""
	for i in range(len(data)):
		c=chr((ord(data[i])+int(key1)) %256)
		if(ord(c) <=31 and ord(c) >=0):
			endata+=chr(ord(c)+32)
		else:
			endata+=c
	return endata
								
def Decrypt():
	dedata=""
	for i in range(len(endata)):
		if(ord(endata[i])-int(key2) <=31 and ord(endata[i])-int(key2) >=0):
			c1=ord(endata[i])-int(key2) -32
			dedata+=chr(c1%256)
		else:
			dedata+=chr((ord(endata[i])-int(key2))%256)
	return dedata

f=open("plaintext.txt","r")
data=f.read()
f.close()
print("Enter key for encryption")
key1=input()


print("Enter key for normal decryption")
key2=input()

endata=Encrypt()
en=open("encrypted.txt", "w")
en.write(endata)
en.close()

dedata=Decrypt()
de=open("decrypt.txt","w")
de.write(dedata)
de.close()
