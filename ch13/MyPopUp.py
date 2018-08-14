import sys
from tkinter import *

popupper = (len(sys.argv) > 1)


def dialog():
    win = Toplevel()
    Label(win, text='Do you Always Do what you are Told?').pack()
    Button(win, text='Now click this one', command=win.destroy).pack()
    if popupper:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print("you better obey me...")


root = Tk()
Button(root, text='click me', command=dialog).pack()
root.mainloop()
