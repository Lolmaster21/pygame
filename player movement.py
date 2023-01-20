import pygame
from math import *
import time
pygame.init()  
pygame.display.set_caption("Space Invaders")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock


class Player():
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def draw(self):
        pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))


p1= Player(50,50)

while True:  
    clock.tick(60)

    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      

    #physics section-------------------------------------------

   
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
     
    p1.draw()
  

    pygame.display.flip()#this actually puts the pixel on the screen
    
pygame.quit()
