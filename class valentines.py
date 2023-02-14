import pygame
from math import sin 
from math import cos

pygame.init()
pygame.display.set_caption("Valentine's Hearts")
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))

GameLoop = True #variable to run game loop


class heart:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (250, 100, 100), (self.xpos, self.ypos), 20)
        pygame.draw.circle(screen, (250, 100, 100), (self.xpos+40, self.ypos), 20)
        pygame.draw.polygon(screen, (250, 100, 100), ((self.xpos-20, self.ypos+5), (self.xpos+59, self.ypos+5), (self.xpos+20, self.ypos+50)))
#------------------------------------------------------------------------------------------------------------
v1 = heart(250,300)  
v2 = heart(500,500)

while GameLoop:
    
    event = pygame.event.wait()
 
    
    v1.draw()
    v2.draw()
    pygame.display.flip()
    
pygame.quit()
