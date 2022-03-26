import tkinter
win = tkinter.Tk()

win.title('command demo')

win.geometry('400x300')

def add():
    e3.config(state='normal')
    e3.delete(0, 'end')
    n1 = int(e1.get())
    n2 = int(e2.get())
    e3.insert(tkinter.END, str(n1+n2))
    e3.config(state='disabled')
    
lb1 = tkinter.Label(win, text = 'Enter first number ')
lb2 = tkinter.Label(win, text = 'Enter second number ')
lb3 = tkinter.Label(win, text = 'Result ')
e1 = tkinter.Entry(win, bd=3)
e2 = tkinter.Entry(win, bd=3)
e3 = tkinter.Entry(win, state='disabled')

b1 = tkinter.Button(win, text = 'Add', command = add)
lb1.place(x=100, y=50)
e1.place(x=200, y=50)
lb2.place(x=100, y=100)

e2.place(x=200, y=100)
b1.place(x=150, y = 150)
lb3.place(x=100, y=200)
e3.place(x=200, y=200)
win.mainloop()