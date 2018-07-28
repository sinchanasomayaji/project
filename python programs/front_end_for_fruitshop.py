import tkinter
from tkinter import *
from tkinter import messagebox
import fruitshop

root=Tk()
root.title('Fruitshop')

def donext():
    def donext1():
        s1=StringVar()
        s2=IntVar()
        def done1():
            name=s1.get()
            name=fruitshop.fruit(s1.get(),s2.get())
            messagebox.showinfo('Added employe','successfully added')
                
        l1=Label(root1,text='Enter the employee name')
        l1.pack()
        e1=Entry(root1,textvariable=s1)
        e1.pack()
        l2=Label(root1,text='                        ')
        l2.pack()
        l3=Label(root1,text="Enter the employee's salary")
        l3.pack()
        e2=Entry(root1,textvariable=s2)
        e2.pack()
        b2=Button(root1,text='Done',command=done1)
        b2.pack()

    def sell():
        name2=s3.get()
        name2=fruitshop.fruit(name2)
        if(var2.get()=='Apple'):
            if(s4.get()>fruitshop.fruit.apple):
                messagebox.showerror('sellapple',str(s4.get())+' apples are not available')
            if(s4.get()<=fruitshop.fruit.apple):
                fruitshop.fruit.sell(name2,'Apple',s4.get())
                messagebox.showinfo('sell fruits','successfully sold')
        if(var2.get()=='Mango'):
            if(s4.get()>fruitshop.fruit.mango):
                messagebox.showerror('sell mango',str(s4.get())+' mangoes are not available')
            if(s4.get()<=fruitshop.fruit.mango):
                fruitshop.fruit.sell(name2,'Mango',s4.get())
                messagebox.showinfo('sell fruits','successfully sold')

    def buy():
        name3=s5.get()
        name3=fruitshop.fruit(name3)
        if(var3.get()=='Apple'):
            fruitshop.fruit.buy(name3,'Apple',s6.get())
        if(var3.get()=='Mango'):
            fruitshop.fruit.buy(name3,'Mango',s6.get())
        messagebox.showinfo('buy fruits','successful bought')
    
    if(var.get()=='Add Employees'):
        root1=Toplevel(root)
        root1.title('Employees')
        donext1()
        
    if(var.get()=='Sell Fruits'):
        root2=Toplevel(root)
        root2.title('Sell fruits')
        s3=StringVar()
        s4=IntVar()
        
        l4=Label(root2,text='Enter the employee name')
        l4.pack()
        e3=Entry(root2,textvariable=s3)
        e3.pack()
        l7=Label(root2,text='                        ')
        l7.pack()
        l5=Label(root2,text='Select the fruit')
        l5.pack()
        var2=StringVar()
        var2.set('Apple')
        o2=OptionMenu(root2,var2,'Apple','Mango')
        o2.pack()
        l8=Label(root2,text='                        ')
        l8.pack()
        l6=Label(root2,text='Enter the weight of fruit')
        l6.pack()
        e4=Entry(root2,textvariable=s4)
        e4.pack()
        b3=Button(root2,text='sell',command=sell)
        b3.pack()
    if(var.get()=='Buy Fruits'):
        root3=Toplevel(root)
        root3.title('Buy fruits')
        s5=StringVar()
        s6=IntVar()
        
        l9=Label(root3,text='Enter the employee name')
        l9.pack()
        e5=Entry(root3,textvariable=s5)
        e5.pack()
        l10=Label(root3,text='                        ')
        l10.pack()
        l11=Label(root3,text='Select the fruit')
        l11.pack()
        var3=StringVar()
        var3.set('Apple')
        o3=OptionMenu(root3,var3,'Apple','Mango')
        o3.pack()
        l12=Label(root3,text='                        ')
        l12.pack()
        l13=Label(root3,text='Enter the weight of fruit')
        l13.pack()
        e6=Entry(root3,textvariable=s6)
        e6.pack()
        b4=Button(root3,text='buy',command=buy)
        b4.pack()
    if(var.get()=='See stock'):
        messagebox.showinfo('stock','no of apples are '+str(fruitshop.fruit.apple)+'\nno of mangoes are '+str(fruitshop.fruit.mango))
    
        
var=StringVar()
var.set('Select')

o=OptionMenu(root,var,'Select','Add Employees','Sell Fruits','Buy Fruits','See stock')
o.pack()

b=Button(root,text='Next',command=donext)
b.pack()

root.mainloop()
