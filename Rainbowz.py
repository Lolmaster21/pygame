import pygame #import library (called "modules" in python)
from math import sin #so we don't have to type "math.sin" each time
from math import cos
import random

pygame.init()#initializes Pygame
pygame.display.set_caption("Valentine's Hearts")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 150))#paint background black

GameLoop = True #variable to run game loop


class rainbow:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def draw(self):
        #draws a heart using circles and triangles
        pygame.draw.circle(screen, (250, 250, 250), (self.x, self.y+100), 40)
        pygame.draw.circle(screen, (250, 250, 250), (self.x+100, self.y+100), 40)
        pygame.draw.circle(screen, (250, 250, 250), (self.x+50, self.y+100), 40)
        pygame.draw.circle(screen, (250, 250, 250), (self.x+50, self.y+50), 40)
        pygame.draw.arc(screen, (255, 0, 0), (self.x-25, self.y-60, 150, 150), 7*3.14/4, 5*3.14/4, 8)
        pygame.draw.arc(screen, (255, 255, 0), (self.x-15, self.y-45, 130, 120), 7*3.14/4, 5*3.14/4, 8)
        pygame.draw.arc(screen, (0, 255, 0), (self.x+5, self.y-35, 90, 100), 7*3.14/4, 5*3.14/4, 8)
        pygame.draw.arc(screen, (0, 0, 255), (self.x+10, self.y-20, 80, 90), 7*3.14/4, 5*3.14/4, 8)

        
#instantiate
r1 =rainbow(200, 300)
r2 =rainbow(400, 400)
r3 =rainbow(600,500)
# GAME LOOP-----------------------------------------------------------
while GameLoop:
    
    r1.draw()
    r2.draw()
    r3.draw()
    
    
    pygame.display.flip()
pygame.quit()
