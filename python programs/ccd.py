class ccemply():

    totalfrommal=0
    totalfromyesh=0
    totalfromind=0
    totalfromall3=0
    totalbev=0
    totalprofit=0
    totalbill=0
    noofcoffeesold=0
    noofteasold=0
    e1=list()
    e2=list()
    e3=list()

    def __init__(self,fullname,branch,salary=2000):
        self.fullname=fullname
        self.salary=salary
        self.branch=branch
        self.profitfromperson=0
        self.noofteasold=0
        self.noofcoffeesold=0
        self.cbill=0
        self.tbill=0
        self.profitfromcoffee=0
        self.profitfromtea=0
        self.totalbevsold=0
        if(branch=='M'):
            ccemply.e1.append(fullname)
        elif(branch=='Y'):
            ccemply.e2.append(fullname)
        else:
            ccemply.e3.append(fullname)

    def sell(self,bev,count):
        if(bev=='c'):
            self.cbill=count*10
            ccemply.noofcoffeesold+=count
            self.profitfromcoffee+=count*10
            self.profitfromperson+=count*10
            self.totalbevsold+=count
        if(bev=='t'):
            self.tbill=count*20
            ccemply.noofteasold+=count
            self.profitfromtea+=count*20
            self.profitfromperson+=count*20
            self.totalbevsold+=count
        ccemply.totalbev+=self.totalbevsold
        ccemply.totalbill=self.tbill+self.cbill
    
    def branchtotal(self,branch):
        self.branch=branch
        if(branch=='M'):
            ccemply.totalfrommal+=self.profitfromperson
        if(branch=='Y'):
            ccemply.totalfromyesh+=self.profitfromperson
        if(branch=='I'):
            ccemply.totalfromind+=self.profitfromperson
        ccemply.totalprofit=ccemply.totalfrommal+ccemply.totalfromyesh+ccemply.totalfromind
        
            
        
