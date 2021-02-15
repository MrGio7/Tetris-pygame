import pygame
from blocks import Blocks

pygame.init()

blocks = Blocks()

clock = pygame.time.Clock()
loop = True
while loop:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            loop = False
    
    pygame.display.set_caption("Tetris By MrGio7")

    blocks.draw_bg()
    blocks.block_draw()

    pygame.display.flip()