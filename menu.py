import pygame
from window import Window

class Menu(Window):
    def __init__(self):
        super().__init__()
        self.pos = 0
        self.txt_size = 0

    def text(self, text, size, color, posy):
        font = pygame.font.SysFont(None, size)
        render = font.render(text, True, color, None)
        self.txt_size = font.size(text)
        self.pos = ((self.width - self.txt_size[0])/2, posy)
        
        self.screen.blit(render, self.pos)

    def click(self, state):
        cl = pygame.mouse.get_pressed(num_buttons=3)
        pos = pygame.mouse.get_pos()

        if cl == (1, 0, 0) and pos[0] > self.pos[0] and pos[0] < (self.pos[0] + self.txt_size[0]) and pos[1] > self.pos[1] and pos[1] < (self.pos[1] + self.txt_size[1]):
            self.state = state