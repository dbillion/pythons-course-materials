from tkinter import * 
##from tkinter.ttk import * 
##from time import strftime 
from tkinter.filedialog import askopenfile   
# creating tkinter window 
root = Tk() 
root.title('Menu Demonstration')
root.geometry('400x300')

def menu_clicked(choice):
    if choice == 1:
        label.config(text = 'New File Menu was selected')
    elif choice == 2:
        label.config(text = 'Open.. Menu was selected')
    else:
        pass

        
def open_file(): 
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
    if file is not None: 
        content = file.read() 
        print(content)
        
# Creating Menubar 
menubar = Menu(root) 
  
# Adding File Menu and commands 
file = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='File', menu = file) 
file.add_command(label ='New File', command = lambda: menu_clicked(1)) 
file.add_command(label ='Open...', command = open_file) 
file.add_command(label ='Save', command = None) 
file.add_separator() 
file.add_command(label ='Exit', command = root.destroy) 
  
# Adding Edit Menu and commands 
edit = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Edit', menu = edit) 
edit.add_command(label ='Cut', command = None) 
edit.add_command(label ='Copy', command = None) 
edit.add_command(label ='Paste', command = None) 
edit.add_command(label ='Select All', command = None) 
edit.add_separator() 
edit.add_command(label ='Find...', command = None) 
edit.add_command(label ='Find again', command = None) 
  
# Adding Help Menu 
help_ = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Help', menu = help_) 
help_.add_command(label ='Tk Help', command = None) 
help_.add_command(label ='Demo', command = None) 
help_.add_separator() 
help_.add_command(label ='About Tk', command = None) 
  
# display Menu 
root.config(menu = menubar)
label = Label(root, text = '', font = ('Consolas', 16), fg = 'red')
label.place(x=50, y=50)
mainloop() 
