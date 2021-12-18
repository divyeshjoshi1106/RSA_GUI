# main file for this RSA_GUI Python project.

from tkinter import *
from PIL import ImageTk, Image

HEIGHT = 700
WIDTH = 800

# Global variable "frame"
frame = None

# Stack to remember pages visited before for use with the back buttons.
back_stack = []


# Function to generate pages, the page to generate designated by the name passed as argument.
def go_to_page(next_page):
    if next_page == "back" and back_stack:
        go_to_page(back_stack.pop())
    elif next_page == "home":
        clear_frame()
        back_stack.clear()
        go_home()
    elif next_page == "rsa_tutorial_1":
        back_stack.append("home")
        clear_frame()
        rsa_tutorial_1()
    elif next_page == "rsa_tutorial_2":
        back_stack.append("rsa_tutorial_1")
        clear_frame()
        rsa_tutorial_2()
    elif next_page == "rsa_tutorial_3":
        back_stack.append("rsa_tutorial_2")
        clear_frame()
        rsa_tutorial_3()


def go_home():
    main_frame = Frame(frame, bg='#cbde23')
    main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    top_frame = Frame(main_frame, bg='#80c1ff')
    top_frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.15, anchor='n')
    label = Label(top_frame, text="RSA Educational GUI", font=('Arial', 40, 'bold'), bg='#80c1ff')
    label.place(relwidth=1, relheight=1)

    middle_frame = Frame(main_frame, bg='#80c1ff')
    middle_frame.place(relx=0.5, rely=0.25, relwidth=1, relheight=0.5, anchor='n')
    label2 = Label(middle_frame, font=('Arial', 10, 'bold'), bg='#80c1ff')
    label2.place(relwidth=1, relheight=1)
    label2.config(text="RSA encryption tutorial using GUI \nCovers encryption, decryption with an example")

    bottom_frame = Frame(main_frame, bg='#80c1ff')
    bottom_frame.place(relx=0.5, rely=0.8, relwidth=1, relheight=0.15, anchor='n')
    button = Button(bottom_frame, text='What is RSA?', bg='gray', command=lambda: go_to_page("rsa_tutorial_1"))
    button.place(relx=0.0, rely=0.4, relwidth=0.25, relheight=0.25)
    button2 = Button(bottom_frame, text='Encrypt', bg='gray')
    button2.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.25)
    button3 = Button(bottom_frame, text='decrypt', bg='gray')
    button3.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.25)


def rsa_tutorial_1():
    global frame
    main_frame = Frame(frame, bg='#cbde23')
    main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    top_frame = Frame(main_frame, bg='#80c1ff')
    top_frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.15, anchor='n')
    label = Label(top_frame, text="RSA", font=('Arial', 40, 'bold'), bg='#80c1ff')
    label.place(relwidth=1, relheight=1)

    middle_frame = Frame(main_frame, bg='#80c1ff')
    middle_frame.place(relx=0.5, rely=0.25, relwidth=1, relheight=0.5, anchor='n')
    label2 = Label(middle_frame, font=('Arial', 10, 'bold'), bg='#80c1ff')
    label2.place(relwidth=1, relheight=1)
    label2.config(text="RSA is an encryption/decryption algorithm developed to implement public-key cryptography.\n"
                       "\"RSA\" is short for \"Rivest-Shamir-Adleman\", the surnames of the three men who developed\n"
                       "the original algorithm in 1977.\n\n"
                       "Why is encryption needed?\n"
                       "Encryption is needed in order to protect private and sensitive data,\n"
                       "such as personal information, credit card information.\n\n"
                       "Continue to find out more about public-key cryptography!")

    bottom_frame = Frame(main_frame, bg='#80c1ff')
    bottom_frame.place(relx=0.5, rely=0.8, relwidth=1, relheight=0.15, anchor='n')
    button = Button(bottom_frame, text='BEFORE', bg='gray', command=lambda: go_to_page("back"))
    button.place(relx=0.0, rely=0.4, relwidth=0.25, relheight=0.25)
    button2 = Button(bottom_frame, text='HOME', bg='gray', command=lambda: go_to_page("home"))
    button2.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.25)
    button3 = Button(bottom_frame, text='NEXT', bg='gray', command=lambda: go_to_page("rsa_tutorial_2"))
    button3.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.25)


def rsa_tutorial_2():
    global frame
    main_frame = Frame(frame, bg='#cbde23')
    main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    top_frame = Frame(main_frame, bg='#80c1ff')
    top_frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.15, anchor='n')
    label = Label(top_frame, text="RSA", font=('Arial', 40, 'bold'), bg='#80c1ff')
    label.place(relwidth=1, relheight=1)

    middle_frame = Frame(main_frame, bg='#80c1ff')
    middle_frame.place(relx=0.5, rely=0.25, relwidth=1, relheight=0.5, anchor='n')
    label2 = Label(middle_frame, font=('Arial', 10, 'bold'), bg='#80c1ff')
    label2.place(relwidth=1, relheight=1)
    label2.config(text="Public-Key Cryptography a cryptographic system that uses pairs of keys,\n"
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

    bottom_frame = Frame(main_frame, bg='#80c1ff')
    bottom_frame.place(relx=0.5, rely=0.8, relwidth=1, relheight=0.15, anchor='n')
    button = Button(bottom_frame, text='BEFORE', bg='gray', command=lambda: go_to_page("back"))
    button.place(relx=0.0, rely=0.4, relwidth=0.25, relheight=0.25)
    button2 = Button(bottom_frame, text='HOME', bg='gray', command=lambda: go_to_page("home"))
    button2.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.25)
    button3 = Button(bottom_frame, text='NEXT', bg='gray', command=lambda: go_to_page("rsa_tutorial_3"))
    button3.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.25)


def rsa_tutorial_3():
    global frame
    main_frame = Frame(frame, bg='#cbde23')
    main_frame.place(relx=0.5, rely=0, relwidth=1, relheight=1, anchor='n')

    top_frame = Frame(main_frame, bg='#80c1ff')
    top_frame.place(relx=0.5, rely=0.05, relwidth=1, relheight=0.15, anchor='n')
    label = Label(top_frame, text="RSA", font=('Arial', 40, 'bold'), bg='#80c1ff')
    label.place(relwidth=1, relheight=1)

    middle_frame = Frame(main_frame, bg='#80c1ff')
    middle_frame.place(relx=0.5, rely=0.25, relwidth=1, relheight=0.5, anchor='n')
    label2 = Label(middle_frame, font=('Arial', 10, 'bold'), bg='#80c1ff')
    label2.place(relwidth=1, relheight=1)
    label2.config(text="So how does RSA work?\n\n"
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

    bottom_frame = Frame(main_frame, bg='#80c1ff')
    bottom_frame.place(relx=0.5, rely=0.8, relwidth=1, relheight=0.15, anchor='n')
    button = Button(bottom_frame, text='BEFORE', bg='gray', command=lambda: go_to_page("back"))
    button.place(relx=0.0, rely=0.4, relwidth=0.25, relheight=0.25)
    button2 = Button(bottom_frame, text='HOME', bg='gray', command=lambda: go_to_page("home"))
    button2.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.25)
    button3 = Button(bottom_frame, text='Check out RSA encryption!', bg='gray', command=lambda: go_to_page("encrypt"))
    button3.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.25)


def clear_frame():
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
