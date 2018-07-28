#program to print first 2 and last 2 chars of given string
st=str(input('enter the string'))
if(len(st)>2):
    print(st[0],st[1],st[-2],st[-1])
else:
    print('empty string ' '')
