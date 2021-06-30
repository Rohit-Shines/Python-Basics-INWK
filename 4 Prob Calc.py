from tkinter import  *

# Designing the basic calci size
root=Tk()
root.title("Chill Bro calculator")
root.geometry("1200x1000+0+0")

# Definition to take value when clicked
def btnClick(number):
    global val
    val = val+str(number)
    data.set(val)

def btnclear():
    global val
    val =""
    data.set("")

def btnEquals():
    global val
    result = str(eval(val))
    data.set(result)

val = ""
data = StringVar()

# Designing the display size of calci where values are entered
display = Entry(root,width=30,textvariable=data,bd=3,justify="right",bg="black",font=("ariel",20))
display.grid(row=0,columnspan=5)

# Designing buttons in calculator
#R1
btn1=Button(root,text="1",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(1))
btn1.grid(row=1,column=0)

btn2=Button(root,text="2",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(2))
btn2.grid(row=1,column=1)

btn3=Button(root,text="3",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(3))
btn3.grid(row=1,column=2)

btnA=Button(root,text="+",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('+'))
btnA.grid(row=1,column=3)

#R2
btn4=Button(root,text="4",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(4))
btn4.grid(row=2,column=0)

btn5=Button(root,text="5",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(5))
btn5.grid(row=2,column=1)

btn6=Button(root,text="6",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(6))
btn6.grid(row=2,column=2)

btnS=Button(root,text="-",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('-'))
btnS.grid(row=2,column=3)

#R3
btn7=Button(root,text="7",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(7))
btn7.grid(row=3,column=0)

btn8=Button(root,text="8",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(8))
btn8.grid(row=3,column=1)

btn9=Button(root,text="9",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(9))
btn9.grid(row=3,column=2)

btnD=Button(root,text="/",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('/'))
btnD.grid(row=3,column=3)

#R4
btn0=Button(root,text="0",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick(0))
btn0.grid(row=4,column=0)

btno=Button(root,text="Clear",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnclear)
btno.grid(row=4,column=1)

btnE=Button(root,text="=",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
btnE.grid(row=4,column=2)

btnM=Button(root,text="*",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btnM.grid(row=4,column=3)

# #R5
btnPA=Button(root,text="P(A)",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btnPA.grid(row=5,column=0)

btnPB=Button(root,text="P(B)",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnclear)
btnPB.grid(row=5,column=1)

btnPC=Button(root,text="P(C)",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
btnPC.grid(row=5,column=2)

btnSS=Button(root,text="SampleSpace",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btnSS.grid(row=5,column=3)

#R6
btnPAB=Button(root,text="P(A|B)",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btnPAB.grid(row=6,column=0)

btnPAC=Button(root,text="P(A|C)",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnclear)
btnPAC.grid(row=6,column=1)

btnPBA=Button(root,text="P(B|A)",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=btnEquals)
btnPBA.grid(row=6,column=2)

btnBC=Button(root,text="P(B|C)",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btnBC.grid(row=6,column=3)

btnCA=Button(root,text="P(C|A)",font=("Ariel",12,"bold"),bd=12,height=2,width=6,command=lambda:btnClick('*'))
btnCA.grid(row=6,column=4)


# This will help us to display the output for ever
root.mainloop()




