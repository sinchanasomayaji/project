#program to change all ocurence of first char to $ except first chars
st=str(input('enter the string'))
def change(str):
    char=str[0]
    str1=str.replace(char,'$')
    return str[0]+str1[1:]
print(change(st))

