from tkinter import *


# create root window
obj = Tk()

obj.title("My Buttont Program")  ## Detail on title bar of the window

# frame inside root window
frame = Frame(obj)

# geometry method
frame.pack()

# button inside frame which is
# inside root
button = Button(frame, text ='Geek')
button.pack()

# Tkinter event loop
obj.mainloop()

########### Advanced Button ##########
# activebackground: to set the background color when button is under the cursor.
# activeforeground: to set the foreground color when button is under the cursor.
# bg: to set he normal background color.
# command: to call a function.
# font: to set the font on the button label.
# image: to set the image on the button.
# width: to set the width of the button.
# height: to set the height of the button.

# import tkinter as tk
# r = tk.Tk()
# r.title('Counting Seconds')
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()
# r.mainloop()
