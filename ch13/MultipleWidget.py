from tkinter import *


def result():
    print('the sum of 2+2 is ', 2 + 2)


win = Frame()
win.pack()
Button(win, text="add", command=result).pack(side=LEFT)
Label(win, text='click add to get the sum or quit to exit').pack(side=TOP)
Button(win, text='quit', command=win.quit).pack(side=RIGHT)
win.mainloop()
