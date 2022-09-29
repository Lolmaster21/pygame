import pygame
import random
import time
import pygame.freetype
pygame.init()
pygame.display.set_caption("Wire task")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
# font = pygame.freetype.Font("amatic.ttf", 80)

#colooorssss/ variables
YELLOW = (250,250,0)
RED = (200,0,0)
PINK = (200,0,200)
BLUE = (0,0,200)
WHITE = (255,255,255)
xpos = 0
ypos = 0
mousePos = (xpos, ypos) #variable mousePos stores TWO numbers
draw = False


numLines = 0 #variavle to keep track of number of lines so we only draw one at a time
BoxList = [] #list that holds the box objects
WireList = []
StartBox = 0
EndBox = 0

#lists that hold positions and colors of wire boxes
LeftPositions = [(0,100),(0,300),(0,500),(0,700)]
RightPositions = [(750,100),(750,300),(750,500),(750,700)]



#gameloop###################################################
while True:
#event queue (bucket that holds stuff that happens in game and passes to one of the sections below)
    event = pygame.event.wait()
#update/timer section---------------------------------------    
    if mousePos[0] > 0 and mousePos[0] < 50 and mousePos[1] >750:
        color = RED
    if mousePos[0] > 50 and mousePos[0] < 100 and mousePos[1] >750:
        color = BLUE
    #add other colors here!
#input section----------------------------------------------
    if event.type == pygame.QUIT: #close game window
        break

    if event.type == pygame.MOUSEBUTTONDOWN:
        draw = True

    if event.type == pygame.MOUSEBUTTONUP:
        draw = False

    if event.type == pygame.MOUSEMOTION:
        mousePos = event.pos
 
#render section---------------------------------------------
    if draw == True:
        pygame.draw.circle(screen, color, (mousePos), 10) #player paintbrush
    
    #color changing rectangles at bottom of screen 
    pygame.draw.rect(screen, RED, (LeftPositions[0][0],LeftPositions[0][1] ,50, 50))
    pygame.draw.rect(screen, BLUE, (LeftPositions[1][0],LeftPositions[1][1] ,50, 50))
    pygame.draw.rect(screen, YELLOW, (LeftPositions[2][0],LeftPositions[2][1] ,50, 50))
    pygame.draw.rect(screen, PINK, (LeftPositions[3][0],LeftPositions[3][1] ,50, 50))
    
    pygame.draw.rect(screen, RED, (RightPositions[0][0],RightPositions[0][1] ,50, 50))
    pygame.draw.rect(screen, BLUE, (RightPositions[1][0],RightPositions[1][1] ,50, 50))
    pygame.draw.rect(screen, YELLOW, (RightPositions[2][0],RightPositions[2][1] ,50, 50))
    pygame.draw.rect(screen, PINK, (RightPositions[3][0],RightPositions[3][1] ,50, 50))
    

    #more colors go here!
        
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()




