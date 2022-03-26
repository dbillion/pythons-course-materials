from tkinter import *
  
root = Tk() 
root.geometry('600x500') 


txt = '''
This is the informational board for the programming lovers.
You can chose to develop in your favorite programming language.
Mine is C++ and now a days python (because no body used c++ now a days).
what is yours?
'''
msg = Message( root, text = txt, font = ('Arial Black', 20),
               fg = 'red')
    
msg.pack()

  
root.mainloop()
