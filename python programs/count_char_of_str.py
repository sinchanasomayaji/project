#program to count the no of characters and store in dictionary
st=str(input('enter the string '))
d=dict()
for i in st:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print('result',d)
