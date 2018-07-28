def fib(n):
    if n==0:
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

inp=int(input('enter the number of fibonacci series'))
b=fib(inp)
print(b)

    
