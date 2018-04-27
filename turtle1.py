import turtle


def drawSquare(size):
    for i in range(0,4):
        touche.forward(size)
        if (i<3):
            touche._rotate(90)

def readyNext(size):
    touche.pu()
    #touche._rotate(-90)
    touche.forward(10)
    touche._rotate(-90)
    touche.forward(10)
    touche._rotate(180)

    touche.pd()
    size+=20
    return  size

touche = turtle.Turtle()
size = 50
for squares in range (0,10):
    drawSquare(size)
    size =readyNext(size)

turtle.done()
