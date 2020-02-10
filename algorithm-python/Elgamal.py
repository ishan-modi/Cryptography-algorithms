from Crypto.PublicKey import ElGamal
from Crypto import Random

plaintext = open("plaintext.txt", 'r').read()
privateKey = ElGamal.generate(256, Random.new().read)
publicKey = privateKey.publickey()
print("Prime Number:- "+str(privateKey.p))
print("Generator:- "+str(privateKey.g))
print("Public Key(y):- "+str(privateKey.y))
print("Private Key(x):- "+str(privateKey.x))
ciphertext = [publicKey.encrypt(ord(i), 32) for i in plaintext]
print("Ciphertext:- %s" % (ciphertext))
plaintext = "".join([chr(privateKey.decrypt(i)) for i in ciphertext])
print("Plaintext:- "+str(plaintext))