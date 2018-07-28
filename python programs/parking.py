class park:
    noof2wheelers=0
    noof4wheelers=0
    tbill=0
    totalvech=0
    totalearn=0
    e=list()

    def __init__(self,name,salary=2000):
        self.name=name
        self.salary=salary
        self.bill=0
        park.e.append(name)

    def bill(self,vech,hrs):
        self.hrs=hrs
        if(vech=='twowheel'):
            self.bill=self.hrs*20
            park.noof2wheelers+=1
        elif(vech=='fourwheel'):
            self.bill=self.hrs*40
            park.noof4wheelers+=1
        park.totalvech=park.noof2wheelers+park.noof4wheelers
        park.tbill=self.bill

    def total(self):
        park.totalearn=park.totalearn+self.bill
        
