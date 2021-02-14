import pygame
from pygame.constants import K_LEFT, K_RIGHT, K_UP
from window import Window

class Blocks(Window):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.block_I = []
        self.block_I_1 = []
        self.block2 = []
        self.block3 = []
        self.block4 = []
        self.block5 = []
        self.block6 = []
        self.block7 = []
        self.update = 0

    def block_init(self):
        for i in range(4):
            I = [i*self.width/self.columns, self.height/self.rows]
            self.block_I.append(I)
            I_1 = [self.width/self.columns, i*self.height/self.rows]
            self.block_I_1.append(I_1)
        self.blocks.append(self.block_I)

    def block_draw(self):
        for obj in self.blocks:
            for ch in obj:
                pygame.draw.rect(self.screen, self.BLUE, [ch[0], ch[1], self.size - 1, self.size - 1], width=0)

    def block_drop(self):
        key = pygame.key.get_pressed()
        
        self.update += 1
        if self.update > 10:
            if key[K_LEFT]:
                for obj in self.blocks:
                    for ch in obj:
                        ch[0] -= self.size
                        
            if key[K_RIGHT]:
                for obj in self.blocks:
                    for ch in obj:
                        ch[0] += self.size
            
            if key[K_UP]:
                pass


            for obj in self.blocks:
                for ch in obj:
                    if ch[1] < self.height - self.size:
                        ch[1] += self.size
            self.update = 0