import turtle
import time
import math
import random

myturtle = turtle.Turtle()
size = 50
x1 = 0
y1 = 100
x2 =5
y2 =0
delay = .001
resolution = 4

def drawSquare(x1, y1, diameter):
    myturtle.penup()
    myturtle.goto(x1, y1)
    myturtle.pendown()
    for i in range(0,4):
        myturtle.forward(diameter)
        myturtle._rotate(90)

def drawTriangle(x1, y1, diameter):
    myturtle.penup()
    myturtle.goto(x1,y1)
    myturtle.pendown()
    #myturtle._rotate(60)
    for i in range (3):
        myturtle.forward(diameter)
        myturtle._rotate(-120)


def drawStar(x1, y1, x2, y2, resolution):
    for lines in range(0, 25):
        myturtle.setposition(x1, y1)
        myturtle.goto(-x2, y2)
        myturtle.setposition(x1, -y1)
        myturtle.goto(x2, y2)
        y1 -= resolution
        x2 += resolution

def drawPent(x1,y2,size):
    myturtle.setheading(0)
    myturtle.penup()
    myturtle.goto(x1,y1)
    #myturtle.setposition(x1,y1)
    myturtle.pendown()
    #myturtle._rotate(-45)
    for i in range (0,8):
        myturtle.forward(size)
        myturtle._rotate(45)


def drawPoly(x, y, num_side, radius):
    sideLen = 2*radius *math.sin(math.pi /num_side)
    angle = 360 /num_side
    myturtle.penup()
    myturtle.goto(x,y)
    myturtle.pendown()
    for i in range(0, num_side):
        myturtle.forward(sideLen)
        myturtle.left(angle)

def randColor():
    red = random.random()
    green = random.random()
    blue = random.random()
    myturtle.pencolor(red,green,blue)

myturtle.speed(10)
#drawPoly(10,0,34,180)
#drawTriangle(10,20,80)
#drawSquare(10,20,80)
#myturtle.speed(8)
#input ("wait")

for i in range (100):
    randColor()
    #drawTriangle(10,40,90)
    drawPoly(10,20,4,30+i)
    myturtle._rotate(3)

#drawStar(x1, y1, x2, y2, resolution)
input ("wait")
dist = 50
x =10
y = 20
for i in range (0,12):
    #drawPent(x1, y1, dist)
    drawPoly(x,y,5,dist)
    x +=10
    y -= 10
    dist +=12
#drawPent(x1, y1, 50)

turtle.done()
