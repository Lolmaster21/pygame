import pygame
#import bru
import random
pygame.init()  

pygame.display.set_caption("fish")  
screen = pygame.display.set_mode((800, 800))  
clock = pygame.time.Clock()

#variables---------------
doExit = False

class fish: #Fish variables 
  def __init__(self):
    self.xpos = random.randrange(0,600)
    self.ypos = random.randrange(100,450)
    self.vx = random.randrange(-3,3)
    self.vy = random.randrange(-3,3)
    self.red = random.randrange(0,100)
    self.green = random.randrange(100,250)
    self.blue = random.randrange(50,200)
    self.ticker = random.randrange(0,100)
    self.alive = True
    self.onHook = False
    self.hunger = 200
    
    
    
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
  def hung(self):
      while doExit == False:
          if self.hunger > 0:
              pygame.draw.rect(screen, (255,0,0), (20, 20, self.hunger, 20))
              self.hunger -= 1
          if self.hunger <=0:
              self.hunger = 0
          
  
  def move(self):# Fish movements 
    if self.xpos > 600:
      self.xpos = 600
      self.vx *= -1
    if self.xpos < 200:
      self.xpos = 200
      self.vx *= -1
    if self.ypos > 600:
      self.ypos = 600
      self.vy *= -1
    if self.ypos < 200:
      self.ypos = 200
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




while doExit is False:

  clock.tick(60)


  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            doExit = True


  


  for i in range(20):
    school[i].move()
  #render section---------------------------------
  screen.fill((0, 0, 255))
  pygame.draw.rect(screen, (240,240,220), (0, 250, 800, 200))#Ocean floor 
  pygame.draw.rect(screen, (192,192,192), (650, 490, 75, 100))#Fish food
  
  pygame.draw.rect(screen, (0,0,0), (200, 200, 420, 420),10)
  #fish logo 
  pygame.draw.ellipse(screen, (255, 128, 0), (680, 535, 40, 30))
  pygame.draw.ellipse(screen, (0,0,0), (700, 540, 10, 10))
  pygame.draw.polygon(screen, (255, 128, 0), ((690,510), (680, 520), (710, 540)))
  pygame.draw.polygon(screen, (255, 128, 0), ((680,530), (640, 550), (680, 570)))

  
  for i in range(20):
    school[i].draw()
  pygame.display.flip()

#end game loop------------------------------------
pygame.quit()
