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

keys = [False, False, False, False,False, False, False, False] #this list holds whether each key has been pressed
#this list holds whether each key has been pressed



while not gameover: #GAME LOOP------------------------------------------------
    clock.tick(60) #FPS
    
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
    pygame.draw.rect(screen, (0, 250,0), (xpos, ypos, 70, 25))
    pygame.draw.rect(screen, (0, 250,0), (xpos+15, ypos-15, 40, 15))
    pygame.draw.rect(screen, (0, 250,0), (xpos+28, ypos-20, 15, 10))

  

    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
