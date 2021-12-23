import random


def rabin_miller_test(n, d):
    """
    Test whether the number 'n' is likely to be a prime number with the Rabin-Miller primality test.
    :param n: The number that may be a prime number.
    :param d: A positive odd integer.
    :return: True if 'n' is likely a prime number.
    """
    a = random.randint(2, (n - 2) - 2)
    x = pow(a, int(d), n)  # pow(x,y,z) = (x ^ y) % z
    if x == 1 or x == n - 1:
        return True
    # Square x
    while d != n - 1:
        x = pow(x, 2, n)
        d *= 2
        if x == 1:
            return False
        elif x == n - 1:
            return True
    # If not prime
    return False


def is_prime_test(n):
    """
    Test whether the number 'n' is a prime number.
    Falls back to the Rabin-Miller primality test.
    :param n: The number that may be a prime number.
    :return: True if 'n' is a prime number.
    """
    # Low prime numbers saved in an array to save time
    low_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                  103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                  211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                  331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                  449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                  587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                  709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                  853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                  991, 997]

    # 0, 1, negative numbers are not prime
    if n < 2:
        return False
    # True if found in low_primes
    if n in low_primes:
        return True
    # False if divisible by low-primes
    for prime in low_primes:
        if n % prime == 0:
            return False

    # Test with the Rabin-Miller primality test (Find number c such that c * 2 ^ r = n - 1).
    c = n - 1  # 'c' is even because 'n' is not divisible by 2
    while c % 2 == 0:
        c /= 2  # Make 'c' odd
    for i in range(512):  # Prove not prime 128 times
        if not rabin_miller_test(n, c):
            return False

    return True


def is_co_prime_test(p, q):
    """
    Test whether the numbers 'p' and 'q' are co-primes by checking if the greatest common divisor is 1.
    :return: True if the greatest common divisor of 'p' and 'q' is 1.
    """
    return gcd(p, q) == 1


def gcd(p, q):
    """
    Find the greatest common divisor of the numbers 'p' and 'q' with the euclidean algorithm.
    :return: The greatest common divisor of 'p' and 'q'.
    """
    while q:
        p, q = q, p % q
    return p


def egcd(a, b):
    s = 0
    old_s = 1
    t = 1
    old_t = 0
    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # Return gcd, x, y
    return old_r, old_s, old_t


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

    # Generate prime numbers for p & q
    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)

    n = p * q  # RSA Modulus
    phi = (p - 1) * (q - 1)  # totient

    # Choose e
    while True:
        e = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if is_co_prime_test(e, phi):
            break

    # Choose d
    d = modular_inverse(e, phi)

    return e, d, n, p, q, phi


def generate_large_prime(keysize):
    """
    Generate a random large prime number of keysize bits in size.
    """
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize - 1)
        if is_prime_test(num):
            return num


def modular_inverse(a, b):
    """
    Calculate the modular inverse of the numbers 'a' and 'b'.
    :return: The modular inverse of 'a' and 'b'.
    """
    gcdiv, x, y = egcd(a, b)
    if x < 0:
        x += b
    return x


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
