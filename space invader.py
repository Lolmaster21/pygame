import pygame
pygame.init()  
pygame.display.set_caption("Space Invaders")  # sets the window title
screen = pygame.display.set_mode((1000, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2

#player variables
xpos = 430 #xpos of player
ypos = 750 #ypos of player
vx = 0 #x velocity of player
timer = 0;

keys = [False, False, False, False,False, False, False, False] #this list holds whether each key has been pressed
#this list holds whether each key has been pressed

class Alien:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.isAlive = True
        self.direction = 1
    
    def draw(self):
        pygame.draw.rect(screen,(250,250,250),(self.xpos,self.ypos, 40,40))
    
    def move(self, time):
        if timer %100==0:
            self.ypos += 100
            self.direction =-1
            return 0
        if time % 100 == 0:
            self.xpos += 50*self.direction
            
        return time
            
            
    
        
            

bob = []
for i in range(4):
    for j in range(10):
        bob.append(Alien(j*70+30, i*70+30))

while not gameover: #GAME LOOP------------------------------------------------
    clock.tick(60) #FPS
    timer += 1
   

    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
          
                    
# Input KEYUP
            
        #Player 1 Input
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            
            if event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
  

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
        
  

    #RIGHT MOVEMENT
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT

    #turn off velocity
    else:
        vx = 0

    #update player position
    xpos+=vx 
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    
    #Player 1
    pygame.draw.rect(screen, (0, 250,0), (xpos, 750, 60, 20))
    pygame.draw.rect(screen, (0, 250,0), (xpos+5, 745, 50, 20))
    pygame.draw.rect(screen, (0, 250,0), (xpos+25, 736, 10, 20))
    pygame.draw.rect(screen, (0, 250,0), (xpos+28, 732, 4, 20))
    
    for i in range (len(bob)):
        timer = bob[i].move(timer)

  

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
