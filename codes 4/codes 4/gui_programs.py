import tkinter as tk

####program 1
##root = tk.Tk()
##l = tk.Label(root, text = 'Hello world')
##l.pack()
##root.mainloop()

####program 2
##def hi():
##    print('hello friend!!')
##
##root = tk.Tk()
##l = tk.Label(root, text='My button')
##l.pack()
##
##b = tk.Button(root, text = 'Hello', command = hi)
##b.pack()
##root.mainloop()

####program 3
### Button Callback Function 
##def clickMe(): 
##	button.configure(text ='Hello ' + name.get())
##
##win = tk.Tk()
##win.title('MY GUI')
##win.geometry('150x100')
##win.resizable(0, 0)
##
###our Label 
##lab = tk.Label(win, text="Enter a name:")
##lab.grid(column = 0, row = 0)
##
### Adding a Textbox Entry widget 
##name = tk.StringVar() #string variable input 
##nameEntered = tk.Entry(win, width = 12, textvariable = name) 
##nameEntered.grid(column = 0, row = 1) 
##
### Adding a Button 
##button = tk.Button(win, text="Click Me!", command = clickMe) 
##button.grid(column = 1, row = 1)
##
###dum labels 
####l2 = tk.Label(win, text = '3')
####l2.grid(column = 0, row = 2)
####
####l3 = tk.Label(win, text = '4')
####l3.grid(column = 1, row = 2)
####
##
### Starting main window (root window)
##win.mainloop()

##program 4
from tkinter import ttk
win = tk.Tk()
# Selections of int values
num = tk.IntVar() # defining int type variable
##numChosen = ttk.Combobox(win, width = 12, textvariable = num)
##numChosen['values'] = (0, 1, 2, 3, 4, 5) 
##numChosen.grid(column = 1, row = 2)
##numChosen.current(2)
list1 = [0, 1, 2, 3, 4, 5]
numChosen = ttk.Combobox(win, width = 12, values = list1)
numChosen.grid(column = 1, row = 2)
numChosen.current(2)

def clk():
        numResult = tk.Label(win, text = str(numChosen.get()))
        numResult.grid(column = 1, row = 3)


# Label to display selected combo box value 
numDisp = tk.Label(win, text = 'You have chosen: ') #, command = clk) # make it button
numDisp.grid(column = 0, row = 3)
numResult = tk.Label(win, text = str(numChosen.get()))
numResult.grid(column = 1, row = 3)
win.mainloop()
