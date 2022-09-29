import pygame
import random
import time
import pygame.freetype
pygame.init()
pygame.display.set_caption("Wire task")
screen = pygame.display.set_mode((800,800))
screen.fill((0,0,0))
font = pygame.freetype.Font("amatic.ttf", 80)

#colooorssss
YELLOW = (250,250,0)
RED = (200,0,0)
PINK = (200,0,200)
BLUE = (0,0,200)
WHITE = (255,255,255)

numLines = 0 #variavle to keep track of number of lines so we only draw one at a time
BoxList = [] #list that holds the box objects
WireList = []
StartBox = 0
EndBox = 0

#lists that hold positions and colors of wire boxes
LeftPositions = [(100,100),(100,300),(100,500),(100,700)]
RightPositions = [(550,100),(550,300),(550,500),(550,700)]

