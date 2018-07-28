inp=int(input('enter the units consumed'))
if(inp<=100):
    cost=inp*60
    print('cost is ',cost,' cents')
elif(inp>100 and inp<=300):
    r=inp-100
    cost=6000+r*70
    print('cost is ',cost,' cents')
elif(inp>300):
    r=inp-300
    cost=6000+14000+r*80
    print('cost is ',cost,' cents')
