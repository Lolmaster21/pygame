import pygame #import library (called "modules" in python)
from math import sin #so we don't have to type "math.sin" each time
from math import cos

pygame.init()#initializes Pygame
pygame.display.set_caption("Valentine's Hearts")#sets the window title
screen = pygame.display.set_mode((800, 800))#creates game screen
screen.fill((0, 0, 0))#paint background black

GameLoop = True #variable to run game loop

t=0;
# GAME LOOP-----------------------------------------------------------
while GameLoop:
    t+=1;
    xpos = -32*sin(t)*sin(t)*sin(t)+400
    ypos = -26*cos(t)+10*cos(2*t)+4*cos(3*t)+2*cos(4*t)+50
    pygame.draw.circle(screen,(250,0,0),(xpos,ypos), 1)

    xpos2 = -32*sin(t)*sin(t)*sin(t)+400
    ypos2 = -26*cos(t)+10*cos(2*t)+4*cos(3*t)+2*cos(4*t)+100
    pygame.draw.circle(screen,(250,0,255),(xpos2,ypos2), 1)

    xpos3 = -32*sin(t)*sin(t)*sin(t)+400
    ypos3 = -26*cos(t)+10*cos(2*t)+4*cos(3*t)+2*cos(4*t)+150
    pygame.draw.circle(screen,(250,250,55),(xpos3,ypos3), 1)

    xpos4 = -32*sin(t)*sin(t)*sin(t)+400
    ypos4 = -26*cos(t)+10*cos(2*t)+4*cos(3*t)+2*cos(4*t)+200
    pygame.draw.circle(screen,(250,68,5),(xpos4,ypos4), 1)

    xpos5 = -32*sin(t)*sin(t)*sin(t)+400
    ypos5 = -26*cos(t)+10*cos(2*t)+4*cos(3*t)+2*cos(4*t)+250
    pygame.draw.circle(screen,(150,60,85),(xpos5,ypos5), 1)

    xpos6 = -32*sin(t)*sin(t)*sin(t)+400
    ypos6 = -26*cos(t)+10*cos(2*t)+4*cos(3*t)+2*cos(4*t)+300
    pygame.draw.circle(screen,(250,156,255),(xpos6,ypos6), 1)


   
    #draws a heart using circles and triangles
    pygame.draw.circle(screen, (250, 100, 100), (200, 200), 21)
    pygame.draw.circle(screen, (250, 100, 100), (240, 200), 21)
    pygame.draw.polygon(screen, (250, 100, 100), ((180, 205), (260, 205), (220, 250)))
   
    #draws a heart using lines and arcs
    pygame.draw.arc(screen, (250, 0, 0), (180, 180, 40, 40), 0, 3.14,5)
    pygame.draw.arc(screen, (250, 0, 0), (220, 180, 40, 40), 0, 3.14,5)
    pygame.draw.line(screen, (250, 0, 0), (220, 250), (180, 200), 5)
    pygame.draw.line(screen, (250, 0, 0), (220, 250), (260, 200), 5)
    pygame.display.flip()
pygame.quit()
