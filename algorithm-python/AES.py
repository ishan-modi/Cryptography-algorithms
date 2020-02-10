from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto import Random

plaintext = open("plaintext.txt", 'rb').read()
length = int(input("Enter Key Length(16,24,32):- "))
key = Random.get_random_bytes(length)
mode = int(input("1: ECB\n2: CBC\n3: CFB\n4: OFB\n5: CTR\nYour Choice:- "))

if mode == 1:
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    print("Ciphertext:- " + str(ciphertext))

    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print("Plaintext:- " + str(plaintext))

elif mode == 2:
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    print("Ciphertext:- " + str(ciphertext))

    iv = cipher.iv
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    print("Plaintext:- " + str(plaintext))

elif mode == 3:
    cipher = AES.new(key, AES.MODE_CFB)
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:- " + str(ciphertext))

    iv = cipher.iv
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    print("Plaintext:- " + str(plaintext))

elif mode == 4:
    cipher = AES.new(key, AES.MODE_OFB)
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:- " + str(ciphertext))

    iv = cipher.iv
    cipher = AES.new(key, AES.MODE_OFB, iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    print("Plaintext:- " + str(plaintext))

elif mode == 5:
    cipher = AES.new(key, AES.MODE_CTR)
    ciphertext = cipher.encrypt(plaintext)

    nonce = cipher.nonce
    print("Ciphertext:- " + str(ciphertext.decode('ISO-8859-1')))
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    print("Plaintext:- " + str(plaintext.decode('ISO-8859-1')))