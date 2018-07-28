import string
import random
low_limit=7
upper_limit=10

def randompwd():
    return random.randint(97,122)

len=random.randint(low_limit,upper_limit)
p=list()
for i in range(0,len):
    a=randompwd()
    a=int(a)
    b=chr(a)
    print(b,end='')
