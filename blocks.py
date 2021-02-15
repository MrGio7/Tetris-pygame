import pygame
import random
from pygame.constants import K_LEFT, K_RIGHT, K_UP
from window import Window

class Blocks(Window):
    def __init__(self):
        super().__init__()
        self.shape = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 5, 9]],
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]]
        ]
        self.matrix = [
            [0,1,2,3],
            [4,5,6,7],
            [8,9,10,11],
            [12,13,14,15],
        ]
        self.random_shape = random.randint(0, int(len(self.shape) - 1))
        self.random_figure = random.randint(0, int(len(self.shape[self.random_shape]) - 1))
        self.update = 0
        self.rotation = 0

    def block_rotation(self):
        self.rotation = self.rotation + 1 % len(self.blocks[0])

    def block_draw(self):
        for i in self.shape[self.random_shape][self.random_figure]:
            posx = 0
            posy = 0
            for row in self.matrix:
                if i in row:
                    posx = row.index(i)
                    posy = self.matrix.index(row)
            pygame.draw.rect(self.screen, self.BLUE, [self.size*posx + 1, self.size*posy + 1, self.size - 1, self.size - 1], width=0)

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