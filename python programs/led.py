import tkinter
from tkinter import *
from tkinter import messagebox

count=0
root=Tk()
root.title('Led light')

def led_on_off():
    global count
    count+=1
    if(count%2==0):
        print('led is off')
    else:
        print('led is on')

b=Button(root,text='click',command=led_on_off)
b.pack()

root.mainloop()
