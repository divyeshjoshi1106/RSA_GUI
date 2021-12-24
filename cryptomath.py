def gcd(a, b):
    """
    Find the greatest common divisor of the numbers 'a' and 'b' with the euclidean algorithm.
    :return: The greatest common divisor of 'a' and 'b'.
    """
    while a != 0:
        a, b = b % a, a
    return b


def find_modular_inverse(a, m):
    """
    Calculate the modular inverse of the numbers 'a' and 'm'.
    :return: The modular inverse of 'a' and 'm'.
    """
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m
