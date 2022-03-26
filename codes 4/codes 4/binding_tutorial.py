import tkinter

def enter(event):
    lb.configure(text = 'mouse is on gui window')

def leave(event):
    lb.configure(text = 'mouse is outside gui window')

def clk1(event):
    lb.configure(text = 'Left button clicked at x = {}, y = {}'.format(event.x, event.y))

def clk2(event):
    lb.configure(text = 'Middle button clicked at x = {}, y = {}'.format(event.x, event.y))

def clk3(event):
    lb.configure(text = 'Right button clicked at x = {}, y = {}'.format(event.x, event.y))



win = tkinter.Tk()
win.geometry('500x300')
lb = tkinter.Label(win, text = ' ', font = ('Arial Bold', 16), fg = 'red')
lb.grid(column = 1, row = 0)
                 
win.bind('<Button-1>', clk1)
win.bind('<Button-2>', clk2)
win.bind('<Button-3>', clk3)
win.bind('<Enter>', enter)
win.bind('<Leave>', leave)
win.mainloop()
