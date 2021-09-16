from tkinter import *
########### list ############
top = Tk()
Lb = Listbox(top)
Lb.insert(1, 'Python')
Lb.insert(2, 'Java')
Lb.insert(3, 'C++')
Lb.insert(4, 'Any other')
Lb.pack()

############## Radio Button ############
v = IntVar()
Radiobutton(top, text='GfG', variable=v, value=1).pack(anchor=W)
Radiobutton(top, text='MIT', variable=v, value=2).pack(anchor=W)

############## Scale Button ############
w = Scale(top, from_=0, to=42)
w.pack()
w = Scale(top, from_=0, to=200, orient=HORIZONTAL)
w.pack()
mainloop()


########### Message #########
ourMessage ='This is our Message'
messageVar = Message(top, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )
top.mainloop()



# highlightcolor: To set the color of the focus highlight when widget has to be focused.
# bg: to set he normal background color.
# bd: to set the border width in pixels.
# font: to set the font on the button label.
# image: to set the image on the widget.
# width: to set the width of the widget.
# height: to set the height of the widget.