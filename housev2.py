import turtle
import time
import math
import random

myturtle = turtle.Turtle()
size = 150
x1 = 0
y1 = 00
myturtle.degrees()

# roof is two triangles of size /2   
roof = math.sqrt(2*(size/2)* (size/2))


vectors=[(90,size),(45,roof),(-45,roof),(180,size),(315,roof*2),(180,size)
         ,(45,roof*2),(270,size)]

myturtle.penup()
myturtle.goto(x1, y1)
myturtle.pendown()


for vector in vectors:
    angle,dist=vector
    myturtle.setheading(angle)
    myturtle.forward(dist)
    

    




