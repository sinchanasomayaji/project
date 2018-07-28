import tkinter
from tkinter import *
from tkinter import messagebox
import parking


root=Tk()
root.title('Orion Mall Parking')

def donext():
    if(var.get()=='Add Employee'):
        root1=Toplevel(root)
        root1.title('Add employee')

        def add():
            name=s1.get()
            name=parking.park(name,s2.get())
            messagebox.showinfo('Added employee','Successfully added')
            
            
        l1=Label(root1,text='Enter the name of employee')
        l1.pack()
        s1=StringVar()
        e1=Entry(root1,textvariable=s1)
        e1.pack()
        l2=Label(root1,text='Enter salary')
        l2.pack()
        s2=IntVar()
        e2=Entry(root1,textvariable=s2)
        e2.pack()
        b1=Button(root1,text='Add',command=add)
        b1.pack()

    if(var.get()=='Generate Bill'):
        root2=Toplevel(root)
        root2.title('Generate Bill')

        def bill():
            name1=s1.get()
            if name1 in parking.park.e:
                name1=parking.park(name1)
                if(var1.get()=='2 Wheeler'):
                    parking.park.bill(name1,'twowheel',s2.get())
                    messagebox.showinfo('Bill','Vehicle \t Hours \t Amount(per hour)\n'+str(var1.get())+'\t   '+str(s2.get())+'\t $20\n\n\t\tTotal = $'+str(parking.park.tbill))
                if(var1.get()=='4 Wheeler'):
                    parking.park.bill(name1,'fourwheel',s2.get())
                    messagebox.showinfo('Bill','Vehicle \t hours \t Amount(per hour)\n'+str(var1.get())+'\t   '+str(s2.get())+'\t $40\n\n\t\tTotal = $'+str(parking.park.tbill))
                parking.park.total(name1)
            else:
                messagebox.showwarning('Authentication error','Authentication error\n'+s1.get()+' is not an employee')
                

        l1=Label(root2,text='Enter the name of employee')
        l1.pack()
        s1=StringVar()
        e1=Entry(root2,textvariable=s1)
        e1.pack()
        var1=StringVar()
        var1.set('Vehicle')
        o1=OptionMenu(root2,var1,'2 Wheeler','4 Wheeler')
        o1.pack()
        l2=Label(root2,text='Enter no of hours')
        l2.pack()
        s2=IntVar()
        e2=Entry(root2,textvariable=s2)
        e2.pack()
        b2=Button(root2,text='Bill',command=bill)
        b2.pack()

    if(var.get()=='Statistics'):
        root3=Toplevel(root)
        root3.title('Statistics')

        l3=Label(root3,text='Number of 2 wheelers parked = '+str(parking.park.noof2wheelers)+'\nNumber of 4 wheelers parked = '+str(parking.park.noof4wheelers)+'\nTotal vehicles parked = '+str(parking.park.totalvech)+'\nTotal earning = $'+str(parking.park.totalearn))
        l3.pack()
        
var=StringVar()
var.set('Select')

o=OptionMenu(root,var,'Add Employee','Generate Bill','Statistics')
o.pack()

b=Button(root,text='Next',command=donext)
b.pack()

root.mainloop()
