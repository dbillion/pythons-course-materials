import tkinter as tk
from tkinter import scrolledtext

w = 50
h = 5

root = tk.Tk()
scrltext = scrolledtext.ScrolledText(root, width = w, height = h, wrap = tk.WORD)
txt = '''
This is the story of a King.
Once there was a king. His kingdom was at the edge of the world, very cold and windy.
Once day he googled how to start a fire.
After that his kingdom was never cold again... just because of fire. 
...
'''
scrltext.insert(tk.INSERT, txt)
scrltext.pack()

root.mainloop()
