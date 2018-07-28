import math
a=str(input('enter the numbers'))
a=a.split(',')
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if(int(a[j])>int(a[j+1])):
            a[j],a[j+1]=a[j+1],a[j]
print(a)
    
