import pygame
import math
import random
pygame.init()  # initializes Pygame
pygame.display.set_caption("Circles")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
clock = pygame.time.Clock() #sets up a game clock to regulate game speed

xpos = (random.randint(100,800))
ypos = (random.randint(0,800))
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers

GameLoop = True

while GameLoop:

#render section---------------------------------------------

    pygame.draw.circle(screen, (random.randint(1,255),random.randint(1,255),random.randint(1,255)), (xpos,ypos), 50) #player paintbrush
    
  
    pygame.display.flip()
pygame.quit()
