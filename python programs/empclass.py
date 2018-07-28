class employee :
    def __init__(self,first,last,salary):
        self.first=first
        self.last=last
        self.salary=salary
        self.email_id=first+'.'+last+'@company.com'
    def raise_sal(self):
        return self.salary*1.1
    def assign_designation(self,desig):
        self.desig=desig
emp=dict()
i=0
emp[i]=employee('sinchana','somayaji',30000)
print(emp.__dict__)


'''class languages(employee):
    def __init__(self,first,last,salary,lang):
        employee.__init__(self,first,last,salary)
        self.lang=lang
class expr(languages):
    def __init__(self,first,last,salary,lang,experience):
        languages.__init__(self,first,last,salary,lang)
        self.experience=experience

if __name__=='__main__':
    emp3=languages('kushi','d',60000,'pyton')
    emp3.assign_designation('programmer')
    print(emp3.__dict__)
    print('salary after hike',emp3.raise_sal())
    emp4=expr('madhu','gn',70000,'java',5)
    emp4.assign_designation('testing')
    print(emp4.__dict__)
    print('salary after hike',emp4.raise_sal())'''
    
