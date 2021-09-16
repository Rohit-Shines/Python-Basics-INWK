from tkinter import *
from tkinter.ttk import *

# writing code needs to
# create the main window of
# the application creating
# main window object named root
obj = Tk()

# giving title to the main window
obj.title("First_Program")  ## Detail on title bar of the window

# Label is what output will be
# show on the window
label = Label(obj, text="Hello World !").pack()     # Details inside the window

# calling mainloop method which is used
# when your application is ready to run
# and it tells the code to keep displaying
obj.mainloop()  # helps to display all the time
