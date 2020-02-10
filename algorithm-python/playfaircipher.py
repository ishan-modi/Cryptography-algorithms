from numpy import *


def find(val):
    for i in range(6):
        for j in range(6):
            if m[i, j]==str(val):
                return i,j


def encrypt(plaintext):
    plaintext=plaintext.lower()
    plaintextf = ''
    for i in plaintext:
        if (i.isalnum()):
            plaintextf += i
    plaintext = plaintextf

    plaintext = list(plaintext)
    plaintextf = ""
    encrypttext = ""
    for i in range(len(plaintext)):
        if (i + 1 < len(plaintext) and plaintext[i] == plaintext[i + 1]):
            plaintextf += plaintext[i] + "x"
        else:
            plaintextf += plaintext[i]
    if (len(plaintextf) % 2 != 0):
        plaintextf += "x"
    for i in range(0,len(plaintextf),2):
        a,b=find(plaintextf[i])
        c,d=find(plaintextf[i+1])
        if(a==c):
            encrypttext+=m[a,(b+1)%6]+m[c,(d+1)%6]
        elif(b==d):
            encrypttext += m[(a + 1) % 6,b] + m[(c + 1) % 6,d]
        else:
            encrypttext += m[a,d] + m[c,b]
    return encrypttext


def decrypt(encypttext):
    decrypttext=""
    for i in range(0,len(encypttext),2):
        a,b=find(encypttext[i])
        c,d=find(encypttext[i+1])
        if(a==c):
            decrypttext+=m[a,(b-1)%6]+m[c,(d-1)%6]
        elif(b==d):
            decrypttext += m[(a - 1) % 6,b] + m[(c - 1) % 6,d]
        else:
            decrypttext += m[a,d] + m[c,b]
    return decrypttext


def keymatrix(key):
    # 1
    key = key.lower()

    # 2
    keyf = ''
    for i in key:
        if (i.isalnum()):
            keyf += i
    key = keyf

    # 3
    '''
    key=''.join(sorted(set(key),key=key.index))
    print(key)
    '''
    keyf = ''
    for i in key:
        if i not in keyf:
            keyf += i
    key = keyf

    k = 0
    for i in range(6):
        for j in range(6):
            if (k != len(key)):
                m[i, j] = key[k]
                k += 1
            else:
                for l in alphalist:
                    if l not in key:
                        m[i, j] = l
                        alphalist.remove(l)
                        break
    return m





m=chararray((6,6),unicode=True)
alphalist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

key=input("Enter the key")
m=keymatrix(key)

plaintext = input("Enter the plain text")

encrypttext=encrypt(plaintext)
print("Encrypted text : "+encrypttext)

decrypttext= decrypt(encrypttext)
print("Decrypted text : "+decrypttext)
