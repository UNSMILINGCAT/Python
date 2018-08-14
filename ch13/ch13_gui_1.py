import tkinter
from tkinter import *

root = Tk()
labelfont = ('times', 24, 'italic')  # setting the family size and style
widget = Label(root, text='Eat at joes')  # setting label text
widget.config(bg='black', fg='red', font=labelfont,cursor='cross')
widget.pack(expand=YES, fill=BOTH)
root.mainloop()
