import string

inp=str(input('enter the words seperated by commas '))
inp=inp.split(',')
inp=sorted(inp)
print(','.join(inp))

