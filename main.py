import pygame
from window import Window

pygame.init()

window = Window()

loop = True
while loop:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            loop = False
    
    pygame.display.set_caption("Tetris By MrGio7")

    window.draw_bg()

    pygame.display.flip()