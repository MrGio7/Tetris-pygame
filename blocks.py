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
        self.block = []
        self.valid_space = []
        self.update = 0
        self.response = 0
        self.rotation = 0

    def block_rotation(self):
        self.rotation = self.rotation % len(self.shape[self.random_shape])

    def block_init(self):
        for i in self.shape[self.random_shape][self.rotation]:
                    for row in self.matrix:
                        if i in row:
                            posx = self.size*row.index(i)
                            posy = self.size*self.matrix.index(row)
                            self.block.append([posx, posy])

    def valid_sp(self):
        pass

    def block_draw(self):
        for i in self.shape[self.random_shape][self.rotation]:
                    for row in self.matrix:
                        if i in row:
                            posx = self.size*row.index(i)
                            posy = self.size*self.matrix.index(row)
                            self.block.append([posx, posy])
        for cor in self.block:
            pygame.draw.rect(self.screen, self.BLUE, [cor[0], cor[1], self.size - 1, self.size - 1], width=0)

    def block_drop(self):
        key = pygame.key.get_pressed()

        self.response += 1
        if key[K_LEFT]:
            if self.response > 5 and self.posx > 0:
                self.posx -= self.size
                    
        if key[K_RIGHT]:
            if self.response > 5 and self.posx < self.width - self.size:
                self.posx += self.size
        
        if key[K_UP]:
            if self.response > 5:
                self.rotation += 1
                self.block_rotation()

        if self.response > 5:
            self.response = 0

        self.update += 1

        contains = False
        for cor in self.block:
            if ([cor[0], cor[1] + self.size]) in self.bg:
                contains = True

        if contains:
            for cor in self.block:
                self.bg.append(cor)
            self.block = []
            self.random_shape = random.randint(0, int(len(self.shape) - 1))
            self.random_figure = random.randint(0, int(len(self.shape[self.random_shape]) - 1))
            self.block_init()
            contains = False

        if self.update > 10:  
            for cor in self.block:
                cor[1] += self.size
                self.update = 0