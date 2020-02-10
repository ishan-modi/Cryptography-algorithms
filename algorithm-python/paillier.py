from phe import paillier

plaintext = open("plaintext.txt", 'r').read()
publicKey, privateKey = paillier.generate_paillier_keypair()
ciphertext = [publicKey.encrypt(ord(i)) for i in plaintext]
print("Ciphertext:- %s" %(ciphertext))
plaintext = "".join([chr(privateKey.decrypt(i)) for i in ciphertext])
print("Plaintext:- %s" % (plaintext))