"""
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

WHITE = ( 255, 255, 255)
RED = ( 255, 0, 0)

rows = 5;
width = 10; 
block_size = 0.1; 

for y in range(rows):
    for x in range(width):
        rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
        pygame.draw.rect(screen, WHITE, rect, 1)

pygame.draw.rect(screen, WHITE, pygame.Rect(45, 60, 60, 60), 1)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip() 
"""

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
#for row in range(10):
for row in range(20):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
    #for column in range(20): 
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[0][5] = 1
 
# Initialize pygame
pygame.init()
 
# Set the WIDTH and HEIGHT of the screen
# WINDOW_SIZE = [255, 255]
WINDOW_SIZE = [255 , 510]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(20):
    #for row in range(20):
        for column in range(10):
        #for column in range(20):
            color = WHITE
            if grid[row][column] == 1:
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)


# win = pygame.display
# surface = win.set_mode([400,400])
# loadimage = pygame.image.load('Car.jpeg')
# window = True

# while window:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             window = False 
#     surface.blit(loadimage,(200,200))
#     win.update()
#     # Go ahead and update the screen with what we've drawn.
pygame.display.flip()
 
# # Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()