# Joe Deller May 2017
# Based on the scratch project to draw nets for 3D shapes
# Here is a python version
# Some work is needed to ask for number of sides / height and so on
# Draw a net for a hexagonal prism
# Use the Python "turtle" for drawing lines and shapes
import turtle

length= 60 # the length of the sides of our top and bottom shape
speed = 10 # use a smaller number to go slower
myturtle = turtle.Turtle() # make a turtle using the turtle library
shapesides = 14
heightscaler = 2.5

# Make our drawing window the full screen size
window = turtle.Screen()
window.setup(width=1.0, height=1.0, startx=None, starty=None)

def drawSquare():
    # Draw four sides, turning left 90' each time
    # then move again so we are back where we started
    for i in range (1,5):
        if (i % 2):
           myturtle.forward(length)
        else:
           myturtle.forward(length*heightscaler)        
        myturtle._rotate(-90)
    
def drawShape():
    for i in range (0,shapesides):
        myturtle._rotate(360/shapesides)
        myturtle.forward(length)

def readyTurtle():
# Get our turtle ready to draw using a fast thick pen using degrees (not radians)   
  myturtle.degrees()
  myturtle.pensize (4)
  myturtle.speed(speed)
  myturtle.penup()
  myturtle.goto(50,10)
  myturtle.pendown()

# Turtle Ready!
readyTurtle()

# Start by drawing the specified shapesides number squares, rotating left (360/shapesides) degrees after each square
# This gives us a hexagon shape (360/60) ending up back where we started

for i in range(0,shapesides):
   drawSquare()
   myturtle.forward(length)
   myturtle._rotate(360/shapesides)


# Turtle is now pointing -> so turn back then face downwards ready for final shape
# at the top of our 3D shape
myturtle._rotate(-90)
myturtle.forward(length * heightscaler)
myturtle._rotate(-90)           
# Now for the final shape
drawShape()
