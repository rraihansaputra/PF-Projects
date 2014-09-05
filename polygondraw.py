import turtle

def turtle_setup():
    import turtle
    turtle.pendown()
    print('Turtle is ready')

def anglecalculation(side):
    angle = 180 - (180* ( side - 2))/ side
    return angle

def draw(side, length):
    for i in range(side):
        turtle.forward(length)
        turtle.left(anglecalculation(side))

def start():
    turtle_setup()
    length = eval(input('Please enter length desired for the polygon that will be drawn.. '))
    side = eval(input('Please enter sides desired for the polygon.. '))
    color = input('Please type the color of the polygon.. ')
    turtle.color(color)
    print('Side will be ', side, 'long. Exterior angle calculated is ', anglecalculation(side), '.')
    input('Ready. Please press Enter to continue..')
    draw(side, length)
    ask = input('Do you want to draw another polygon? (Y/N)')
    if ask== 'Y':
        start()
    else:
        quit

start()
