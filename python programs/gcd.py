print('enter 2 numbers to find gcd')
num1=int(input())
num2=int(input())
while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp
gcd=num1
print('GCD is ',gcd)
