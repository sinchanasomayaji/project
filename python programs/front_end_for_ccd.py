import tkinter
from tkinter import *
from tkinter import messagebox
import ccd

root=Tk()
root.title('Cafe Coffee Day')

def donext():
    if(var.get()=='Add employee'):
        root1=Toplevel(root)
        root1.title('Add employee')

        def add():
            name=s1.get()
            if(br1.get()=='Malleshwaram'):
                name=ccd.ccemply(name,'M',s2.get())
            if(br1.get()=='Yeshwanthpuram'):
                name=ccd.ccemply(name,'Y',s2.get())
            if(br1.get()=='Indiranagar'):
                name=ccd.ccemply(name,'I',s2.get())
            messagebox.showinfo('Added employee','Successsfully added')

        l1=Label(root1,text='Enter the name of employee')
        l1.pack()
        s1=StringVar()
        e1=Entry(root1,textvariable=s1)
        e1.pack()

        br1=StringVar()
        br1.set('Branch')
        o1=OptionMenu(root1,br1,'Malleshwaram','Yeshwanthpuram','Indiranagar')
        o1.pack()

        l2=Label(root1,text='Enter the salary')
        l2.pack()
        s2=IntVar()
        e2=Entry(root1,textvariable=s2)
        e2.pack()

        b1=Button(root1,text='Add',command=add)
        b1.pack()
        
    if(var.get()=='Take order'):
        root2=Toplevel(root)
        root2.title('Order')

        def order():
            name2=s3.get()
            if(br2.get()=='Malleshwaram'):
                if name2 in ccd.ccemply.e1:
                    name2=ccd.ccemply(name2,'M')
                    if(ct1.get()==1):
                        ccd.ccemply.sell(name2,'t',s4.get())
                        if(ct2.get()==1):
                            ccd.ccemply.sell(name2,'c',s5.get())
                            messagebox.showinfo('Bill','Item \t Quntity \t Amount \nTea \t  '+str(s4.get())+'\t  $'+str(20)+'\nCoffee \t'+str(s5.get())+'\t $'+str(10)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                        else:
                            messagebox.showinfo('Bill','Item \t Quntity \t Amount \nTea \t  '+str(s4.get())+'\t  $'+str(20)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                    elif(ct2.get()==1):
                        ccd.ccemply.sell(name2,'c',s5.get())
                        messagebox.showinfo('Bill','Item \t Quntity \t Amount \nCoffee \t '+str(s5.get())+'\t  $'+str(10)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                    ccd.ccemply.branchtotal(name2,'M')
                else:
                    messagebox.showwarning('Authentication error','Authentication error\n'+str(s3.get())+' is not an employee of '+str(br2.get())+' branch')
            if(br2.get()=='Yeshwanthpuram'):
                if name2 in ccd.ccemply.e2:
                    name2=ccd.ccemply(name2,'Y')
                    if(ct1.get()==1):
                        ccd.ccemply.sell(name2,'t',s4.get())
                        if(ct2.get()==1):
                            ccd.ccemply.sell(name2,'c',s5.get())
                            messagebox.showinfo('Bill','Item \t Quntity \t Amount \nTea \t  '+str(s4.get())+'\t  $'+str(20)+'\nCoffee \t'+str(s5.get())+'\t $'+str(10)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                        else:
                            messagebox.showinfo('Bill','Item \t Quntity \t Amount \nTea \t  '+str(s4.get())+'\t  $'+str(20)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                    elif(ct2.get()==1):
                        ccd.ccemply.sell(name2,'c',s5.get())
                        messagebox.showinfo('Bill','Item \t Quntity \t Amount \nCoffee \t '+str(s5.get())+'\t  $'+str(10)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                    ccd.ccemply.branchtotal(name2,'Y')
                else:
                    messagebox.showwarning('Authentication error','Authentication error\n'+str(s3.get())+' is not an employee of '+str(br2.get())+' branch') 
            if(br2.get()=='Indiranagar'):
                if name2 in ccd.ccemply.e3:
                    name2=ccd.ccemply(name2,'I')
                    if(ct1.get()==1):
                        ccd.ccemply.sell(name2,'t',s4.get())
                        if(ct2.get()==1):
                            ccd.ccemply.sell(name2,'c',s5.get())
                            messagebox.showinfo('Bill','Item \t Quntity \t Amount \nTea \t  '+str(s4.get())+'\t  $'+str(20)+'\nCoffee \t'+str(s5.get())+'\t $'+str(10)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                        else:
                            messagebox.showinfo('Bill','Item \t Quntity \t Amount \nTea \t  '+str(s4.get())+'\t  $'+str(20)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                    elif(ct2.get()==1):
                        ccd.ccemply.sell(name2,'c',s5.get())
                        messagebox.showinfo('Bill','Item \t Quntity \t Amount \nCoffee \t '+str(s5.get())+'\t  $'+str(10)+'\n\n\t\t Total $'+str(ccd.ccemply.totalbill))
                    ccd.ccemply.branchtotal(name2,'I')
                else:
                    messagebox.showwarning('Authentication error','Authentication error\n'+str(s3.get())+' is not an employee of '+str(br2.get())+' branch')
            
                
        l3=Label(root2,text='Employee name')
        l3.pack()
        s3=StringVar()
        e3=Entry(root2,textvariable=s3)
        e3.pack()

        br2=StringVar()
        br2.set('Branch')
        o2=OptionMenu(root2,br2,'Branch','Malleshwaram','Yeshwanthpuram','Indiranagar')
        o2.pack()
        
        ct1=IntVar()
        ct2=IntVar()
        s5=IntVar()
        l11=Label(root2,text='                    ')
        l11.pack()
        a=Checkbutton(root2,text='Tea',variable=ct1)
        a.pack()
        l4=Label(root2,text='enter no of tea')
        l4.pack()
        s4=IntVar()
        e4=Entry(root2,textvariable=s4)
        e4.pack()
        b=Checkbutton(root2,text='Coffee',variable=ct2)
        b.pack()
        l12=Label(root2,text='enter no of coffee')
        l12.pack()
        e5=Entry(root2,textvariable=s5)
        e5.pack()

        b2=Button(root2,text='Bill',command=order)
        b2.pack()
        
    if(var.get()=='Turnover'):
        root3=Toplevel(root)
        root3.title('Turnover')

        l5=Label(root3,text='Number of coffee sold = '+str(ccd.ccemply.noofcoffeesold)+'\nNumber of tea sold = '+str(ccd.ccemply.noofteasold)+'\nTotal sales in malleshwaram = '+str(ccd.ccemply.totalfrommal)+'\nTotal sales in Yeshwanthpura = '+str(ccd.ccemply.totalfromyesh)+'\nTotal sales in Indiranagar = '+str(ccd.ccemply.totalfromind)+'\nTotal earningss = '+str(ccd.ccemply.totalprofit))
        l5.pack()

var=StringVar()
var.set('Select')

o=OptionMenu(root,var,'Add employee','Take order','Turnover')
o.pack()

b=Button(root,text='Next',command=donext)
b.pack()

root.mainloop()
