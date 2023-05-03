import pygame
from math import *
import time
pygame.init()
#settings___________________
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
black = (0,0,0)

#________________
pygame.display.set_caption("CAR")  # sets the window title
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # creates game screen
screen.fill(black)
clock = pygame.time.Clock() #set up clock


class Player():
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.velocity = 0
    def draw(self):
        pygame.draw.rect(screen, (200, 0, 100), (self.xpos, self.ypos, 100, 20))

    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            self.velocity = 1
        else:
            self.velocity = 0
        self.xpos += self.velocity
       
    def update(self,amount):
        self.input()
        self.draw()

player = Player(0,600)
world_shift = 0
while True:  
    clock.tick(60)
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
    #physics section-------------------------------------------
    if player.xpos < SCREEN_WIDTH / 10  and player.velocity < 0:
            world_shift = 8
            player.velocity = 0
    else:
        world_shift = 0

    screen.fill(black) #wipe screen so it doesn't smear

    player.update(world_shift)

    pygame.display.flip()#this actually puts the pixel on the screen
    
pygame.quit()
