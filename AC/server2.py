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
def caesar_cipher_decrypt(ciphertext, substitution_box_odd, substitution_box_even):
    encrypted_text=ciphertext
    column_length = len(encrypted_text) // 4
    second_column = encrypted_text[:column_length]
    fourth_column = encrypted_text[column_length * 3:column_length * 4]
    first_column = encrypted_text[column_length:column_length * 2]
    third_column = encrypted_text[column_length * 2:column_length * 3]

  
    matrix_second_column = [second_column[i:i+1] for i in range(len(second_column))]
    matrix_third_column = [third_column[i:i+1] for i in range(len(third_column))]
    matrix_first_column = [first_column[i:i+1] for i in range(len(first_column))]
    matrix_fourth_column = [fourth_column[i:i+1] for i in range(len(fourth_column))]

    combined_matrix = []

    for row in zip(matrix_third_column, matrix_second_column, matrix_fourth_column, matrix_first_column):
        combined_matrix.append(''.join(row))

    for row in combined_matrix:
        print(row)
    result = ''.join([''.join(row) for row in combined_matrix]).replace('$','')
    print(result)
    decryption_box_odd = {v: k for k, v in substitution_box_odd.items()}
    decryption_box_even = {v: k for k, v in substitution_box_even.items()}
    decrypted_text = ""
    
    for i, char in enumerate(result):
        if i % 2 == 0:  
            decryption_box = decryption_box_odd
        else:
            decryption_box = decryption_box_even

        decrypted_char = decryption_box.get(char, char)
        decrypted_text += decrypted_char

    return decrypted_text

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
        encrypted_request = client_socket.recv(1024)
        encrypted_request = encrypted_request.decode("utf-8")

        
        if encrypted_request.lower() == "close":
            
            client_socket.send("closed".encode("utf-8"))
            break

        
        decrypted_request = caesar_cipher_decrypt(encrypted_request, substitution_box_odd, substitution_box_even)
        print(f"Received (Decrypted): {decrypted_request}")

        response = "accepted".encode("utf-8") 
        
        client_socket.send(response)

    
    client_socket.close()
    print("Connection to client closed")
   
    server.close()

run_server()
