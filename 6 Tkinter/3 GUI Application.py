# Import Module
from tkinter import *

# create root window
root = Tk()

############# TITLE  #####################################################################################################
# root window title and dimension
root.title("Rohits First application")

# Set geometry (widthxheight)
root.geometry('800x800')

############# MENU NOT WORKING  #####################################################################################################
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)


############# LABEL  #####################################################################################################
#adding a label to the root window
lbl = Label(root, text = "Rohit shines Mowa")
lbl.grid(column=1, row=1)


############# BUTTON  #####################################################################################################
# function to display text when
# button is clicked
def clicked():
    lbl.configure(text="Nokkesav successfully")

# button widget with red color text
# inside
btn = Button(root, text="Button Nokku mowa",fg="yellow", command=clicked)

# set Button grid
btn.grid(column=1, row=2)


############# ENTRY DATA  #####################################################################################################
# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =3)



# all widgets will be here
# Execute Tkinter
root.mainloop()
