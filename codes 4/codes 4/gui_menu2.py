import tkinter
from tkinter import ttk
from tkinter import scrolledtext

# Button Callback Function 
def clickMe(): 
	button.configure(text ='Hello ' + name.get())
	# button.configure(state='disabled')
	

win = tkinter.Tk()
win.title('Python GUI')
# win.geometry('250x100')
# win.withdraw()
##win.iconbitmap(r'C:\Python36\DLLs\pyc.ico')

win.resizable(0, 0)

main = tkinter.LabelFrame(win, text=' My Python GUI Widgets ')
main.grid(column=0, row=0, padx = 20, pady = 10)

#our Label 
lab = tkinter.Label(main, text='Enter a name:')
lab.grid(column = 0, row = 0, sticky = 'W')

# Adding a Textbox Entry widget 
name = tkinter.StringVar() #defining a Strnig variable
nameEntered = tkinter.Entry(main, width = 12, textvariable = name) 
nameEntered.grid(column = 0, row = 1, sticky= 'W')
nameEntered.focus() #to bring the cursor there

# Adding a Button 
button = tkinter.Button(main, text = 'Click Me!', command = clickMe) 
button.grid(column = 1, row = 1)

# Adding Label for Combobox
numLab = tkinter.Label(main, text = 'Choose a number:')
numLab.grid(column = 0, row = 2)

# Selections of int values
num = tkinter.IntVar() # defining int type variable
numChosen = ttk.Combobox(main, width = 12, textvariable = num)
numChosen['values'] = (1, 2, 3, 4, 5) 
numChosen.grid(column = 1, row = 2)
numChosen.current(2)

# Label to display selected combo box value 
numDisp = tkinter.Label(main, text = 'You chose: ')
numDisp.grid(column = 0, row = 3)

numResult = tkinter.Label(main, text = str(numChosen.get()))
numResult.grid(column = 1, row = 3)

# Creating three checkbuttons
chVarDis = tkinter.IntVar()
check1 = tkinter.Checkbutton(main, text = 'Disabled', variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = 4, sticky = tkinter.W) 

chVarUn = tkinter.IntVar() 
check2 = tkinter.Checkbutton(main, text = 'UnChecked', variable = chVarUn)
check2.deselect() 
check2.grid(column = 1, row = 4, sticky = tkinter.W) 

chVarEn = tkinter.IntVar() 
check3 = tkinter.Checkbutton(main, text = 'Enabled', variable = chVarEn)
check3.select()  
check3.grid(column = 2, row = 4, sticky = tkinter.W) 


# Radiobutton Globals
COLOR1 = "Blue" 
COLOR2 = "Gold" 
COLOR3 = "Red" 

# Radiobutton Callback 
def radCall(): 
	radSel=radVar.get()
	if radSel == 1: 
		win.configure(background = COLOR1)
	elif radSel == 2: 
		win.configure(background = COLOR2)
	elif radSel == 3: 
		win.configure(background = COLOR3)
		

# Using a scrolled Text
scrolW = 30
scrolH = 4
scr = scrolledtext.ScrolledText(main, width = scrolW, height = scrolH, wrap = tkinter.WORD)

txt = '''This is just a matter of time before you become expert in programming.
good luck and never lose hope.'''
scr.insert(tkinter.INSERT,txt)
scr.grid(column = 0, columnspan = 3)

# create three Radiobuttons
radVar = tkinter.IntVar() 
rad1 = tkinter.Radiobutton(main, text = COLOR1, variable = radVar, value = 1,command = radCall) 
rad1.grid(column = 0, row = 7, sticky = tkinter.W) 
rad2 = tkinter.Radiobutton(main, text = COLOR2, variable = radVar, value = 2, command = radCall)
rad2.grid(column = 1, row = 7, sticky = tkinter.W)
rad3 = tkinter.Radiobutton(main, text = COLOR3, variable = radVar, value = 3, command = radCall)
rad3.grid(column = 2, row = 7, sticky = tkinter.W) 

# Create a Frame for labels
labelsFrame = tkinter.LabelFrame(main, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=8, padx = 20, pady = 20)

# Place labels into the container element
tkinter.Label(labelsFrame, text = 'Label1').grid(column = 0, row = 0)
tkinter.Label(labelsFrame, text = 'Label2').grid(column = 0, row = 1)
tkinter.Label(labelsFrame, text = 'Label3').grid(column = 0, row = 2)

#Call back function for Exit menu
def _quit():
	win.quit()
	win.destroy()
	exit()


#creating Menu Bar
menuBar = tkinter.Menu(win) 
win.config(menu = menuBar)
fileMenu = tkinter.Menu(menuBar, tearoff = 0)
fileMenu.add_command(label = 'New')
menuBar.add_cascade(label = 'File', menu = fileMenu)
fileMenu.add_separator()
fileMenu.add_command(label = 'Exit', command = _quit) 

helpMenu = tkinter.Menu(menuBar, tearoff = 0)
helpMenu.add_command(label = '?')
helpMenu.add_command(label ='About')
menuBar.add_cascade(label = 'Help', menu = helpMenu)





# Starting main window (root window)
win.mainloop()
