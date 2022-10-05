import pygame
import time
pygame.init()
pygame.display.set_caption("Data structures")
screenSize = (800,800)
screen = pygame.display.set_mode(screenSize)


YELLOW = (250,250,0)
RED = (200,0,0)
FRANDS = ("Jesse","Ricardo","Kevin","Simon","Random name")
pygame.draw.circle(screen,YELLOW,(200,200),100)
print(FRANDS)
print(FRANDS[2])

pygame.display.flip()
time.sleep(100)
pygame.quit
