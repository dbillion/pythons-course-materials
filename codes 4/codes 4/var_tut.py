import tkinter
from tkinter import ttk


win = tkinter.Tk()
win.geometry('300x400')

##v1 = tkinter.IntVar()
##print('default value: {} '.format(v1.get()))
##print(type(v1))
##v1.set(20)
##print(type(v1))
##print('current value: {} '.format(v1.get()))
##
##

##var = tkinter.StringVar()
##var.set('one')
data = ('one', 'two', 'three', 'four', 'five')
##cb = ttk.Combobox(win, values = data)
##cb.place(x=60, y=100)

lstbox = tkinter.Listbox(win, height = 5)
for num in data:
    lstbox.insert(tkinter.END, num)


lstbox.place(x=60, y=100)

win.mainloop()
