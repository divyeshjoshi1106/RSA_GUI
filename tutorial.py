from tkinter import *
from PIL import ImageTk, Image
from docutils.nodes import comment

from main import go_to_page

HEIGHT = 700
WIDTH = 800


def rsa_tutorial_1(global_frame):
    main_frame = Frame(global_frame, bg='#cbde23')
    main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    top_frame = Frame(main_frame, bg='#80c1ff')
    top_frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.15, anchor='n')
    label = Label(top_frame, text="RSA", font=('Arial', 40, 'bold'), bg='#80c1ff')
    label.place(relwidth=1, relheight=1)

    middle_frame = Frame(main_frame, bg='#80c1ff')
    middle_frame.place(relx=0.5, rely=0.25, relwidth=1, relheight=0.5, anchor='n')
    label2 = Label(middle_frame, font=('Arial', 10, 'bold'), bg='#80c1ff')
    label2.place(relwidth=1, relheight=1)
    label2.config(text="RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data\n"
                       "transmission. It is also one of the oldest. The acronym RSA comes from the surnames of \n"
                       "Ron Rivest,Adi Shamir and Leonard Adleman, \n"
                       "who publicly described the algorithm in 1977. An equivalent system \n"
                       "was developed secretly, in 1973 at GCHQ (the British signals intelligence agency), \n"
                       "by the English mathematician Clifford Cocks. That system was declassified in 1997")

    bottom_frame = Frame(main_frame, bg='#80c1ff')
    bottom_frame.place(relx=0.5, rely=0.8, relwidth=1, relheight=0.15, anchor='n')
    button = Button(bottom_frame, text='BEFORE', bg='gray')
    button.place(relx=0.0, rely=0.4, relwidth=0.25, relheight=0.25)
    button2 = Button(bottom_frame, text='HOME', bg='gray', command=lambda: go_to_page("home"))
    button2.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.25)




# RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data transmission.
# It is also one of the oldest. The acronym RSA comes from the surnames of Ron Rivest,Adi Shamir and Leonard Adleman,
# who publicly described the algorithm in 1977. An equivalent system was developed secretly, in 1973 at GCHQ
# (the British signals intelligence agency), by the English mathematician Clifford Cocks.
# That system was declassified in 1997


# RSA is an encryption/decryption algorithm developed to implement public-key cryptography.
# "RSA" is short for "Rivest-Shamir-Adleman", the surnames of the three men who developed the original algorithm in 1977.

# Why is encryption needed?
# Encryption is required to protect private and sensitive data, such as personal information, credit card information.

# Public-Key Cryptography
# This is a cryptographic system that uses pairs of keys, a public key for encryption and a private key for decryption.
# A key is a piece of information, usually a string of letters and numbers that can be used to encrypt or decrypt data
# according to a cryptographic algorithm.
# A public key may be known to others and are publicly distributed so other people can use them,
# while a private key is only known by the owner. The idea is that the public key is used to encrypt data,
# while the owner uses the private key to decrypt the data.
# This is like a postbox. Anyone can put mail into the postbox through the opening (public key),
# but only the owner has the key (private key) to open the mailbox and retrieve the contents.
# Public-key cryptography can also be used to verify the authenticity of data with digital signatures.
# The owner can use his private key to encrypt a message and form a digital signature.
# Anyone with the public key can combine the key with the digital signature to check if the message is as expected.
# If the message is as expected, then it can be assumed that this digital signature was created by the owner
# and was not tampered with.

# How does RSA work?
# The basic idea behind the RSA algorithm comes from the fact that it is difficult to factorize large prime numbers.
# Note: RSA is a slow and resource-heavy algorithm compared to other algorithms,
# so it is typically not used to encrypt large amounts of data.
# There are two numbers as public keys, "e" and "n", one private key, "d", and three parameters, "p", "q", and "phi".
# "p" and "q" are two large prime numbers. "n" is the product of "p" and "q". "phi" is the product of (p-1) and (q-1).
# "e" is a coprime to "phi" ("e" and "phi" share the number 1 as the only positive integer divisor).
# "d" is a number such that (e*d)mod(phi) = 1.
# For encryption, c=(m^e)mod(n), with "m" as message and "c" as the ciphertext (encrypted text).
# For decryption, m=(c^d)mod(n).
# For digital signatures, sig=(m^d)mod(n), with "m" as message to be signed, "d" as private key, "sig" as signature.
# For verifying digital signatures, m=(sig^e)mod(n)
