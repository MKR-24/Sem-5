def initial_permutation(block):
    permutation_table = [2, 6, 3, 1, 4, 8, 5, 7]
    return [block[i - 1] for i in permutation_table]

def expansion_permutation(right_half):
    expansion_table = [4, 1, 2, 3, 2, 3, 4, 1]
    return [right_half[i - 1] for i in expansion_table]

def bitwise_xor(left, right):
    assert len(left) == len(right), "Input lists must have the same length"
    return [l ^ r for l, r in zip(left, right)]

def substitution(s_box_input):
    s_box = [
        [1, 0, 1, 0],  
        [0, 1, 0, 1]   
        
    ]
    return [bit for s_box_index in s_box_input for bit in s_box[s_box_index - 1]]

def permutation(right_half):
    permutation_table = [2, 4, 3, 1]
    return [right_half[i - 1] for i in permutation_table]

def des_single_round(block, subkey):
    left_half = block[:4]
    right_half = block[4:]
    print("Left half => ",left_half)
    print("Right half => ",right_half)
    expanded_right = expansion_permutation(right_half)
    print("Expanded right => ",expanded_right)
    expanded_xor_subkey = bitwise_xor(expanded_right, subkey)
    print("expanded_xor_subkey => ",expanded_xor_subkey)
    substituted = substitution(expanded_xor_subkey)
    permuted = permutation(substituted)
    print("permuted p-box => ",permuted)
    new_right = bitwise_xor(left_half, permuted)
    print("new_right  => ",new_right)
    return right_half + new_right


block = [1, 0, 1, 0, 1, 0, 1, 0]
subkey = [0, 0, 1, 1, 0, 0, 1, 1]

print('Block => ',block)
print('subkey => ', subkey)


result = des_single_round(block, subkey)
print("result => ", result)
