from tkinter import *

from tkinter import messagebox

top = Tk() #root window
##top.geometry("100x100")

def hello():
   messagebox.showerror("Say Hello", "Hello World")

B1 = Button(top, text = "Say Hello", command = hello)
B1.place(x = 20,y = 50)

top.mainloop()
