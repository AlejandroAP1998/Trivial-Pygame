import pygame
from pygame.locals import *

WIDTH,HEIGHT = 640,640
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Trivial")

WHITE = (255,255,255)




def draw():
    WINDOW.fill(WHITE)
    pygame.display.update()

def main():
    pygame.init()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    
    pygame.quit()


if __name__ == "__main__":
    main()



