hr=str(input('enter time '))
a=str(input('enter AM or PM '))
hr=hr.split(':')
if(a=='AM' and hr[0]=='12'):
    print('00',':',hr[1],':',hr[2])
elif(a=='AM'):
    print(hr[0],':',hr[1],':',hr[2]) 
if(a=='PM' and hr[0]=='12'):
    print('12',':',hr[1],':',hr[2])
elif(a=='PM'):
    hr[0]=int(hr[0])+12
    print(hr[0],':',hr[1],':',hr[2])
