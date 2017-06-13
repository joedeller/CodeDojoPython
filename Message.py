# Joe Deller May 2017
# You need to install pygame before running this as it is not
# installed by default with Python
# A Python version of the Pymine draw a message using blocks 

import pygame
import time 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen_x = 800
screen_y = 600
fontWidth = 6 # The width of each character of our font, which is monospace
y = 5

def setBlock(x, y, colour):
    lx = x *  20
    ly = y * 20
    pygame.draw.rect(screen, colour, [lx, ly, 18, 18])


def DrawMessage(x,message):
# Firstly look up the letter / number in our alphabet dictionary
    for letter in message:
    # Take the list of data we get back and separate it out into rows
    # pass the pattern and where we want to draw the letter to DrawLetter
        pattern  = letters.get(letter).split(",")
        #print "Pattern for letter " + letter + " = " + letters.get(letter)
      
        DrawLetter(pattern,x,y)
# The character set we are using is actually a 5 blocks wide by 7 blocks high one
# so we will reduce the amount of space between the letters by only
# leaving a single block of space between them
        x = x + fontWidth

def DrawLetter(pattern,x,y):
    # We have a series of Hexadecimal (base 16)  numbers that represent 1 row of blocks of the letter we want to draw
    # We draw from the top of the letter to the bottom, from left to right
    # Our dictionary of letter patterns is in Hexadecimal (base 16)  format, so our scale is 16
    # we could have used base 10, but that is slightly more typing
    scale = 16
    # Each row of our letter can be up to 8 blocks wide including the spaces around it
    num_of_blocks = 8

    # Draw the letter one row at a time
    for row in pattern:
        # We draw each row of the letter from left to right, we need to move 8 to the left at the start of each row
        x = x - 8
        # Convert the hexadecimal value into a binary one, a series of block patterns like "1001001"
        # Each 1 means draw a solid block, each 0 means draw an empty block (air)
        blocks = bin(int(row,scale))[2:].zfill(num_of_blocks)
        # We now have all the information we need to draw one row of the letter
        # so step through every block and draw it, left to right
        # be careful in that the word "block" is already in use, so I use "brick" instead
        for brick in blocks:
          if (brick == "1"):
              setBlock(x,y,WHITE)
          else:
              setBlock(x,y,BLACK)
          # move right one block
          x = x + 1
        # Now move down to the next row of blocks for our letter
        y = y + 1    
    

# Here is a list of the codes needed to make our alphabet font
# The characters are actually 5 wide by 8 high and the data is in Hex format to save typing
# Create a new dictionary, the space character is all zeros
letters=dict({' ':'00,00,00,00,00,00,00,00'})

# Add the rest of the letters to our dictionary
letters ['A'] = '70,88,88,88,F8,88,88,88'
letters ['B'] = 'F0,88,88,F0,88,88,88,F0'
letters ['C'] = '70,88,80,80,80,80,88,70'
letters ['D'] = 'E0,90,88,88,88,88,90,E0'
letters ['E'] = 'F8,80,80,F0,80,80,80,F8'
letters ['F'] = 'F8,80,80,F0,80,80,80,80'
letters ['G'] = '70,88,80,80,B8,88,88,70'
letters ['H'] = '88,88,88,F8,88,88,88,88'
letters ['I'] = 'F8,20,20,20,20,20,20,F8'
letters ['J'] = '08,08,08,08,08,88,88,70'
letters ['K'] = '88,90,A0,C0,C0,A0,90,88'
letters ['L'] = '80,80,80,80,80,80,80,F8'
letters ['M'] = '88,D8,A8,A8,88,88,88,88'
letters ['N'] = '88,C8,A8,A8,98,88,88,88'
letters ['O'] = '70,88,88,88,88,88,88,70'
letters ['P'] = 'F0,88,88,88,F0,80,80,80'
letters ['Q'] = '70,88,88,88,88,A8,90,68'
letters ['R'] = 'F0,88,88,88,F0,A0,90,88'
letters ['S'] = '78,80,80,70,08,08,08,F0'
letters ['T'] = 'F8,20,20,20,20,20,20,20'
letters ['U'] = '88,88,88,88,88,88,88,70'
letters ['V'] = '88,88,88,88,50,50,20,20'
letters ['W'] = '88,88,88,88,A8,A8,D8,88'
letters ['X'] = '88,88,50,20,20,50,88,88'
letters ['Y'] = '88,88,88,50,20,20,20,20'
letters ['Z'] = 'F8,08,10,20,20,40,80,F8'
letters ['a'] = '00,00,70,08,78,88,88,78'
letters ['b'] = '80,80,80,B0,C8,88,88,F0'
letters ['c'] = '00,00,70,88,80,80,88,70'
letters ['d'] = '08,08,08,68,98,88,88,78'
letters ['e'] = '00,00,00,70,88,F8,80,70'
letters ['f'] = '30,48,40,40,E0,40,40,40'
letters ['g'] = '00,78,88,88,78,08,08,70'
letters ['h'] = '80,80,80,B0,C8,88,88,88'
letters ['i'] = '00,20,00,20,20,20,20,20'
letters ['j'] = '10,00,30,10,10,10,90,60'
letters ['k'] = '80,80,80,90,A0,C0,A0,90'
letters ['l'] = '60,20,20,20,20,20,20,70'
letters ['m'] = '00,00,D0,A8,A8,88,88,88'
letters ['n'] = '00,00,B0,C8,88,88,88,88'
letters ['o'] = '00,00,00,70,88,88,88,70'
letters ['p'] = '00,00,F0,88,88,F0,80,80'
letters ['q'] = '00,00,68,98,78,08,08,08'
letters ['r'] = '00,00,00,B0,C8,80,80,80'
letters ['s'] = '00,00,00,70,80,70,08,F0'
letters ['t'] = '40,40,E0,40,40,40,48,30'
letters ['u'] = '00,00,00,88,88,88,98,68'
letters ['v'] = '00,00,00,88,88,88,50,20'
letters ['w'] = '00,00,00,88,A8,A8,A8,50'
letters ['x'] = '00,00,00,88,50,20,50,88'
letters ['y'] = '00,00,48,48,48,38,08,70'
letters ['z'] = '00,00,00,F8,10,20,40,F8'
letters ['1'] = '20,60,20,20,20,20,20,70'
letters ['2'] = '70,88,08,10,20,40,80,F8'
letters ['3'] = '70,88,08,30,08,08,88,70'
letters ['4'] = '10,30,50,90,F8,10,10,10'
letters ['5'] = 'F8,80,80,F0,08,08,88,70'
letters ['6'] = '18,20,40,80,F0,88,88,70'
letters ['7'] = 'F8,08,10,20,40,40,40,40'
letters ['8'] = '70,88,88,70,88,88,88,70'
letters ['9'] = '70,88,88,88,78,08,10,60'
letters ['?'] = '70,88,88,10,20,20,00,20'
letters ['!'] = '20,20,20,20,20,20,00,20'
letters ['0'] = '70,88,98,A8,C8,88,88,70'
letters [':'] = '00,30,30,00,00,30,30,00'
letters ['@'] = '70,88,88,08,68,A8,A8,70'
letters ['&'] = '60,90,90,A0,40,A8,90,68'
letters ['('] = '10,20,40,40,40,40,20,10'
letters [')'] = '40,20,10,10,10,10,20,40'


 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (screen_x, screen_y)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock() 
# -------- Main Program Loop -----------
screen.fill(BLACK)
    
 
    # --- Drawing code should go here
DrawMessage(10,"Hello")
pygame.display.flip()
time.sleep(2)
# --- Limit to 60 frames per second
clock.tick(60)

# Close the window and quit.
pygame.quit()
