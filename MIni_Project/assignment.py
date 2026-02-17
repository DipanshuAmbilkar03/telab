# ----------------------------
# Dipanshu Ambilkar 
# Simplified Data Encryption Standard
# S-DES IMPLEMENTATION
# ----------------------------

# Permutation tables
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
P8  = [6, 3, 7, 4, 8, 5, 10, 9]
IP  = [2, 6, 3, 1, 4, 8, 5, 7]
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
EP  = [4, 1, 2, 3, 2, 3, 4, 1]
P4  = [2, 4, 3, 1]

# S-boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]


# ----------------------------
# Utility Functions
# ----------------------------

def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(a, b):
    return ''.join('0' if a[i] == b[i] else '1' for i in range(len(a)))

def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '02b')


# ----------------------------
# Key Generation
# ----------------------------

def generate_keys(key):
    key = permute(key, P10)
    left, right = key[:5], key[5:]

    # LS-1
    left = left_shift(left, 1)
    right = left_shift(right, 1)
    K1 = permute(left + right, P8)

    # LS-2
    left = left_shift(left, 2)
    right = left_shift(right, 2)
    K2 = permute(left + right, P8)

    return K1, K2


# ----------------------------
# Function Fk
# ----------------------------

def fk(bits, key):
    left, right = bits[:4], bits[4:]

    temp = permute(right, EP)
    temp = xor(temp, key)

    left_part = temp[:4]
    right_part = temp[4:]

    s0_out = sbox_lookup(left_part, S0)
    s1_out = sbox_lookup(right_part, S1)

    sbox_output = permute(s0_out + s1_out, P4)
    result = xor(left, sbox_output)

    return result + right


def switch(bits):
    return bits[4:] + bits[:4]


# ----------------------------
# Encryption
# ----------------------------

def encrypt(plaintext, key):
    K1, K2 = generate_keys(key)

    bits = permute(plaintext, IP)
    bits = fk(bits, K1)
    bits = switch(bits)
    bits = fk(bits, K2)

    ciphertext = permute(bits, IP_INV)
    return ciphertext


# ----------------------------
# Decryption
# ----------------------------

def decrypt(ciphertext, key):
    K1, K2 = generate_keys(key)

    bits = permute(ciphertext, IP)
    bits = fk(bits, K2)
    bits = switch(bits)
    bits = fk(bits, K1)

    plaintext = permute(bits, IP_INV)
    return plaintext


# ----------------------------
# Example Usage
# ----------------------------

if __name__ == "__main__":
    key = "1010000010"       # 10-bit key
    plaintext = "11010111"   # 8-bit data

    print("Original Plaintext :", plaintext)

    cipher = encrypt(plaintext, key)
    print("Encrypted Ciphertext:", cipher)

    decrypted = decrypt(cipher, key)
    print("Decrypted Plaintext:", decrypted)
