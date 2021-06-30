from tkinter import  *

# Designing the basic calci size
root=Tk()
root.title("Screen Size Test") # Decides the screen dimensions
root.geometry("1300x870")
text = ""
data = StringVar()
def btnfunc():  # Manually you need to entry
    global text
    text = display.get()
    data.set(text)

# def btnfunc2():  # Giving value directly so that it prints in the empty space
#     text = " Mowa brooooo"
#     display.insert(0,text)
#     return None
#
# def btnfunc3():  # Giving value directly so that it prints in the empty space
#
#     display.delete(0,END )
#     return None

print(text)

### Type 1
display = Entry(root,width = 130)  # Decides the Size of the entry box
display.pack()                      # Displays the output of entry box


Button(root,text="Press me",font=("Ariel",29,"bold"),bd=12,height=2,width=6,command=btnfunc).pack()

#
# ### Type 2
# display = Entry(root,width = 100)  # Decides the Size of the entry box
# display.pack()                      # Displays the output of entry box
#
#
# Button(root,text="nokku me",font=("Ariel",29,"bold"),bd=12,height=2,width=6,command=btnfunc2).pack()
#
# ### Type 3
# display = Entry(root,width = 100)  # Decides the Size of the entry box
# display.pack()                      # Displays the output of entry box
#
#
# Button(root,text="delete",font=("Ariel",29,"bold"),bd=12,height=2,width=6,command=btnfunc3).pack()


root.mainloop()