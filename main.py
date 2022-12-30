import pygame
from pygame.locals import *
import cmath
import numpy as np

WIDTH,HEIGHT = 900,790
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Trivial")

WHITE = (255,255,255)
BLACK = (0,0,0)

CENTER = (WIDTH/2,HEIGHT/2)
RADIUS1 = HEIGHT/2 -10
RADIUS2 = HEIGHT/2 -110
RADIUS3 = 70
FPS = 60

def split_circ(cen,r,n):
    # Divide la circunferencia de centro cen y radio r en n partes iguales y devuelve un array con las coordenadas de la partición.
    lista = []
    x,y = cen
    for i in range(n):
        rect = cmath.rect(r,(2*cmath.pi*i)/n)
        lista.append([round(x+rect.real),round(y+rect.imag)])
    return lista

def mult(a,v):
    #Multiplica el escalar a por el vector bidimensional v, y devuelve la tupla de coordenadas del vector resultado.
    prod = np.dot(a,v)
    return prod[0],prod[1]

def suma(u,v):
    #Suma los vectores bidimensionales u y v, y devuelve la tupla de coordenadas del vector resultado.
    s = np.add(u,v)
    return s[0],s[1]


def draw_board():
    pygame.draw.circle(WINDOW, BLACK,CENTER,RADIUS1,1)
    pygame.draw.circle(WINDOW, BLACK,CENTER,RADIUS2,1)
    part1 = split_circ(CENTER,RADIUS1,48)
    part2 = split_circ(CENTER,RADIUS2,48)
    part3 = split_circ(CENTER,RADIUS3,6)
    for i in range(48):
        if i not in [4,12,20,28,36,44]:
            pygame.draw.line(WINDOW,BLACK,part1[i],part2[i])
        if i in [3,5,11,13,19,21,27,29,35,37,43]:
            pygame.draw.line(WINDOW,BLACK,part2[i],part3[round(i/8)])
    pygame.draw.line(WINDOW,BLACK,part2[45],part3[0])
    pygame.draw.polygon(WINDOW,BLACK,part3,1)

    for i in [3,11,19,27,35]:
        for j in range(1,5):
            k = round(i/8)
            pygame.draw.line(WINDOW,BLACK,suma(mult(j/5,part2[i]),mult((5-j)/5,part3[k])),suma(mult(j/5,part2[i+2]),mult((5-j)/5,part3[k+1])))
    for j in range(1,5):
        pygame.draw.line(WINDOW,BLACK,suma(mult(j/5,part2[43]),mult((5-j)/5,part3[5])),suma(mult(j/5,part2[45]),mult((5-j)/5,part3[0])))



def draw_window():
    WINDOW.fill(WHITE)
    draw_board()
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
        draw_window()
    
    pygame.quit()


if __name__ == "__main__":
    main()



