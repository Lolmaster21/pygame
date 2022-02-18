import pygame #import library (called "modules" in python)
from math import sin #so we don't have to type "math.sin" each time
from math import cos
import random

pygame.init()#initializes Pygame
pygame.display.set_caption("Quiz 5")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 150))#paint background black

GameLoop = True #variable to run game loop


class butterfly:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos
    def draw(self):
        #draws a heart using circles and triangles
        pygame.draw.circle(screen, (150, 0, 220), (self.x, self.y+100), 50)#Bottom left circle
        
        pygame.draw.circle(screen, (150, 0, 180), (self.x-10, self.y+40), 60)#Bottom right circle
        
        pygame.draw.circle(screen, (150, 0, 180), (self.x+45, self.y+45), 60)#Top right circle
        
        pygame.draw.circle(screen, (150, 0, 220), (self.x+50, self.y+100), 50)#Top left circle
        
        pygame.draw.circle(screen, (150, 0, 180), (self.x+45, self.y+45), 60)#Top right circle
        
        pygame.draw.line(screen,(0,0,0),(self.x+10,self.y-80),(self.x+20,self.y-20),5) #Right antena 
        
        pygame.draw.line(screen,(0,0,0),(self.x+40,self.y-75),(self.x+30,self.y-20),5) #Right antena 
    
        
        pygame.draw.ellipse(screen, (255, 255, 0), (self.x, self.y-20, 50, 200))#Yellow body
        
        pygame.draw.arc(screen, (200, 100, 0), (self.x-40, self.y-35, 140, 140), 4*3.14/3, 5*3.14/3, 5)
        
        pygame.draw.arc(screen, (200, 100, 0), (self.x-40, self.y-45, 140, 140), 4*3.14/3, 5*3.14/3, 5)

        pygame.draw.arc(screen, (200, 100, 0), (self.x-40, self.y-60, 135, 130), 4*3.14/3, 5*3.14/3, 5)
        
        pygame.draw.arc(screen, (200, 100, 0), (self.x-40, self.y-75, 135, 130), 4*3.14/3, 5*3.14/3, 5)

        pygame.draw.arc(screen, (200, 100, 0), (self.x-40, self.y-90, 135, 130), 4*3.14/3, 5*3.14/3, 5)

#instantiate
r1 =butterfly(200, 300)
r2 =butterfly(400, 400)
r3 =butterfly(600,500)
# GAME LOOP-----------------------------------------------------------
while GameLoop:

    r1.draw()
    r2.draw()
    r3.draw()
    
    
    pygame.display.flip()
pygame.quit()
