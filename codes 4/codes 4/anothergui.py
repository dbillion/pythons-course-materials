import tkinter

root = tkinter.Tk()
root.geometry("200x200")
root.title("Button Click")
root.resizable(1, 1)
help(root.resizable)

counter = tkinter.IntVar()

def onClick():
    counter.set(counter.get() + 1)

label = tkinter.Label(root, textvariable=counter)
label.pack()
button = tkinter.Button(root, text="Increase", command=onClick)
button.pack()

root.mainloop()