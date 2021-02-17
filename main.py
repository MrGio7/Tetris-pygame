import pygame
from blocks import Blocks
from menu import Menu

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

    if blocks.state == "Menu":
        blocks.text("Menu", 160, blocks.WHITE, 50)
        blocks.text("START", 100, blocks.GREEN, 350)
        blocks.start("Game")
        blocks.text("Choose Difficulty:", 50, blocks.WHITE, 550)
        blocks.text("Easy", 35, blocks.WHITE, 600)
        blocks.dif_choose("Easy")
        blocks.text("Medium", 35, blocks.WHITE, 650)
        blocks.dif_choose("Medium")
        blocks.text("Hard", 35, blocks.WHITE, 700)
        blocks.dif_choose("Hard")
    elif blocks.state == "Game":
        blocks.draw_grid()
        blocks.draw_bg()
        blocks.block_drop()
        blocks.block_draw()
        blocks.line_pop()

    pygame.display.flip()