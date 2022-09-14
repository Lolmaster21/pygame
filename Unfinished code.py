import pygame
pygame.init

#constants for colors
RED = (250,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)

### class definition--------------------------------------------
class flower:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
       
    def draw(xpos,ypos):
        pygame.draw.rect(screen, (GREEN), (xpos-10, ypos+20, 20, 100)) #(190, 330) is my top left corner
        pygame.draw.circle(screen, (RED), (xpos-20, ypos+20), 20)
        pygame.draw.circle(screen, (RED), (xpos-20, ypos-20), 20)
        #add missing petals here
        pygame.draw.circle(screen, (RED), (xpos+20, ypos-20), 20)
        pygame.draw.circle(screen, (RED), (xpos+20, ypos+20), 20)
        pygame.draw.circle(screen, (ORANGE), (xpos, ypos), 20)
       

# end of class definition-----------------------------------------


#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("flower class demo")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed


#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
    choice = 0
    while choice != 'q':
        print("Give me a x")
        xpos = int(input())
        print("Give me a y")
        ypos = int(input())
        
    flower.draw()
     
    #render section-----------------------------------
     

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()

