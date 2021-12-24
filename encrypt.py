import random
import rabin_miller
import cryptomath


def generate_keys(keysize=512):
    """
    Generates keys and parameters for use in RSA encryption and decryption.
    These consist of the public keys 'e' and 'n', the private key 'd', and secret parameters 'p', 'q', and 'phi'.
    'p' and 'q' are two large prime numbers.
    'n' is the modulus for encryption and decryption in the RSA algorithm.
    'phi' is calculated as (p - 1) * (q - 1).
    'e' is chosen such that 'e' is co-prime with 'phi' and 1 < e <= phi.
    'd' is chosen such that (e * d) mod phi = 1; that is, 'd' is the modular inverse of 'e' with respect to 'phi'.
    :param keysize: The RSA key size to use in generating keys. Default size is 512 bits.
    :return: e, d, n, p, q, phi
    """
    e = d = n = p = q = phi = 0

    # Step 1: Generate two prime numbers for p & q.
    p = rabin_miller.generate_large_prime(keysize)
    q = rabin_miller.generate_large_prime(keysize)

    n = p * q  # RSA Modulus.
    phi = (p - 1) * (q - 1)  # totient.

    # Step 2: Choose e that is relatively prime to phi.
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** (keysize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the modular inverse of e.
    d = cryptomath.find_modular_inverse(e, phi)

    return e, d, n, p, q, phi


def encrypt(e, n, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, n)) + " "

    return cipher


def decrypt(d, n, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, n))

    return msg
