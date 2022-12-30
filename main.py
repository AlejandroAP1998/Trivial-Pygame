import pygame
from pygame.locals import *

WIDTH,HEIGHT = 640,640
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Trivial")

WHITE = (255,255,255)


FPS = 60

def draw():
    WINDOW.fill(WHITE)
    pygame.display.update()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw()
    
    pygame.quit()


if __name__ == "__main__":
    main()



