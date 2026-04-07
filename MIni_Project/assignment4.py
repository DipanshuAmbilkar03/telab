# RSA Algorithm Implementation

# Function to find GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# Function to find modular inverse (Extended Euclidean Algorithm)
def mod_inverse(e, phi):
    old_r, r = e, phi
    old_s, s = 1, 0

    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s

    if old_r != 1:
        return None
    return old_s % phi


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


# RSA Key Generation
def generate_keys(p, q):
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Both p and q must be prime numbers.")
    if p == q:
        raise ValueError("p and q must be distinct prime numbers.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Prefer standard public exponent when possible.
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while e < phi and gcd(e, phi) != 1:
            e += 2

    # Find d such that (e * d) % phi = 1
    d = mod_inverse(e, phi)
    if d is None:
        raise ValueError("Failed to compute modular inverse for e.")

    return (e, n), (d, n)


# Encryption
def encrypt(message, public_key):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in message]
    return cipher


# Decryption
def decrypt(cipher, private_key):
    d, n = private_key
    message = ''.join([chr(pow(char, d, n)) for char in cipher])
    return message


# Main
if __name__ == "__main__":
    print("=== RSA Algorithm ===")

    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    try:
        public_key, private_key = generate_keys(p, q)
    except ValueError as exc:
        print("Error:", exc)
        raise SystemExit(1)

    if public_key[1] <= 255:
        print("Warning: n is very small; some characters may not decrypt correctly.")

    print("\nPublic Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)

    msg = input("\nEnter message: ")

    cipher = encrypt(msg, public_key)
    print("Encrypted message:", cipher)

    decrypted_msg = decrypt(cipher, private_key)
    print("Decrypted message:", decrypted_msg)