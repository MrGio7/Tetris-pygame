import pygame

class Window(object):
    def __init__(self):
        self.width = 400
        self.height = 800
        self.rows = 20
        self.columns = 10
        self.size = 40
        self.bg = []
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.CYAN = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PINK = (255, 0, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (100, 100, 100)
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.state = "Menu"

    def draw_bg(self):
        if len(self.bg) > 0:
            for cor in self.bg:
                pygame.draw.rect(self.screen, self.RED, [cor[0], cor[1], self.size - 1, self.size - 1], width=0)

    def draw_grid(self):
        self.screen.fill(self.BLACK)
        for i in range(self.rows):
           pygame.draw.line(self.screen, self.GREY, (0, i*self.height/self.rows), (self.width, i*self.height/self.rows), width=1)
        for i in range(self.columns):
            pygame.draw.line(self.screen, self.GREY, (i*self.height/self.rows, 0), (i*self.height/self.rows, self.height), width=1)
    