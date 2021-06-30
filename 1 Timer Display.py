## 1 Timer Code

from tkinter import *   # Package
from tkinter.ttk import *

from time import strftime

root = Tk()  # Creating UI  for display board
root.title("Rohit Calculator")

# Writing function to insert data into the display board
def time():
    string = strftime('%H:%M:%S %p')
    Display.config(text=string)
    Display.after(1000, time)

# inserting Display configurations by calling time function
Display = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
Display.pack(anchor='center')
time()

mainloop()