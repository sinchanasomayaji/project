refund=0
totalfnd=0
n=int(input('enter the total number of bottels'))
i=n
while(i!=0):
    qun=float(input('enter the quantity'))
    print('enter the number of bottles having',qun,'liters')
    btl=int(input())
    if(qun<1.0):
        refund=btl*0.10
    elif(qun>1.0):
        refund=btl*0.25
    i=i-btl
    totalfnd=totalfnd+refund
print('total refund is $',totalfnd)

