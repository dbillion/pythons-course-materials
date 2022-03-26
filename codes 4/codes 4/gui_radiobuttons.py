import tkinter

win = tkinter.Tk()
win.title('MY GUI')
win.geometry('250x200')
win.resizable(0, 0)


# Radiobutton Globals
COLOR1 = "Blue" 
COLOR2 = "Gold" 
COLOR3 = "Red" 

# Radiobutton Callback 
def radCall(): 
	radSel=radVar.get()
	if radSel == 1: 
		win.configure(background = COLOR1)
		rad1.configure(bg = COLOR1)
		rad2.configure(bg = COLOR1)
		rad3.configure(bg = COLOR1)
	elif radSel == 2: 
		win.configure(background = COLOR2)
		rad2.configure(bg = COLOR2)
	elif radSel == 3: 
		win.configure(background = COLOR3)
		rad3.configure(bg = COLOR3)
        
# create three Radiobuttons
radVar = tkinter.IntVar() 
rad1 = tkinter.Radiobutton(win, text = COLOR1, variable = radVar, value = 1,command = radCall) 
rad1.grid(column = 0, row = 5, sticky = tkinter.W) 
rad2 = tkinter.Radiobutton(win, text = COLOR2, variable = radVar, value = 2, command = radCall)
rad2.grid(column = 1, row = 5, sticky = tkinter.W)
rad3 = tkinter.Radiobutton(win, text = COLOR3, variable = radVar, value = 3, command = radCall)
rad3.grid(column = 2, row = 5, sticky = tkinter.W) 
