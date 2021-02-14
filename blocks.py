import pygame
from window import Window

class Blocks(Window):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.block1 = []
        self.block2 = []
        self.block3 = []
        self.block4 = []
        self.block5 = []
        self.block6 = []
        self.block7 = []

    def block_init(self):
        for i in range(4):
            loc = [i*self.width/self.columns, self.height/self.rows]
            self.block1.append(loc)
        self.blocks.append(self.block1)

    def block_draw(self):
        for obj in self.blocks:
            for ch in obj:
                pygame.draw.rect(self.screen, self.BLUE, [ch[0], ch[1], self.size - 1, self.size - 1], width=0)

    def block_drop(self):
        for obj in self.blocks:
            for ch in obj:
                if ch[1] < self.height - self.size:
                    ch[1] += self.size