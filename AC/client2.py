import socket
substitution_box_odd = {
    'a': 'h', 'b': 'i', 'c': 'j', 'd': 'k', 'e': 'l',
    'f': 'm', 'g': 'n', 'h': 'o', 'i': 'p', 'j': 'q',
    'k': 'r', 'l': 's', 'm': 't', 'n': 'u', 'o': 'v',
    'p': 'w', 'q': 'x', 'r': 'y', 's': 'z', 't': 'a',
    'u': 'b', 'v': 'c', 'w': 'd', 'x': 'e', 'y': 'f',
    'z': 'g', ' ': ' '
}

substitution_box_even = {
    'a': 'f', 'b': 'g', 'c': 'h', 'd': 'i', 'e': 'j',
    'f': 'k', 'g': 'l', 'h': 'm', 'i': 'n', 'j': 'o',
    'k': 'p', 'l': 'q', 'm': 'r', 'n': 's', 'o': 't',
    'p': 'u', 'q': 'v', 'r': 'w', 's': 'x', 't': 'y',
    'u': 'z', 'v': 'a', 'w': 'b', 'x': 'c', 'y': 'd',
    'z': 'e', ' ': ' '
}
def caesar_cipher_encrypt(plaintext, substitution_box_odd, substitution_box_even):
    encrypted_text = ""
    for i, char in enumerate(plaintext):
        if i % 2 == 0:  
            substitution_box = substitution_box_odd
        else:
            substitution_box = substitution_box_even

        encrypted_char = substitution_box.get(char, char)
        encrypted_text += encrypted_char   
    print("Caesar Cipher Encrypted text="+encrypted_text)
    num_columns = 4

    ciphertext_matrix = [encrypted_text[i:i + num_columns] for i in range(0, len(encrypted_text), num_columns)]

   
    for i in range(len(ciphertext_matrix)):
        ciphertext_matrix[i] = ciphertext_matrix[i].ljust(num_columns, '$')

    for row in ciphertext_matrix:
        print(row)

    
    second_column = "".join(row[1] for row in ciphertext_matrix)
    fourth_column = "".join(row[3] for row in ciphertext_matrix)
    first_column = "".join(row[0] for row in ciphertext_matrix)
    third_column = "".join(row[2] for row in ciphertext_matrix)

    
    result = (second_column + fourth_column + first_column + third_column)
    return result

def run_client():
  
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"  
    server_port = 8000  
    
    client.connect((server_ip, server_port))

    while True:
       
        plaintext = input("Enter message: ")
        
      
        encrypted_text = caesar_cipher_encrypt(plaintext, substitution_box_odd, substitution_box_even)
        print("Encrypted text="+encrypted_text)
       
        client.send(encrypted_text.encode("utf-8")[:1024])

       
        response = client.recv(1024)
        response = response.decode("utf-8")

        if response.lower() == "closed":
            break

        print(f"Received: {response}")

   
    client.close()
    print("Connection to server closed")

run_client()
