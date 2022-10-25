import pygame
import sys


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        self.clock =pygame.time.clock()
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            dt= self.clock.tick()/1000
            pygame.display.update()
        #end of game loop------------------------------------------
            

#---------- main(starting point of program)-------------------------------------
if __name__=='__main__':
    game = Game()
    game.run()
