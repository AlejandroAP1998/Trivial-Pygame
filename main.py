import pygame
from pygame.locals import *
import cmath
import math
import numpy as np

WIDTH,HEIGHT = 900,790
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Trivial")

WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (200,200,200)
PINK = (255,103,204)
YELLOW = (255,255,102)
GREEN = (0,204,102)
ORANGE = (255,128,0)
BLUE = (0,222,255)
PURPLE = (204,0,204)
BACKGROUND = (0,76,153)
COLORS = [PINK,YELLOW,GREEN,ORANGE,BLUE,PURPLE,WHITE]

# Filas que salen desde el círculo exterior hacia el centro. El primer color es la casilla grande, que otorga quesito.
COL1 = [4,0,2,1,3,5]
COL2 = [3,2,5,0,1,4]
COL3 = [1,5,4,2,0,3]
COL4 = [0,4,3,5,2,1]
COL5 = [2,3,1,4,5,0]
COL6 = [5,1,0,3,4,2]

# Tramos entre quesito y quesito, tomando como referencia los números asignados a cada quesito anteriormente.
COL1TO2 = [0,6,1,5,6,2]
COL2TO3 = [2,6,0,4,6,5]
COL3TO4 = [5,6,2,3,6,4]
COL4TO5 = [4,6,5,1,6,3]
COL5TO6 = [3,6,4,0,6,1]
COL6TO1 = [1,6,3,2,6,0]


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

PART1 = split_circ(CENTER,RADIUS1,48)
PART2 = split_circ(CENTER,RADIUS2,48)
PART3 = split_circ(CENTER,RADIUS3,6) #Divisiones para los caminos interiores

def mult(a,v):
    #Multiplica el escalar a por el vector bidimensional v, y devuelve la tupla de coordenadas del vector resultado.
    prod = np.dot(a,v)
    return prod[0],prod[1]

def suma(u,v):
    #Suma los vectores bidimensionales u y v, y devuelve la tupla de coordenadas del vector resultado.
    s = np.add(u,v)
    return s[0],s[1]

def polares(x,y,cen=CENTER):
    #Calcula las coordenadas polares (r,theta) del punto (x,y) respecto al punto origen cen
    r = round(np.sqrt((cen[0]-x)**2 + (cen[1]-y)**2))
    theta = -math.atan2(y-cen[1],x-cen[0])
    return r,theta


def draw_board():
    pygame.draw.circle(WINDOW, GREY,CENTER,RADIUS1,0)
    pygame.draw.circle(WINDOW, BLACK,CENTER,RADIUS1,1)
    pygame.draw.circle(WINDOW, BACKGROUND,CENTER,RADIUS2,0)
    

    for i in range(5): 
        pygame.draw.polygon(WINDOW,GREY,[PART3[i],PART3[i+1],PART2[5+8*i],PART2[3+8*i]])
    pygame.draw.polygon(WINDOW,GREY,[PART3[5],PART3[0],PART2[45],PART2[43]])
    pygame.draw.circle(WINDOW, BLACK,CENTER,RADIUS2,1)

    for i in range(48):
        if i not in [4,12,20,28,36,44]:
            pygame.draw.line(WINDOW,BLACK,PART1[i],PART2[i])
        if i in [3,5,11,13,19,21,27,29,35,37,43]:
            pygame.draw.line(WINDOW,BLACK,PART2[i],PART3[round(i/8)])
    pygame.draw.line(WINDOW,BLACK,PART2[45],PART3[0])

    pygame.draw.polygon(WINDOW,GREY,PART3,0)
    pygame.draw.polygon(WINDOW,BLACK,PART3,1)


    for i in [3,11,19,27,35]:
        for j in range(1,5):
            k = round(i/8)
            pygame.draw.line(WINDOW,BLACK,suma(mult(j/5,PART2[i]),mult((5-j)/5,PART3[k])),suma(mult(j/5,PART2[i+2]),mult((5-j)/5,PART3[k+1])))
    for j in range(1,5):
        pygame.draw.line(WINDOW,BLACK,suma(mult(j/5,PART2[43]),mult((5-j)/5,PART3[5])),suma(mult(j/5,PART2[45]),mult((5-j)/5,PART3[0])))



def draw_window():
    WINDOW.fill(BACKGROUND)
    draw_board()
    pygame.display.update()

def main():
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #Permite cerrar el juego
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN: # Cuando se hace clic con cualquier botón del ratón
                lc,mc,rc = pygame.mouse.get_pressed()
                if lc == 1: # Cuando se hace clic izquierdo
                    x,y = pygame.mouse.get_pos()
                    r,theta = polares(x,y)
                    if RADIUS2 <= r <= RADIUS1: # Clic en la zona circular del tablero
                        print(theta)
                    
                    
        draw_window()
    
    pygame.quit()


if __name__ == "__main__":
    main()

