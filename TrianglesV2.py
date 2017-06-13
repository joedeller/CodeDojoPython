# Python Turtle graphics example for CoderDojo
# Joe Deller May 2017
# V2.0
# This code uses recursion to draw shapes within shapes
# A more generic approach to the triangle and square code
# could be used
 

import time 
import random
import turtle
import sys
import math


def siertriangle(length, depth):
    if (depth>1):
        for i in range (0,3):
            turtle.forward(length)
            turtle.left(120)
            siertriangle(length *0.5, depth-1)
            


            
def siersquare(length, depth):
    if (depth >1):
        for i in range (0,4):
                for j in range (0,2):            
                    siersquare(length /3, depth-1)
                    turtle.forward(length /3)
                turtle.forward(length /3)
                turtle.left(90)

turtle.degrees()
turtle.setheading(0)
turtle.speed(0)

length = 140
# to speed up set tracer to (0,0)
turtle.tracer(10,1)
depth = 5

for i in range (0,6):
    siertriangle(length,depth)
    turtle.color(random.random(),random.random(),random.random())
    turtle.right(90)
    siersquare(length,depth)    
    turtle.forward(length)
    turtle.right(-30)

# Now reposition the turtle ready to fill in the inside
turtle.left(210)
turtle.forward(length)
turtle.right(180)

for i in range (6):
    turtle.color(random.random(),random.random(),random.random())
    siertriangle(length,depth)
    turtle.left(60)


