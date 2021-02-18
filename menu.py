import pygame
from blocks import Blocks

class Menu(Blocks):
    def __init__(self):
        super().__init__()
        self.txt = ""
        self.color = self.WHITE
        self.pos = 0
        self.txt_size = 0
        self.difficulty = "Easy"
        self.score = 0

    def text(self, text, size, color, posy):
        self.txt = text
        self.color = color
        if self.txt == self.difficulty:
            self.color = self.RED
        font = pygame.font.SysFont(None, size)
        render = font.render(self.txt, True, self.color, None)
        self.txt_size = font.size(self.txt)
        self.pos = ((self.width - self.txt_size[0])/2, posy)
        
        self.screen.blit(render, self.pos)

    def start(self, state):
        self.bg = []
        self.posx = 0
        self.posy = 0
        self.block = []
        self.update = 0
        self.response = 0
        self.rotation = 0
        self.border = False
        cl = pygame.mouse.get_pressed(num_buttons=3)
        pos = pygame.mouse.get_pos()

        if cl == (1, 0, 0) and pos[0] > self.pos[0] and pos[0] < (self.pos[0] + self.txt_size[0]) and pos[1] > self.pos[1] and pos[1] < (self.pos[1] + self.txt_size[1]):
                self.state = state

    def dif_choose(self, state):
        cl = pygame.mouse.get_pressed(num_buttons=3)
        pos = pygame.mouse.get_pos()

        if cl == (1, 0, 0) and pos[0] > self.pos[0] and pos[0] < (self.pos[0] + self.txt_size[0]) and pos[1] > self.pos[1] and pos[1] < (self.pos[1] + self.txt_size[1]):
                self.difficulty = state
                if state == "Easy":
                    self.fps = 20
                elif state == "Medium":
                    self.fps = 15
                elif state == "Hard":
                    self.fps = 10

