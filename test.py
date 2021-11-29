from tkinter import *
from PIL import ImageTk, Image

HEIGHT = 700
WIDTH = 800


def info_rsa():
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

root = Tk()

root.title("RSA")

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg = ImageTk.PhotoImage(Image.open("landscape.png"))
bg_label = Label(root, image=bg)
bg_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#80c1ff')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


label = Label(frame, text="RSA Educational GUI", font=('Arial', 40, 'bold'), bg='#80c1ff')
label.place(relwidth=1, relheight=1)

frame2 = Frame(root, bg='#80c1ff')
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.5, anchor='n')

label2 = Label(frame2, font=('Arial', 10, 'bold'), bg='#80c1ff')
label2.place(relwidth=1, relheight=1)
label2.config(text="RSA encryption tutorial using GUI \nCovers encryption, decryption with an example" )

frame3 = Frame(root, bg='#80c1ff')
frame3.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.1, anchor='n')
button = Button(frame3, text='What is RSA?', bg='gray', command=info_rsa)
button.place(relx=0.0, rely=0.4, relwidth=0.25, relheight=0.25)

button2 = Button(frame3, text='Encrypt', bg='gray')
button2.place(relx=0.4, rely=0.4, relwidth=0.25, relheight=0.25)

button3 = Button(frame3, text='decrypt', bg='gray')
button3.place(relx=0.75, rely=0.4, relwidth=0.25, relheight=0.25)


root.mainloop()
