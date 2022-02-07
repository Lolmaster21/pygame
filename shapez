import pygame #handles graphics, sound, game timings, keyboard input, etc
import math
pygame.init()
#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Silly Shapes")
while True: #sortof a game loop
    
#a few example shapes

    
    pygame.draw.ellipse(screen, (255, 255, 0), (200, 100, 20, 40)) #ellipse
       
    pygame.draw.rect(screen, (255, 255, 255), (400, 400, 20, 20)) #rectangle
      
    pygame.draw.polygon(screen, (100, 0, 100), ((100, 100), (200, 400), (400, 400))) #polygon
          
    pygame.draw.line(screen,(120,50,250),(120,90),(170,150)) #Line
    
    pygame.draw.lines(screen,(120,50,250),0,[(120,90),(170,450), (400, 500),(500, 100)], 20) 
    
    pygame.draw.circle(screen,(100,200,250),(20,40),12) #circle
    pygame.draw.arc(screen, (100,200,250), (400, 100, 200, 500), 0,3.14, 5)
    
    pygame.display.flip() #update graphics 
pygame.quit()
