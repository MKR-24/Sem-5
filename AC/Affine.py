
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None 
    else:
        return x % m

def validate_keys(key):
    a, b = key
    if egcd(a, 26)[0] != 1:
        return False 
    if 0 <= b < 26:
        return True
    return False


def affine_encrypt(text, key):
    if validate_keys(key):
        return ''.join([chr(((key[0] * (ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ', '')])
    else:
        return "Invalid key. 'a' must be coprime to 26, and 'b' must be in the range [0, 25]."


def affine_decrypt(cipher, key):
    if validate_keys(key):
        return ''.join([chr(((modinv(key[0], 26) * (ord(c) - ord('A') - key[1])) % 26) + ord('A')) for c in cipher])
    else:
        return "Invalid key. 'a' must be coprime to 26, and 'b' must be in the range [0, 25]."


def main():
    
    text = input()
    key = [3, 5]

    
    affine_encrypted_text = affine_encrypt(text, key)

    print('Encrypted Text: {}'.format(affine_encrypted_text))

    print('Decrypted Text: {}'.format(affine_decrypt(affine_encrypted_text, key)))

if __name__ == '__main__':
    main()
