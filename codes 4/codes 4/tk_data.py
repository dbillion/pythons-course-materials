import tkinter as tk

window = tk.Tk()

##creating few data from tkinter data types
v1 = tk.IntVar()
print('default value: {}'.format(v1.get()))
v1.set(10)
v2 = tk.IntVar()
v2.set(2)

print('Value of v1: {} '.format(v1.get()))
print('Type of v1: {} '.format(type(v1)))
print('Type of the return value of v1: {}'.format(type(v1.get())))
print('Type of v2: {} '.format(type(v2)))
print('Value of v2: {} '.format(v2.get()))


window.mainloop()
