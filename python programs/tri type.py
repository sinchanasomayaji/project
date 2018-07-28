a=input('enter length of first side')
b=input('enter the length of 2nd side')
c=input('enter length of 3rd side')
if(a==b):
    if(b==c):
        print('equilateral ')
    else:
        print('isosceles')
elif(b==c):
    print('isosceles')
elif(a==c):
    print('isosceles')
else:
    print('scalene')
