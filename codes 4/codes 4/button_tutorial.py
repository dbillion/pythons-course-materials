import tkinter

win = tkinter.Tk()
win.title('Button tutorial')
win.geometry('300x200+10+10')

lab = tkinter.Label(win, text = 'This is a sample label')
lab.pack()
btn = tkinter.Button(win, text = 'I am a button', fg = 'blue')
btn.place(x = 80, y = 100)

win.mainloop()
