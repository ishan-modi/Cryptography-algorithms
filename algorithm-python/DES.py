from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util import Counter
from Crypto import Random

plaintext = open("plaintext.txt", 'rb').read()
key = Random.get_random_bytes(8)
mode = int(input("1: ECB\n2: CBC\n3: CFB\n4: OFB\n5: CTR\nYour Choice:- "))
if mode == 1:
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    print("Ciphertext:- " + str(ciphertext))

    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    print("Plaintext:- " + str(plaintext))

elif mode == 2:
    cipher = DES.new(key, DES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    print("Ciphertext:- " + str(ciphertext))

    iv = cipher.iv
    cipher = DES.new(key, DES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    print("Plaintext:-x` " + str(plaintext))

elif mode == 3:
    cipher = DES.new(key, DES.MODE_CFB)
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:- " + str(ciphertext))

    iv = cipher.iv
    cipher = DES.new(key, DES.MODE_CFB, iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    print("Plaintext:- " + str(plaintext))

elif mode == 4:
    cipher = DES.new(key, DES.MODE_OFB)
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:- " + str(ciphertext))

    iv = cipher.iv
    cipher = DES.new(key, DES.MODE_OFB, iv=iv)
    plaintext = cipher.decrypt(ciphertext)
    print("Plaintext:- " + str(plaintext))

elif mode == 5:
    counter = Counter.new(64)
    cipher = DES.new(key, DES.MODE_CTR, counter=counter)
    ciphertext = cipher.encrypt(plaintext)
    print("Ciphertext:- " + str(ciphertext.decode('ISO-8859-1')))

    cipher = DES.new(key, DES.MODE_CTR, counter=counter)
    plaintext = cipher.decrypt(ciphertext)
    print("Plaintext:- " + str(plaintext.decode('ISO-8859-1')))
