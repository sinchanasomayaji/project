n=int(input('enter a positive number '))
m=int(input('enter a positive number '))
gcd=min(n,m)
while n%gcd!=0 or m%gcd!=0:
    gcd=gcd-1
print('GCD is ',gcd)

            
