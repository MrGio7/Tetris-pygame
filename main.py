import pygame
from blocks import Blocks
from menu import Menu

pygame.init()

blocks = Blocks()
menu = Menu()

clock = pygame.time.Clock()
loop = True
while loop:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            loop = False
    
    pygame.display.set_caption("Tetris By MrGio7")

    if menu.state == "Menu":
        menu.text("Menu", 160, menu.WHITE, 50)
        menu.text("START", 100, menu.GREEN, 350)
        menu.click("Game")
        menu.text("Choose Difficulty:", 50, menu.WHITE, 550)
        menu.text("Easy", 35, menu.WHITE, 600)
        menu.text("Medium", 35, menu.WHITE, 650)
        menu.text("Hard", 35, menu.WHITE, 700)
    elif menu.state == "Game":
        blocks.draw_grid()
        blocks.draw_bg()
        blocks.block_drop()
        blocks.block_draw()
        blocks.line_pop()

    pygame.display.flip()