####Tax Calculator 

import tkinter as tk

window = tk.Tk()
window.title('Tax Calculator ')
window.geometry('300x170')
window.resizable(0,0)
sal = tk.DoubleVar()
rate = tk.DoubleVar()
red = tk.DoubleVar()
tax = tk.DoubleVar()
result = tk.DoubleVar()

def clc():
    salv = sal.get()
    rat = rate.get()
    r = salv - ((salv - red.get()) * (rat/100))
    result.set(r)
    tk.Label(section, text = str(result.get())).grid(column = 1, row = 3)
    return


section = tk.LabelFrame(window, text = ' Calc ' , padx = 20, pady = 10)
section.grid(column = 0, row = 0, padx = 5, pady = 5)
tk.Label(section, text = ' Enter Salary: ').grid(column = 0, row = 0)
tk.Entry(section, width = 15, textvariable = sal).grid(column = 1, row = 0)
tk.Label(section, text = ' Enter Tax Rate (%): ').grid(column = 0, row = 1)
tk.Entry(section, width = 15, textvariable = rate).grid(column = 1, row = 1)
tk.Label(section, text = ' Tax Redemption Amount: ').grid(column = 0, row = 2)
tk.Entry(section, width = 15, textvariable = red).grid(column = 1, row = 2)
tk.Label(section, text = ' Total Tax per month($): ').grid(column = 0, row = 3)
##tk.Label(section, text = str(result.get())).grid(column = 1, row = 3)

tk.Button(window, text = '"Calculate Tax"', command = clc).grid(column = 0, row = 4)      

window.mainloop()
