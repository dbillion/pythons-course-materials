import tkinter as tk
from tkinter import ttk
win = tk.Tk()

# Selections of int values
num = tk.IntVar() # defining int type variable
numChosen = ttk.Combobox(win, width = 12, textvariable = num)
numChosen['values'] = (1, 2, 3, 4, 5) 
numChosen.grid(column = 1, row = 2)
numChosen.current(2)


def clk():
        numResult = tk.Label(win, text = str(numChosen.get()))
        numResult.grid(column = 1, row = 3)


# Label to display selected combo box value 
numDisp = tk.Button(win, text = 'You have chosen: ', command = clk)
numDisp.grid(column = 0, row = 3)

win.mainloop()

