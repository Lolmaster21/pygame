import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#rainbow background
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
r2 =rainbow(400, 100)
r3 =rainbow(600,200)

#Creates sprite
#Link = pygame.image.load('fly2.png') #load your spritesheet
#Link.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#animation variables variables
frameWidth = 16
frameHeight = 16
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0


#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3
#Keyboard controls
a = 4
d = 5
w = 6
s = 7


#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
#player variables
xpos2 = 500 #xpos of player
ypos2 = 200 #ypos of player
vx2 = 0 #x velocity of player
vy2 = 0 #y velocity of player
keys = [False, False, False, False,False, False, False, False] #this list holds whether each key has been pressed
 #this list holds whether each key has been pressed

isOnGround = False #this variable stops gravity from pulling you down more when on a platform
isOnGround2 = False #player2


while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True

            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
                
            if event.key == pygame.K_a:
                keys[a]=True

            elif event.key == pygame.K_w:
                keys[w]=True

            elif event.key == pygame.K_d:
                keys[d]=True
                    
# Input KEYUP
            
        #Player 1 Input
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
                
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False   
                
          #Player 2 Input
       
            if event.key == pygame.K_a:
                keys[a]=False

            elif event.key == pygame.K_w:
                keys[w]=False

            elif event.key == pygame.K_d:
                keys[d]=False
                
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
        
    elif keys[a]==True:
        vx2=-3
        direction = LEFT

    #RIGHT MOVEMENT
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT
        
    elif keys[d]==True:
        vx2=3
        direction = RIGHT

    #turn off velocity
    else:
        vx = 0
        vx2 = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
        
    if keys[w] == True and isOnGround2 == True: #only jump when on the ground
        vy2 = -8
        isOnGround2 = False
        direction = UP
    
    

    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>600 and xpos<700 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>400 and xpos<500 and ypos+40 >550 and ypos+40 <570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>500 and xpos<600 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False
    #P2
    if xpos2>100 and xpos2<200 and ypos2+40 >750 and ypos2+40 <770:
        ypos2 = 750-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>200 and xpos2<300 and ypos2+40 >650 and ypos2+40 <670:
        ypos2 = 650-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>600 and xpos2<700 and ypos2+40 >650 and ypos2+40 <670:
        ypos2 = 650-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>400 and xpos2<500 and ypos2+40 >550 and ypos2+40 <570:
        ypos2 = 550-40
        isOnGround2 = True
        vy2 = 0
    elif xpos2>500 and xpos2<600 and ypos2+40 >750 and ypos2+40 <770:
        ypos2 = 750-40
        isOnGround2 = True
        vy2 = 0
    else:
        isOnGround2 = False

    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    #2
    if ypos2 > 760:
        isOnGround2 = True
        vy2 = 0
        ypos2 = 760
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
        
    if isOnGround2 == False:
        vy2+=.2

    #update player position
    xpos+=vx 
    ypos+=vy
    xpos2+=vx2 
    ypos2+=vy2
    
     #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information
    # Only animate when in motion
    
    if vx>0:
        RowNum = 0
    if vx < 0: #left animation
        RowNum = 0
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker+=1
    if vx > 0: #right animation
        RowNum = 1
        # Ticker is a spedometer. We don't want Link animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker+=1
    if ticker%10==0: #only change frames every 10 ticks
        frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        #ticker+=1
    if frameNum>3: 
        frameNum = 0
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    #Player 1
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    
    #Player 2
    pygame.draw.rect(screen, (200, 100, 100), (xpos2, ypos2, 20, 40))
    
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (100, 0, 200), (200, 650, 100, 20))

    #Third platform
    pygame.draw.rect(screen, (100, 200, 0), (600, 650, 100, 20))
    
    #4 platform
    pygame.draw.rect(screen, (255, 100, 200), (400, 550, 100, 20))

    #5 platform
    pygame.draw.rect(screen, (0, 100, 200), (500, 750, 100, 20))
    
    #rainbowss
    r1.draw()
    r2.draw()
    r3.draw()
    
    #sprite loading
    #screen.blit(Link, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))
  

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
