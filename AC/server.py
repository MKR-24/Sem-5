import socket

def caesar_cipher_decrypt(ciphertext, substitution_box):
   decryption_box = {v: k for k, v in substitution_box.items()}
   decrypted_text = ''.join([decryption_box.get(char, char) for char in ciphertext])
   return decrypted_text
substitution_box = {
    'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h',
    'f': 'i', 'g': 'j', 'h': 'k', 'i': 'l', 'j': 'm',
    'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 'o': 'r',
    'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w',
    'u': 'x', 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b',
    'z': 'c', ' ': ' '
}
def columnar_transposition_decode(ciphertext, num_columns):
    num_rows = (len(ciphertext) + num_columns - 1) // num_columns
    num_empty_cells = num_columns * num_rows - len(ciphertext)

    matrix = [['' for _ in range(num_columns)] for _ in range(num_rows)]


    num_cells_in_last_col = num_rows - num_empty_cells

    
    col = 0
    index = 0
    for i, char in enumerate(ciphertext):
        row = i % num_rows
        if row >= num_cells_in_last_col:
            col += 1
        matrix[row][col] = char


    plaintext = ''.join(matrix[row][col] for row in range(num_rows) for col in range(num_columns))

    return plaintext

def run_server():
  
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    port = 8000

    
    server.bind((server_ip, port))
    
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

   
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

 
    while True:
        print("Menu:")
        print("1. Caesar cipher decryption")
        print("2. Columnar transposition decryption")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ciphertext = client_socket.recv(1024).decode("utf-8")
            
            decrypted_msg = caesar_cipher_decrypt(ciphertext, substitution_box)
            print(f"Decrypted message: {decrypted_msg}")
            response = "Decryption completed".encode("utf-8")
            client_socket.send(response)
        elif choice == '2':
            ciphertext = client_socket.recv(1024).decode("utf-8")
            num_columns = int(input("Enter the number of columns: "))
            decrypted_msg = columnar_transposition_decode(ciphertext, num_columns)
            print(f"Decrypted message: {decrypted_msg}")
            response = "Decryption completed".encode("utf-8")
            client_socket.send(response)
        elif choice == '3':
            client_socket.send("close".encode("utf-8"))
            break
        else:
            print("Invalid choice. Please choose a valid option.")

   
    client_socket.close()
    print("Connection to client closed")
 
    server.close()

run_server()
