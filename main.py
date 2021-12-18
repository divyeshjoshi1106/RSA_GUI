from tkinter import *
from PIL import ImageTk, Image

HEIGHT = 700
WIDTH = 800

# Global variable "frame"
frame = None

# main file for this RSA_GUI Python project.

# 2x stacks to remember pages visited before for use with the back and forward buttons.
back_stack = []
forward_stack = []


# Function to generate pages, the page to generate designated by the name passed as argument.
def go_to_page(next_page):
    if next_page == "home":
        clear_frame()
        go_home()
    elif next_page == "rsa_tutorial_1":
        back_stack.append("home")
        clear_frame()
        rsa_tutorial_1()


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
