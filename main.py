from tkinter import *

window = Tk()

frame1 = Frame(window)
frame1.pack()
#window.geometry("420x420") # set height and width of the window
window.title("RSA GUI")
window.config(background="#03f0fc")
#icon = ImageTk.PhotoImage(Image.open("1.jpg"))
#window.iconphoto(True, icon)
#photo = ImageTk.PhotoImage(Image.open("2.png"))

label = Label(frame1,
              text="RSA Educational GUI",
              font=('Arial', 40, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=SUNKEN,  # RAISED
              bd=10,
              padx=20,  # space between x axis and text
              pady=20,
              compound='bottom')
label.pack(side=TOP)  # to put label in window

frame2 = Frame(window)
frame2.pack()

label = Label(frame2,
              text="This is a RSA Educational GUI. It contains information on\n how \n RSA works and also RSA in action",
              font=('Arial', 15, 'bold'),
              fg='#00FF00',
              bg='black',
              relief=SUNKEN,  # RAISED
              bd=10,
              padx=20,  # space between x axis and text
              pady=20,
              compound='bottom')
label.pack(side=TOP)  # to put label in window


frame3 = Frame(window)
frame3.pack(side=BOTTOM)
button_RSA = Button(frame3,
                text="what is RSA",
                #command=click,
                font=("Comic Sans", 10),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                compound="bottom")
button_RSA.pack(side=LEFT)

button_encrypt = Button(frame3,
                text="Encryption",
                #command=click,
                font=("Comic Sans", 10),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                compound="bottom")
button_encrypt.pack(side=RIGHT)
#label.place(x=100,y=100)

window.mainloop()
