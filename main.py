import pygame
from blocks import Blocks

pygame.init()

blocks = Blocks()

blocks.block_init()
print(blocks.blocks)
loop = True
while loop:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            loop = False
    
    pygame.display.set_caption("Tetris By MrGio7")

    
    blocks.draw_bg()
    blocks.block_draw()
    blocks.block_drop()

    pygame.display.flip()