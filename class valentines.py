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
        pygame.draw.circle(screen, (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)), (self.xpos, self.ypos), 20)
        pygame.draw.circle(screen, (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)), (self.xpos+40, self.ypos), 20)
        pygame.draw.polygon(screen, (random.randrange(1,255), random.randrange(1,255), random.randrange(1,255)), ((self.xpos-20, self.ypos+5), (self.xpos+59, self.ypos+5), (self.xpos+20, self.ypos+50)))

    def move(self):
        if self.ypos > 800:
            self.ypos = 0
            
        self.ypos += 3
    
    def update(self):
        self.move()
        self.draw()
        
rain = []

for i in range(70):
    rain.append(heart(random.randrange(1,750), random.randrange(1,750)))
#------------------------------------------------------------------------------------------------------------
v1 = heart(250,300)  
v2 = heart(500,500)

while True:
    clock.tick(60)
 
    screen.fill((0,0,0))
    v1.update()
    v2.update()
    
    for i in range(len(rain)):
        timer = rain[i].move()
        rain[i].draw()
        

    pygame.display.flip()

pygame.quit()
