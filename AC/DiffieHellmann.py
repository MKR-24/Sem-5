from random import randint
def is_primitive_root(g, p):
   
    seen = set()
    for i in range(1, p):
        val = (g ** i) % p
        if val in seen:
            return False
        seen.add(val)
    return len(seen) == p - 1

def find_primitive_root(p):
  
    for g in range(2, p):
        if is_primitive_root(g, p):
            return g
    return None
def generate_key(p, g, private_key):
    
    public_key = (g ** private_key) % p
    return public_key

def calculate_shared_secret(public_key, private_key, p):
   
    shared_secret = (public_key ** private_key) % p
    return shared_secret


p = 7 
print("Prime Number",p)
g = find_primitive_root(p)
print("Primitive root",g)

private_key_alice = randint(1, p - 1)
print("private_key_alice:",private_key_alice)
public_key_alice = generate_key(p, g, private_key_alice)
print("public_key_alice",public_key_alice)


private_key_bob = randint(1, p - 1)
print("private_key_bob",private_key_bob)
public_key_bob = generate_key(p, g, private_key_bob)
print("public_key_bob",public_key_bob)


shared_secret_alice = calculate_shared_secret(public_key_bob, private_key_alice, p)
shared_secret_bob = calculate_shared_secret(public_key_alice, private_key_bob, p)


print(f"Alice's shared secret: {shared_secret_alice}")
print(f"Bob's shared secret: {shared_secret_bob}")
