import pygame
import time
pygame.init()
pygame.display.set_caption("Data structures")
screenSize = (800,800)
screen = pygame.display.set_mode(screenSize)


PURPLE = (230,230,250)

circ1 = [200,100]
circ2 = [200,200]
circ3 = [200,300]
circ4 = [200,400]
circ5 = [400,500]

coordinates = [circ1,circ2,circ3,circ4,circ5]

print(coordinates)


for i in range(len(coordinates)):
    pygame.draw.circle(screen,PURPLE,(coordinates[i]),50)


pygame.display.flip()
time.sleep(100)
pygame.quit
