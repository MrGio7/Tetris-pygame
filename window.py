import pygame

class Window:
    def __init__(self):
        self.width = 400
        self.heigth = 800
        self.rows = 20
        self.columns = 10
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        self.GREEN = (0, 255, 0)
        self.CYAN = (0, 255, 255)
        self.BLUE = (0, 0, 255)
        self.PINK = (255, 0, 255)
        self.BLACK = (0, 0, 0)
        self.GREY = (100, 100, 100)
        self.screen = pygame.display.set_mode((self.width, self.heigth))

    def draw_bg(self):
        self.screen.fill(self.BLACK)
        for i in range(self.rows):
           pygame.draw.line(self.screen, self.GREY, (0, i*self.heigth/self.rows), (self.width, i*self.heigth/self.rows), width=1)
        for i in range(self.columns):
            pygame.draw.line(self.screen, self.GREY, (i*self.heigth/self.rows, 0), (i*self.heigth/self.rows, self.heigth), width=1)