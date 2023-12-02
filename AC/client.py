import socket
import sys

def caesar_cipher_encrypt(plaintext, substitution_box):
    encrypted_text = ''.join([substitution_box.get(char, char) for char in plaintext])
    return encrypted_text

substitution_box = {
    'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h',
    'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm',
    'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r',
    'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w',
    'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b',
    'z': 'c', ' ': ' '
}
def columnar_transposition_encode(plaintext, num_columns):
   
    rows = [plaintext[i:i + num_columns] for i in range(0, len(plaintext), num_columns)]

   
    ciphertext = ""
    for column in range(num_columns):
        for row in rows:
            if column < len(row):
                ciphertext += row[column]

    return ciphertext

def print_matrix(matrix, num_columns):
    for i in range(0, len(matrix), num_columns):
        row = matrix[i:i + num_columns]
        print(" ".join(row))

def run_client():
   
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"  
    server_port = 8000  
  
    client.connect((server_ip, server_port))

    while True:
        print("Menu:")
        print("1. Caesar cipher encryption")
        print("2. Columnar transposition encryption")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            msg = input("Enter message to encrypt using Caesar cipher: ")
            
            encrypted_msg = caesar_cipher_encrypt(msg, substitution_box)
            print(encrypted_msg)
            client.send(encrypted_msg.encode("utf-8")[:1024])
        elif choice == '2':
            msg = input("Enter message to encrypt using Columnar transposition: ")
            num_columns =int(input("Enter the number of columns: "))
            encrypted_msg = columnar_transposition_encode(msg, num_columns)
            print("Matrix format:")
            print_matrix(msg, num_columns)
            print("Encoded text:", encrypted_msg)
            client.send(encrypted_msg.encode("utf-8")[:1024])
        elif choice == '3':
            client.send("closed".encode("utf-8"))
            break
        else:
            print("Invalid choice. Please choose a valid option.")

        response = client.recv(1024)
        response = response.decode("utf-8")

     
        if response.lower() == "closed":
            break

        print(f"Received: {response}")

    client.close()
    print("Connection to server closed")

run_client()
