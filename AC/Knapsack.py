import random
import math

def getknap(key, n, m):
    vals = key.split(',')
    k = ""
    for v in vals:
        i = (int(v) * int(n)) % int(m)
        if k == "":
            k += str(i)
        else:
            k += "," + str(i)
    return k


def solve(n, m):
   for i in range(5000):
       if ((n * i) % m) == 1:
           return i
   return 0



def getcipher(publickey, data):
    data_result = ""
    vals = publickey.split(',')
    weights = [int(v) for v in vals]
    ptr = 0
    total = 0

   
    data = data * (len(weights) // len(data)) + data[:len(weights) % len(data)]

    while ptr < len(data):
        total = 0
        for i in range(len(weights)):
            if ptr < len(data) and data[ptr] == '1':
                bit = 1
            else:
                bit = 0
            total += weights[i] * bit
            ptr += 1

        if data_result == "":
            data_result += str(total)
        else:
            data_result += "," + str(total)

    return data_result

data=input("Enter message:")
priv = input("Enter private key:")
values = [int(v) for v in priv.split(',')]
# m = random.randint(sum(values) + 1, 100)
# print(m)
# n = 2
# while math.gcd(n, m) != 1:
#    n += 1
# print(n)
get_public = getknap(priv, "7", "20")
cipher = getcipher(get_public, data)
solv = solve(7, 20)
plain = getknap(cipher, str(solv), str(20))

print("Private key:", priv)
print("Public key:", get_public)
print("Cipher:", cipher)
print("Solv:", solv)
print("Plain:", plain)
