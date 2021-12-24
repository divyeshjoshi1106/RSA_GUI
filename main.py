# main file for this RSA_GUI Python project.

from tkinter import *
from PIL import ImageTk, Image
import encrypt

HEIGHT = 700
WIDTH = 800

# Global variable "frame"
frame = None
# Global variables for title label, main body label, and left, center, right buttons
title_label = None
body_label = None
left_button = None
center_button = None
right_button = None

# Stack to remember pages visited before for use with the back buttons.
back_stack = []


def go_to_page(next_page):
    """
    Function to handle on-click events by switching to different pages as necessary.
    In most cases, the window and frame are reused and only text and on-click commands of labels and buttons are edited.
    :param next_page: The name of the next page to display.
    """
    if next_page == "back" and back_stack:
        go_to_page(back_stack.pop())
    elif next_page == "home":
        back_stack.clear()
        go_home()
    elif next_page == "rsa_tutorial_1":
        back_stack.append("home")
        rsa_tutorial_1()
    elif next_page == "rsa_tutorial_2":
        back_stack.append("rsa_tutorial_1")
        rsa_tutorial_2()
    elif next_page == "rsa_tutorial_3":
        back_stack.append("rsa_tutorial_2")
        rsa_tutorial_3()
    elif next_page == "encrypt":
        print("HI")
    elif next_page == "decrypt":
        back_stack.append("home")
        decrypt()


def go_home():
    """
    Generates the first page, the "home" page.
    Other functions reuse the labels and buttons generated by this function
    by switching the text and on-click commands as necessary.
    """
    main_frame = Frame(frame, bg='#cbde23')
    main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    top_frame = Frame(main_frame, bg='#80c1ff')
    top_frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.15, anchor='n')
    global title_label
    title_label = Label(top_frame, text="RSA Educational GUI", font=('Arial', 40, 'bold'), bg='#80c1ff')
    title_label.place(relwidth=1, relheight=1)

    middle_frame = Frame(main_frame, bg='#80c1ff')
    middle_frame.place(relx=0.5, rely=0.25, relwidth=1, relheight=0.5, anchor='n')
    global body_label
    body_label = Label(middle_frame, font=('Arial', 10, 'bold'), bg='#80c1ff')
    body_label.place(relwidth=1, relheight=1)
    body_label.config(text="RSA encryption tutorial using GUI \nCovers encryption, decryption with an example")

    bottom_frame = Frame(main_frame, bg='#80c1ff')
    bottom_frame.place(relx=0.5, rely=0.8, relwidth=1, relheight=0.15, anchor='n')
    global left_button
    left_button = Button(bottom_frame, text='What is RSA?', bg='gray', command=go_to_page("rsa_tutorial_1"))
    left_button.place(relx=0.0, rely=0.4, relwidth=0.25, relheight=0.25)
    global center_button
    center_button = Button(bottom_frame, text='Encrypt', bg='gray', command=go_to_page("encrypt"))
    center_button.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.25)
    global right_button
    right_button = Button(bottom_frame, text='Decrypt', bg='gray', command=go_to_page("decrypt"))
    right_button.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.25)


def rsa_tutorial_1():
    """
    Sets the first page for the tutorial on what is RSA.
    go_home() must be called first because this function only changes the text
    and on-click commands of existing labels and buttons.
    The right button leads to the second page.
    """
    title_label.config(text="What is RSA?")
    body_label.config(text="RSA is an encryption/decryption algorithm developed to implement public-key cryptography.\n"\
                           "\"RSA\" is short for \"Rivest-Shamir-Adleman\", the surnames of the three men who developed\n"\
                           "the original algorithm in 1977.\n\n"\
                           "Why is encryption needed?\n"\
                           "Encryption is needed in order to protect private and sensitive data,\n"\
                           "such as personal information, credit card information.\n\n"\
                           "Continue to find out more about public-key cryptography!")
    left_button.config(text="BEFORE", command=go_to_page("back"))
    center_button.config(text="HOME", command=go_to_page("home"))
    right_button.config(text="NEXT", command=go_to_page("rsa_tutorial_2"))


def rsa_tutorial_2():
    """
    Sets the second page for the tutorial on what is RSA.
    go_home() must be called first because this function only changes the text
    and on-click commands of existing labels and buttons.
    The right button leads to the third page.
    """
    title_label.config(text="Public-key Cryptography")
    body_label.config(text="Public-Key Cryptography a cryptographic system that uses pairs of keys,\n"
                       "a public key for encryption and a private key for decryption. A key is a piece of information,\n"
                       "usually a string of letters and numbers that can be used to encrypt or decrypt data\n"
                       "according to a cryptographic algorithm.\n"
                       "A public key may be known to others and are publicly distributed so other people can use them,\n"
                       "while a private key is only known by the owner. The idea is that the public key is used\n"
                       "to encrypt data, while the owner uses the private key to decrypt the data.\n"
                       "This is like a postbox. Anyone can put mail into the postbox through the opening (public key),\n"
                       "but only the owner has the key (private key) to open the mailbox and retrieve the contents.\n"
                       "Public-key cryptography can also verify the authenticity of data with digital signatures.\n"
                       "The owner can use his private key to encrypt a message and form a digital signature.\n"
                       "Anyone with the public key can combine the key with the signature to check if the message\n"
                       "is as expected. If the message is as expected, then it can be assumed that this digital\n"
                       "signature was created by the owner and was not tampered with.")
    right_button.config(command=go_to_page("rsa_tutorial_3"))


def rsa_tutorial_3():
    """
    Sets the third page for the tutorial on what is RSA.
    go_home() must be called first because this function only changes the text
    and on-click commands of existing labels and buttons.
    The right button leads to the encryption example page.
    """
    title_label.config(text="RSA Formulas")
    body_label.config(text="So how does RSA work?\n\n"
                       "The basic idea behind the RSA algorithm comes from the fact that it is difficult to factorize\n"
                       "large prime numbers.\n"
                       "Note: RSA is a slow and resource-heavy algorithm compared to other algorithms, so it is\n"
                       "typically not used to encrypt large amounts of data.\n"
                       "There are two numbers as public keys, \"e\" and \"n\", one private key, \"d\", and three\n"
                       "parameters, \"p\", \"q\", and \"phi\". \"p\" and \"q\" are two large prime numbers.\n"
                       "\"n\" is the product of \"p\" and \"q\". \"phi\" is the product of (p-1) and (q-1)."
                       "\"e\" is a coprime to \"phi\" (\"e\" and \"phi\" share the number 1 as the only positive\n"
                       "integer divisor). \"d\" is a number such that (e*d)mod(phi) = 1.\n"
                       "For encryption, c=(m^e)mod(n), with \"m\" as message and \"c\" as the ciphertext (encrypted text).\n"
                       "For decryption, m=(c^d)mod(n)."
                       "For digital signatures, sig=(m^d)mod(n), with \"m\" as message to be signed, \"d\" as private\n"
                       "key, \"sig\" as signature. For verifying digital signatures, m=(sig^e)mod(n)")
    right_button.config(text="Check out RSA encryption!", command=go_to_page("encrypt"))


def decrypt():
    keysize = 32

    e, d, n, p, q, phi = encrypt.generate_keys(keysize)

    msg = "This is an example of RSA encryption/decryption :)"

    enc = encrypt.encrypt(e, n, msg)
    dec = encrypt.decrypt(d, n, enc)

    title_label.config(text="Example of RSA decryption")
    body_label.config(text="This is an example of RSA decryption.\n"
                      f"The original message is \"{msg}\"."
                      f"We use the public keys: {e} and {n}, the private key: {d}\nand the parameters: {p}, {q}, and {phi}."
                      f"This is what the same message looks like when encrypted:\n{enc}."
                      f"This is what the ciphertext (encrypted message) looks like when we decrypt it again:\n{dec}.")
    left_button.config(text="BEFORE", command=go_to_page("back"))
    center_button.config(text="HOME", command=go_to_page("home"))
    right_button.config(text="Check out RSA encryption!", command=go_to_page("encrypt"))


def clear_frame():
    """
    Clears all contents of the global frame object.
    """
    global frame
    for widget in frame.winfo_children():
        widget.destroy()


if __name__ == '__main__':
    root = Tk()
    root.title("RSA")
    canvas = Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()
    bg = ImageTk.PhotoImage(Image.open("landscape.png"))
    bg_label = Label(root, image=bg)
    bg_label.place(relwidth=1, relheight=1)
    frame = Frame(root, bg='#de2323')
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.8, anchor='n')
    go_to_page("home")
    root.mainloop()
