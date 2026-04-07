# Diffie-Hellman Key Exchange Implementation


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

def power_mod(base, exponent, mod):
    """Efficient modular exponentiation"""
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod
        exponent = exponent // 2
        base = (base * base) % mod
    return result


def diffie_hellman():
    print("=== Diffie-Hellman Key Exchange ===")

    # Public values
    p = int(input("Enter a prime number (p): "))
    g = int(input("Enter primitive root (g): "))

    if not is_prime(p):
        print("Error: p must be a prime number.")
        return
    if not (1 < g < p):
        print("Error: g must satisfy 1 < g < p.")
        return

    # Private keys
    a = int(input("Enter private key of User A: "))
    b = int(input("Enter private key of User B: "))

    if a <= 0 or b <= 0:
        print("Error: private keys must be positive integers.")
        return

    # Public keys
    A = power_mod(g, a, p)   # A = g^a mod p
    B = power_mod(g, b, p)   # B = g^b mod p

    print("\nPublic Key of A:", A)
    print("Public Key of B:", B)

    # Shared secret keys
    key_A = power_mod(B, a, p)   # (g^b)^a mod p
    key_B = power_mod(A, b, p)   # (g^a)^b mod p

    print("\nShared Secret Key (computed by A):", key_A)
    print("Shared Secret Key (computed by B):", key_B)
    if key_A != key_B:
        print("Warning: shared keys do not match. Check p, g, and key inputs.")


# Run program
if __name__ == "__main__":
    diffie_hellman()