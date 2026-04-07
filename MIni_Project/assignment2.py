# S-AES Implementation

# S-Box
SBOX = {
    0x0: 0x9, 0x1: 0x4, 0x2: 0xA, 0x3: 0xB,
    0x4: 0xD, 0x5: 0x1, 0x6: 0x8, 0x7: 0x5,
    0x8: 0x6, 0x9: 0x2, 0xA: 0x0, 0xB: 0x3,
    0xC: 0xC, 0xD: 0xE, 0xE: 0xF, 0xF: 0x7
}

# Round constants
RCON1 = 0x80
RCON2 = 0x30


# Helper functions
def sub_nibbles(byte):
    return (SBOX[byte >> 4] << 4) | SBOX[byte & 0x0F]


def rot_nibble(byte):
    return ((byte << 4) | (byte >> 4)) & 0xFF


def xor(a, b):
    return a ^ b


# Key Expansion
def key_expansion(key):
    w = [0] * 6
    w[0] = (key >> 8) & 0xFF
    w[1] = key & 0xFF

    w[2] = xor(w[0], sub_nibbles(rot_nibble(w[1])) ^ RCON1)
    w[3] = xor(w[2], w[1])

    w[4] = xor(w[2], sub_nibbles(rot_nibble(w[3])) ^ RCON2)
    w[5] = xor(w[4], w[3])

    return w


# Add Round Key
def add_round_key(state, k1, k2):
    return state ^ ((k1 << 8) | k2)


# Substitution
def sub_bytes(state):
    return ((SBOX[(state >> 12) & 0xF] << 12) |
            (SBOX[(state >> 8) & 0xF] << 8) |
            (SBOX[(state >> 4) & 0xF] << 4) |
            (SBOX[state & 0xF]))


# Shift Rows
def shift_rows(state):
    s0 = (state >> 12) & 0xF
    s1 = (state >> 8) & 0xF
    s2 = (state >> 4) & 0xF
    s3 = state & 0xF

    return (s0 << 12) | (s1 << 8) | (s3 << 4) | s2


# Galois Multiplication
def gf_mult(a, b):
    p = 0
    for i in range(4):
        if b & 1:
            p ^= a
        hi_bit = a & 0x8
        a <<= 1
        if hi_bit:
            a ^= 0x13
        b >>= 1
    return p & 0xF


# Mix Columns
def mix_columns(state):
    s0 = (state >> 12) & 0xF
    s1 = (state >> 8) & 0xF
    s2 = (state >> 4) & 0xF
    s3 = state & 0xF

    t0 = gf_mult(s0, 1) ^ gf_mult(s2, 4)
    t2 = gf_mult(s0, 4) ^ gf_mult(s2, 1)
    t1 = gf_mult(s1, 1) ^ gf_mult(s3, 4)
    t3 = gf_mult(s1, 4) ^ gf_mult(s3, 1)

    return (t0 << 12) | (t1 << 8) | (t2 << 4) | t3


# Encryption
def encrypt(plaintext, key):
    w = key_expansion(key)

    # Initial AddRoundKey
    state = add_round_key(plaintext, w[0], w[1])

    # Round 1
    state = sub_bytes(state)
    state = shift_rows(state)
    state = mix_columns(state)
    state = add_round_key(state, w[2], w[3])

    # Round 2
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state, w[4], w[5])

    return state


# Main Execution
if __name__ == "__main__":
    try:
        plaintext = int(input("Enter 16-bit plaintext (in hex): "), 16)
        key = int(input("Enter 16-bit key (in hex): "), 16)
    except ValueError:
        print("Invalid hex input. Please enter valid hexadecimal values.")
        raise SystemExit(1)

    if not (0 <= plaintext <= 0xFFFF and 0 <= key <= 0xFFFF):
        print("Plaintext and key must both be 16-bit values (0000 to FFFF).")
        raise SystemExit(1)

    ciphertext = encrypt(plaintext, key)

    print("Ciphertext:", hex(ciphertext))