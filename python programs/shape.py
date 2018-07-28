inp=int(input('enter the number of sides in the range(3-10)'))
if(inp<3 or inp>10):
    print('entered sides is out of range ')
if(inp==3):
    print(inp,'sides form triangle')
elif(inp==4):
    print(inp,'sides form quadrilateral')
elif(inp==5):
    print(inp,'sides form pentogon')
elif(inp==6):
    print(inp,'sides form hexagon')
elif(inp==7):
    print(inp,'sides form hexagon')
elif(inp==8):
    print(inp,'sides form octogon')
elif(inp==9):
    print(inp,'sides form nanogon')
elif(inp==10):
    print(inp,'sides form decagon')
