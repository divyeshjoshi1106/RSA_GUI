import random, rabin_miller, cryptomath


def main():
    keysize = 512

    e, d, N = generateKey(keysize)

    msg = "Hello, RSA!"

    enc = encrypt(e, N, msg)
    dec = decrypt(d, N, enc)

    print(f"Message: {msg}")
    print(f"e: {e}")
    print(f"d: {d}")
    print(f"N: {N}")
    print(f"enc: {enc}")
    print(f"dec: {dec}")



def generateKey(keySize):
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    print('Generating p prime...')
    p = rabin_miller.generate_large_prime(keySize)
    print('Generating q prime...')
    q = rabin_miller.generate_large_prime(keySize)
    n = p * q

    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e.
    print('Calculating d that is mod inverse of e...')
    d = cryptomath.find_modular_inverse(e, (p - 1) * (q - 1))
    # publicKey = (n, e)
    # privateKey = (n, d)
    # print('Public key:', publicKey)
    # print('Private key:', privateKey)
    return e, d, n


def encrypt(e, N, msg):
    cipher = ""

    for c in msg:
        m = ord(c)
        cipher += str(pow(m, e, N)) + " "

    return cipher


def decrypt(d, N, cipher):
    msg = ""

    parts = cipher.split()
    for part in parts:
        if part:
            c = int(part)
            msg += chr(pow(c, d, N))

    return msg


if __name__ == '__main__':
    main()
