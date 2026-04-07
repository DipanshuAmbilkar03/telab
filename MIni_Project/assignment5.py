# Elliptic Curve Cryptography (ECDH)


def egcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = egcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

# Modular inverse using Extended Euclidean Algorithm
def mod_inverse(a, p):
    a %= p
    g, x, _ = egcd(a, p)
    if g != 1:
        return None
    return x % p


# Point Addition
def point_add(P, Q, a, p):
    if P == (None, None):
        return Q
    if Q == (None, None):
        return P

    x1, y1 = P
    x2, y2 = Q

    # P + (-P) = O
    if x1 == x2 and (y1 + y2) % p == 0:
        return (None, None)

    # Point Doubling
    if P == Q:
        if y1 % p == 0:
            return (None, None)
        inv = mod_inverse(2 * y1, p)
        if inv is None:
            return (None, None)
        lam = ((3 * x1 * x1 + a) * inv) % p
    else:
        inv = mod_inverse(x2 - x1, p)
        if inv is None:
            return (None, None)
        lam = ((y2 - y1) * inv) % p

    x3 = (lam * lam - x1 - x2) % p
    y3 = (lam * (x1 - x3) - y1) % p

    return (x3, y3)


# Scalar Multiplication (k * P)
def scalar_mult(k, P, a, p):
    result = (None, None)  # Point at infinity
    temp = P

    while k > 0:
        if k % 2 == 1:
            result = point_add(result, temp, a, p)
        temp = point_add(temp, temp, a, p)
        k = k // 2

    return result


# Main ECDH Process
def ecdh():
    print("=== ECC (ECDH Key Exchange) ===")

    # Curve parameters (given example)
    p = 17
    a = 2
    b = 2
    G = (5, 1)

    print(f"Curve: y^2 = x^3 + {a}x + {b} mod {p}")
    print(f"Generator Point G = {G}")

    # Private keys
    nA = int(input("Enter Alice's private key: "))
    nB = int(input("Enter Bob's private key: "))

    if nA <= 0 or nB <= 0:
        print("Error: private keys must be positive integers.")
        return

    # Public keys
    PA = scalar_mult(nA, G, a, p)
    PB = scalar_mult(nB, G, a, p)

    print("\nAlice's Public Key:", PA)
    print("Bob's Public Key:", PB)

    # Shared secret
    SA = scalar_mult(nA, PB, a, p)
    SB = scalar_mult(nB, PA, a, p)

    print("\nShared Secret computed by Alice:", SA)
    print("Shared Secret computed by Bob:", SB)


# Run
if __name__ == "__main__":
    ecdh()