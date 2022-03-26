import tkinter


def count():
	counter.set(counter.get() + 1)
	showcounter()
	
def showcounter():
	print(counter.get())
	# #Make another Label
	l2 = tkinter.Label(root, text = (counter.get()))
	l2.grid(column = 1, row = 1)
	


root = tkinter.Tk()   							

counter = tkinter.IntVar()
counter.set(0)


mylabel1 = tkinter.Label(root, text = 'Hello World') 	# Create a Label.
mylabel1.grid(column = 0, row = 0)

mybutton = tkinter.Button(root, text = 'Click Counter', command = count)
mybutton.grid(column = 1, row = 0)

mybutton2 = tkinter.Button(root, text = 'Show Counter', command = showcounter)
mybutton2.grid(column = 0, row = 1)


root.mainloop()


