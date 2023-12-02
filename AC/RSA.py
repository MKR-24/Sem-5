def gcd(a, b):
    while(a!=b):
        if(a > b):
            a = a-b
        else:
            b = b-a
    return a

def key(n):
    ct = 1
    i = 2
    for i in range(2, n):
        if gcd(i, n) == 1:
            return i



def encrypt(message, e, n):
    cipher_text =(pow(message,e)%n)
    return cipher_text

def decrypt(cipher_text, d, n):
    decrypted_text =(pow(cipher_text,d)%n)
    return decrypted_text

p = int(input("Enter value of p: "))
q = int(input("Enter value of q: "))
n = p * q
phi = (p - 1) * (q - 1)
e = key(phi)
d=1
while(True):
    if(((e*d)%phi)==1):
        break
    d+=1
message = int(input("Enter the message to be encrypted: "))
print("Public Key = (", e, ",", n, ")")
print("Private Key = (", d, ",", n, ")")
cipher_text = encrypt(message, e, n)
print("Encrypted message:", cipher_text)

decrypted_text = decrypt(cipher_text, d, n)
print("Decrypted message:", decrypted_text)
