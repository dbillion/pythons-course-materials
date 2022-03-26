import tkinter as tk
### Button Callback Function 
def clickMe():
    button.configure(text ='Hello ' + name.get() + '!')

win = tk.Tk()
win.title('MY GUI')
# win.geometry('250x200')
win.resizable(0, 0)

###our Label 
lab = tk.Label(win, text="Enter a name:")
lab.grid(column = 0, row = 0)
# 
### Adding a Textbox Entry widget 
name = tk.StringVar() #string variable input 
nameEntered = tk.Entry(win, width = 12, textvariable = name) 
nameEntered.grid(column = 0, row = 1) 

# ### Adding a Button 
button = tk.Button(win, text="Click Me!", command = clickMe) 
button.grid(column = 1, row = 1)
##
# ###dum labels 
l2 = tk.Label(win, text = '3')
l2.grid(column = 2, row = 1)
# ####
# ####l3 = tk.Label(win, text = '4')
# ####l3.grid(column = 1, row = 2)
# ####
# ##
# ### Starting main window (root window)
# win.mainloop()
