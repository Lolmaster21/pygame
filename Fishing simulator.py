import pygame
#import bru
import random
pygame.init()  

pygame.display.set_caption("fish")  
screen = pygame.display.set_mode((800, 600))  
clock = pygame.time.Clock()

#variables---------------
doExit = False

class fish: #Fish variables 
  def __init__(self):
    self.xpos = random.randrange(0,700)
    self.ypos = random.randrange(100,450)
    self.vx = random.randrange(-3,3)
    self.vy = random.randrange(-3,3)
    self.red = random.randrange(0,100)
    self.green = random.randrange(100,250)
    self.blue = random.randrange(50,200)
    self.ticker = random.randrange(0,100)
    self.alive = True
    self.onHook = False
    
  def draw(self): #How to draw the fish 
    if self.alive is True:
      if self.vx <= 0:
        pygame.draw.ellipse(screen, (self.red,self.green,self.blue), (self.xpos, self.ypos, 25, 15))
        pygame.draw.circle(screen, (0, 0, 0), (self.xpos + 20, self.ypos + 5), 3)
        pygame.draw.polygon(screen, (self.red,self.green,self.blue), ((self.xpos + 5, self.ypos + 5), (self.xpos - 5, self.ypos - 5), (self.xpos - 5, self.ypos + 15)))
      else:
         pygame.draw.ellipse(screen, (self.red,self.green,self.blue), (self.xpos, self.ypos, 25, 15))
         pygame.draw.circle(screen, (0, 0, 0), (self.xpos + 5, self.ypos + 5), 3)
         pygame.draw.polygon(screen, (self.red,self.green,self.blue), ((self.xpos + 20, self.ypos + 5), (self.xpos + 30, self.ypos - 5), (self.xpos + 30, self.ypos + 15)))
  
  def move(self):# Fish movements 
    if self.xpos > 600:
      self.xpos = 600
      self.vx *= -1
    if self.xpos < 0:
      self.xpos = 0
      self.vx *= -1
    if self.ypos > 300:
      self.ypos = 300
      self.vy *= -1
    if self.ypos < 100:
      self.ypos = 100
      self.vy *= -1
    self.ticker+=1
    if self.ticker > 100:
      self.vx = random.randrange(-2,3)
      self.vy = random.randrange(-2,3)
      self.ticker = 0
    
    self.xpos += self.vx
    self.ypos += self.vy

  
    
school = list()

for i in range(20):
  school.append(fish())

#bru.PlayIntro()


#frank = fish()
#freddy = fish()
#francis = fish()

while doExit is False:

  clock.tick(60)


  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True


  

  #frank.move()
  #freddy.move()
  #francis.move()
  for i in range(20):
    school[i].move()
  #render section---------------------------------
  screen.fill((0, 0, 255))
  pygame.draw.rect(screen, (245,245,220), (0, 250, 800, 200))

  #frank.draw()
  #freddy.draw()
  #francis.draw()
  for i in range(20):
    school[i].draw()

  pygame.display.flip()

#end game loop------------------------------------
pygame.quit()
