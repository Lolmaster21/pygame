import pygame
import random
pygame.init()  # initalizes Pygame
pygame.display.set_caption("TV!")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen 
clock = pygame.time.Clock()# start game clock

#game varialbles---------------------------------------------
doExit = False #this variable controls our game loop
xpos = 0
ypos = 0 

class ractangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def update():
        if self.y>800:
            self.y = -20
            self.x = random.randrange(0,800)
    def draw(self):
        pygame.draw.rect(screen,(200,200,200),(self.x, self.y, 50, 50),10)
    def move(self):
        self.y+=1
#-----------------------------------------------
r1 = ractangle(300,0)
r2 = ractangle(400,0)
r3 = ractangle(500,0)
r4 = ractangle(600,0)
r5 = ractangle(700,0)
r6 = ractangle(800,0)
r7 = ractangle(100,0)
r8 = ractangle(200,0)
r9 = ractangle(300,0)
r10 = ractangle(350,0)
r11 = ractangle(450,0)
r12 = ractangle(550,0)
r13 = ractangle(650,0)
#game loop#######################################
while not doExit:
    clock.tick(60)
#physics section-----------------------------
    #lets you quit the game from the gamescreen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True
   
    
    r1.move()
    r1.draw()
    r2.move()
    r2.draw()
    r3.move()
    r3.draw()
    r4.move()
    r4.draw()
    r5.move()
    r5.draw()
    r6.move()
    r6.draw()
    r7.move()
    r7.draw()
    r8.move()
    r8.draw()
    r9.move()
    r9.draw()
    r10.move()
    r10.draw()
    r11.move()
    r11.draw()
    r12.move()
    r12.draw()
    r13.move()
    r13.draw()
    
#render section-------------------------------
    screen.fill((0, 0, 0)) #clear screen between loops

    r1.draw()
    r2.draw()
    r3.draw()
    r4.draw()
    r5.draw()
    r6.draw()
    r7.draw()
    r8.draw()
    r9.draw()
    r10.draw()
    r11.draw()
    r12.draw()
    r13.draw()
    pygame.display.flip() #draws all the stuff above the screen    
    
#####################################end game loop
pygame.quit()


