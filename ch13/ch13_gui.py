import tkinter
from tkinter import *
import sys


def result():
    print('the sum of 2+2 is', 2 + 2)


win = Frame()
win.pack()
win.mainloop()

# root = Tk()
# widget = Label(root, {'text': '窗口'})
# widget.pack(side=TOP, expand=YES, fill=BOTH)
button = Button(None, text='Click Me', command=sys.exit)
button.pack()
button.mainloop()
# root.mainloop()
