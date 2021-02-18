import pygame
import random
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from menu import Menu

class Blocks(Menu):
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
        self.posx = 0
        self.posy = 0
        self.block = []
        self.update = 0
        self.response = 0
        self.rotation = 0
        self.border = False

    def block_rotation(self):
        self.rotation = self.rotation % (len(self.shape[self.random_shape]))

    def block_draw(self):
        for i in self.shape[self.random_shape][self.rotation]:
            for row in self.matrix:
                if i in row:
                    posx = self.size*row.index(i)
                    posy = self.size*self.matrix.index(row)
                    self.block.append([posx + self.posx, posy + self.posy])
                    if len(self.block) > 4:
                        self.block.pop(0)
        for cor in self.block:
            pygame.draw.rect(self.screen, self.BLUE, [cor[0], cor[1], self.size - 1, self.size - 1], width=0)

    def block_drop(self):
        key = pygame.key.get_pressed()
        
        if key[K_LEFT]:
            self.response += 1
            count = 0
            for cor in self.block:
                if cor[0] < self.size or ([cor[0] - self.size, cor[1]]) in self.bg or ([cor[0] - self.size, cor[1] + self.size]) in self.bg:
                    count += 1
            if count == 0 and self.response > 5:
                self.posx -= self.size
                self.response = 0

        if key[K_RIGHT]:
            self.response += 1
            count = 0
            for cor in self.block:
                if cor[0] >= (self.width - self.size) or ([cor[0] + self.size, cor[1]]) in self.bg or ([cor[0] + self.size, cor[1] + self.size]) in self.bg:
                    count += 1
            if count == 0 and self.response > 5:
                self.posx += self.size
                self.response = 0

        if key[K_UP]:
            self.response += 1
            count = 0
            for cor in self.block:
                if cor[0] == 0:
                    count += 1
                elif cor[0] == (self.width - self.size):
                    count -= 1
            if self.response > 5 and count > 2:
                self.posx += self.size
                self.rotation += 1
                self.block_rotation()
            elif self.response > 5 and count == -2:
                self.posx -= self.size
                self.rotation += 1
                self.block_rotation()
            elif self.response > 5 and count < -2:
                self.posx -= self.size*2
                self.rotation += 1
                self.block_rotation()
            elif self.response > 5 and (count == 0 or count == 1 or count == 2 or count == -1 or count == -2):
                self.rotation += 1
                self.block_rotation()

        if key[K_DOWN]:
            self.response += 1
            if self.response > 5:
                self.posy += self.size
                self.response = 0
                
        if self.response > 5:
            self.response = 0

        self.update += 1
        for cor in self.block:
            if ([cor[0], cor[1] + self.size]) in self.bg or cor[1] >= (self.height - self.size):
                self.border = True

        if self.border:
            for cor in self.block:
                self.bg.append(cor)
            self.block = []
            self.random_shape = random.randint(0, int(len(self.shape) - 1))
            self.random_figure = random.randint(0, int(len(self.shape[self.random_shape]) - 1))
            self.posy = 0
            self.posx = 0
            self.block_rotation()
            self.border = False

        if self.update > self.fps:  
            self.posy += self.size
            self.update = 0

    def line_pop(self):
        for i in range(self.rows):
            y = 0
            for cor in self.bg:
                if i*self.size == cor[1]:
                    y += 1
                if y == 10:
                    cpy = self.bg.copy()
                    self.bg.clear()
                    for coor in cpy:
                        if cor[1] != coor[1]:
                            if coor[1] < cor[1]:
                                self.bg.append([coor[0], (coor[1] + self.size)])
                            if coor[1] > cor[1]:
                                self.bg.append(coor)
