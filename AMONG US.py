import pygame
import random
import time
import pygame.freetype
pygame.init()
pygame.display.set_caption("Wire task")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
# font = pygame.freetype.Font("amatic.ttf", 80)

#Boxie-------------------------------------------------------------------------
class Box():
    def __init__(self,position,color):
        self.position = position
        self.color = color
        self.connected = False
        self.clicked = False
        self.hovering = False
        
    def BBcollision(xpos,ypos,x,y):
        if x<xpos+100 and x>xpos and y>ypos and y<ypos+50:
            return True
        else:
            False
            
        def isHovering(self, MouseX, Mousey):
            if BBcollision(self.position[0],self.position[1],MouseX,Mousey)==True:
                self.hovering = True
            else:
                self.hovering = False
    

    
#Drawing class-----------------------------------------------
    def draw():
        pygame.draw.rect(screen,self.color, (self.position[0],self.position[1],100, 50))
    
        if self.hovering == True:
            pygame.draw.rect(screen,(255,255,255), (self.position[0],self.position[1],100, 50),2)

        
    

#colooorssss/ variables
YELLOW = (250,250,0)
RED = (200,0,0)
PINK = (200,0,200)
BLUE = (0,0,200)
WHITE = (255,255,255)
xpos = 0
ypos = 0
#variable mousePos stores TWO numbers
draw = False
mouseDown = False
mousePos = (0,0)


numLines = 0 #variavle to keep track of number of lines so we only draw one at a time
BoxList = [] #list that holds the box objects
WireList = []
StartBox = 0
EndBox = 0

#lists that hold positions and colors of wire boxes
LeftPosition = [(0,100),(0,300),(0,500),(0,700)]
RightPosition = [(750,100),(750,300),(750,500),(750,700)]
LeftColors = [RED, YELLOW, PINK, BLUE]
RightColors = [RED, YELLOW, PINK, BLUE]
random.shuffle(LeftColors)
random.shuffle(RightColors)
random.shuffle(LeftPosition)
random.shuffle(RightPosition)

#More boxesssss
for i in range(4):
    BoxList.append(Box(LeftPosition[i], LeftColors[i]))
    BoxList.append(Box(RightPosition[i], RightColors[i]))



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
#physics section--------------------------------------------
        for i in range(len(BoxList)):
            BoxList[i].isHovering(mousePos[0],mousePos[1])

 
#render section---------------------------------------------
    screen.fill((0,0,0))
    
    for i in range(len(BoxList)):
        BoxList[i].draw()
        
    pygame.display.flip()
    

#end game loop##############################################

pygame.quit()





