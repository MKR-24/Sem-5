
initial_key = "0001101100000010111011111111110001110001100000000000000000111101"


pc1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]


shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26,
       8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51,
       45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

def generate_round_key(round_num):
    
    key_permuted = [initial_key[i - 1] for i in pc1]


    
    c_half = key_permuted[:28]
    d_half = key_permuted[28:]
    print("56-bit key generated=:", "".join(key_permuted))


    
    for shift in shift_schedule[:round_num]:
        c_half = c_half[shift:] + c_half[:shift]
        d_half = d_half[shift:] + d_half[:shift]

    
    cd_concatenated = c_half + d_half

    
    round_key = [cd_concatenated[i - 1] for i in pc2]

    return "".join(round_key)


round_1_key = generate_round_key(1)
print("Round 1 Key (48-bit):", round_1_key)
