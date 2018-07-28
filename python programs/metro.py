class metro:
    ticket=0

    def __init__(self,age,station):
        self.age=age
        self.station=station
        self.bill=0

    def bill(self,age,station):
        self.station=station
        self.age=age
        if(self.station=='Malleshwaram'):
            if(self.age>=60):
                self.bill=20
            elif(self.age>5):
                self.bill=40
            elif(self.age<=5):
                self.bill=0
        metro.ticket=self.bill
        if(self.station=='Banashankari'):
            if(self.age>=60):
                self.bill=50
            elif(self.age>5):
                self.bill=100
            elif(self.age<=5):
                self.bill=0
        metro.ticket=self.bill
