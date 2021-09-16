from tkinter import *
master = Tk()
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)

e1 = Entry(master)
e2 = Entry(master)
#
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

mainloop()

# bd: to set the border width in pixels.
# bg: to set the normal background color.
# cursor: to set the cursor used.
# command: to call a function.
# highlightcolor: to set the color shown in the focus highlight.
# width: to set the width of the button.
# height: to set the height of the button.