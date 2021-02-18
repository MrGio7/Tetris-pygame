from menu import Menu
import pygame
from blocks import Blocks
from menu import Menu

pygame.init()

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
        Menu()
        menu.text("Menu", 160, menu.WHITE, 50)
        menu.text("START", 100, menu.GREEN, 350)
        menu.start("Game")
        menu.text("Choose Difficulty:", 50, menu.WHITE, 550)
        menu.text("Easy", 35, menu.WHITE, 600)
        menu.dif_choose("Easy")
        menu.text("Medium", 35, menu.WHITE, 650)
        menu.dif_choose("Medium")
        menu.text("Hard", 35, menu.WHITE, 700)
        menu.dif_choose("Hard")
    elif menu.state == "Game":
        menu.draw_grid()
        menu.draw_bg()
        menu.block_drop()
        menu.block_draw()
        menu.line_pop()
    elif menu.state == "GameOver":
        menu.text("Game Over", 100, menu.WHITE, 50)
        menu.text("Play Again", 90, menu.GREEN, 350)
        menu.start("Menu")
        menu.text(f"Your score: {menu.score}", 50, menu.WHITE, 550)


    pygame.display.flip()