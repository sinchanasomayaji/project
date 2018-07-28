a=list()
i=0
print('enter the bits')
while(i<8):
    a.append(input())
    i+=1
count=0
for i in range(0,len(a)):
    if(a[i]!='1' and a[i]!='0'):
        print('error!! wrong input')
for i in a:
    if(i=='1'):
        count+=1
if(count%2==0):
    print('parity bit for the given bits ',a,' is 0')
else:
    print('parity bit for the given bits ',a,' is 1')

