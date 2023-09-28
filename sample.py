from tkinter import *
top = Tk()
top.geometry("800x500")

def fun():
    label2 = Label(top, text = "Hello World")

label1 = Button(top,command=fun).place(x=100, y=100)

top.mainloop()
