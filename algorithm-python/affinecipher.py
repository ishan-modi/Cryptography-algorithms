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

def gcd(a,b):
    if(b>a):
        ans=gcd(b,a)
        return ans
    else:
        if(b==0):
            return a
        ans=gcd(b,a%b)
        return ans

choice='yes'
print('Enter key 1')
while(choice=='yes'):
    key1=int(input())
    if(gcd(key1,26)!=1):
        print('Enter a valid key')
    else:
        print('Enter key 2')
        key2 = int(input())
        break

f=open("plaintext.txt","r")
plaintext=f.read()
#plaintext.lower()

plaintext=re.findall("[a-zA-Z]",plaintext)
plaintext="".join(plaintext)

'''plaintext1=''
for i in plaintext:
    if(plaintext.isalpha()):
        plaintext1+=i
'''


alphalist=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#encrypt

encrypttext=""
for i in plaintext:
    encrypttext+=alphalist[(alphalist.index(i.lower())*key1+key2)%26]

print(encrypttext)

#decrypt
decrypttext=""
for i in encrypttext:
    decrypttext+=alphalist[((alphalist.index(i)-key2)*inverse(key1))%26]

print(decrypttext)