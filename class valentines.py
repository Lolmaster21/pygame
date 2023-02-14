import pygame
import random

pygame.init()
pygame.display.set_caption("Valentine's Hearts")
screen = pygame.display.set_mode((800, 800))
screen.fill((0, 0, 0))
clock = pygame.time.Clock() #set up clock

timer = 0;

GameLoop = True #variable to run game loop



class heart:
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        
        color1 = random.randrange(0,255)
        color2 = random.randrange(0,255)
        color3 = random.randrange(0,255)
        pygame.draw.circle(screen, (color1,color2,color3),(self.xpos,self.ypos),20)
        pygame.draw.circle(screen, (color1,color2,color3),(self.xpos+40,self.ypos),20)
        pygame.draw.polygon(screen,(color1,color2,color3),((self.xpos-20,self.ypos+5),(self.xpos+59, self.ypos+5),(self.xpos+20,self.ypos+50)))

    def move(self):
        if self.ypos > 800:
            self.ypos = 0
            
        self.ypos += 3
    
    def update(self):
        self.move()
        self.draw()
        
love = []
love =[heart(random.randrange(0,800),random.randrange(0,800)) for i in range(90)]


#------------------------------------------------------------------------------------------------------------
v1 = heart(250,300)  
v2 = heart(500,500)

while True:
    clock.tick(60)
 
    screen.fill((0,0,0))
    v1.update()
    v2.update()
    
    for i in range(len(love)):
        timer = love[i].move()
        love[i].draw()
        

    pygame.display.flip()

pygame.quit()
