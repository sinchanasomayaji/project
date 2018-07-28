import tkinter
from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('menu')

var=StringVar()
var.set('c')
n=1

svalue=StringVar()
def selected():
    print(svalue.get())
    messagebox.showinfo('hello','number is '+str(n))

e=Entry(root,text='enter',textvariable=svalue)
e.pack()
l=Label(root,text='enter\n name')
l.pack()

b=Button(root,text="select",command=selected)
b.pack()

root.mainloop()

