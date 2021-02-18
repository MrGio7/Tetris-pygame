import pygame
from blocks import Blocks

class Gameover(Blocks):
    def __init__(self):
        super().__init__()

    def play_again(self, state):
        self.start(state)