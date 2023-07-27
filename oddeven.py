# import tkinter
from tkinter import *

# define the window
window = Tk()
window.title ("ODD EVEN CHECKER")

# define the label
label1 = Label (text="Insert Number Here:")
label1.grid (column=0,row=1)

# define an EMPTY label. We'll change this later
label2 = Label ()
label2.grid (column=1, row=3)

# define the entry -  this is where the user will input data
entry = Entry ()
entry.grid (column=1, row=1)

# define the check function
def check():
    x = int(entry.get())
# if the number is even ie. evenly divisible by 2, it assigns EVEN NUMBER to variable y
    if x%2==0:
        y="EVEN NUMBER!"

# else, it assigns ODD NUMBER to variable y
    else:
        y = "ODD NUMBER!"
# configure the empty label with a string formatted thus
    label2.config (text=f"{x} is {y}")

# create a buttone with title CHECK and define its position
buttn = Button (text="CHECK",command=check)
buttn.grid (row=2, column=1)

# activate the program
mainloop()