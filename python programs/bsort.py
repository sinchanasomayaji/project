a=[0,0,0]
for i in range(0,3):
    a[i]=int(input('enter the number'))
b=max(a)
c=min(a)
mid=a[0]+a[1]+a[2]-b-c
print('sorted number:\n',c,'\n',mid,'\n',b)
