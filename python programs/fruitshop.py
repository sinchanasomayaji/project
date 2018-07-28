class fruit:
    mango=50
    apple=50
    n=0
    def __init__(self,name,salary=2000):
        self.name=name
        self.salary=salary
        fruit.n+=1

    def sell(self,item,wt):
        self.item=item
        self.wt=wt
        if(self.item=='Mango'):
            fruit.mango-=self.wt
        if(self.item=='Apple'):
            fruit.apple-=self.wt

    def buy(self,item,wt):
        self.item=item
        self.wt=wt
        if(self.item=='Mango'):
            fruit.mango+=self.wt
        if(self.item=='Apple'):
            fruit.apple+=self.wt

