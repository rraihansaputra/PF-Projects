#import the turtle module
import turtle

#notification print to shell
print ('turtle module is loaded')
print ('drawing pentagon immidiately...')

#change turtle color to blue
turtle.color('blue')

#so lines would be drawn when moving
turtle.pendown()

#draw one side
turtle.forward(100)

#turn the turtle 72 degrees
turtle.left(72)

#draw one side
turtle.forward(100)

#turn the turtle 72 degrees
turtle.left(72)

#draw one side
turtle.forward(100)

#turn the turtle 72 degrees
turtle.left(72)

#draw one side
turtle.forward(100)

#turn the turtle 72 degrees
turtle.left(72)

#draw one side
turtle.forward(100)

#turn the turtle 72 degrees
turtle.left(72)

#hide the turtle
turtle.hideturtle()

#shell notofication task is finished
print ('blue pentagon is drawn')

#wait for user to type Enter
input('Please type enter to continue...')

#shut the turtle-graphics window
turtle.bye()
