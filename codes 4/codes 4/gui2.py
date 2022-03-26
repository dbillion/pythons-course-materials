import tkinter

# The 'callback function'. Invoked
# when the button is pressed.


def hello(): 
	print('Hello World') 
	
	
root = tkinter.Tk() 
root.title('MY GUI')
root.geometry('200x100')
root.resizable(0, 0)


# Make a Label.
l = tkinter.Label(root, text = 'My Button')
l.pack()

# Make a button.
b = tkinter.Button(root, text = 'Print Hello', command = hello)
b.pack()


root.mainloop()