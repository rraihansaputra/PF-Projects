print ('cake and balloons module is ready to deploy')
print ('have fun')
input ("please press enter ")

name = input("what is your name? ")
modulename = input ("please pick btwn cake / balloon ")



def balloon(name):
    print ("I am", name, "and I love Baloons")
    ErosOut(name)
    
def cake(name):
    print ("I am", name, "and I hate cakes")
    ErosOut(name)
    
def ErosOut(name):
    if name == 'eros':
        print ('yeh', name, 'bosen gw liat muka lu')
    else:
        print ('untung bukan eros. jangan kasitau eros ya.')
        
def modulecall(modulename, name):
    if modulename == 'balloon':
        balloon(name)
    if modulename == 'cake':
        cake(name)
    else:
        modulename = input ("please pick btwn cake / balloon ")
        modulecall(modulename, name)

modulecall(modulename, name)

def start():
    name = input("what is your name? ")
    modulename = input ("please pick btwn cake / balloon ")
    modulecall(modulename, name)


