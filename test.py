from tkinter import *
from PIL import ImageTk, Image

HEIGHT = 700
WIDTH = 800


def draw_start_page(window):
    main_frame = Frame(window, bg='#de2323')
    main_frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.8, anchor='n')

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
    button = Button(bottom_frame, text='What is RSA?', bg='gray', command=lambda: info_rsa(main_frame))
    button.place(relx=0.0, rely=0.4, relwidth=0.25, relheight=0.25)
    button2 = Button(bottom_frame, text='Encrypt', bg='gray')
    button2.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.25)
    button3 = Button(bottom_frame, text='decrypt', bg='gray')
    button3.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.25)


def info_rsa(main_frame):
    clear_frame(main_frame)
    new = Toplevel()
    canvas = Canvas(new, height=HEIGHT, width=WIDTH)
    canvas.pack()

    bg_label = Label(new, image=bg)
    bg_label.place(relwidth=1, relheight=1)

    frame = Frame(new, bg='#80c1ff')
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    label = Label(frame, text="RSA", font=('Arial', 40, 'bold'), bg='#80c1ff')
    label.place(relwidth=1, relheight=1)

    frame2 = Frame(new, bg='#80c1ff')
    frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')

    label2 = Label(frame2, font=('Arial', 10, 'bold'), bg='#80c1ff')
    label2.place(relwidth=1, relheight=1)
    label2.config(text="RSA (Rivest–Shamir–Adleman) is a public-key cryptosystem that is widely used for secure data\n"
                       "transmission. It is also one of the oldest. The acronym RSA comes from the surnames of \n"
                       "Ron Rivest,Adi Shamir and Leonard Adleman, \n"
                       "who publicly described the algorithm in 1977. An equivalent system \n"
                       "was developed secretly, in 1973 at GCHQ (the British signals intelligence agency), \n"
                       "by the English mathematician Clifford Cocks. That system was declassified in 1997")


def clear_frame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


root = Tk()

root.title("RSA")

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg = ImageTk.PhotoImage(Image.open("landscape.png"))
bg_label = Label(root, image=bg)
bg_label.place(relwidth=1, relheight=1)

draw_start_page(root)

root.mainloop()
