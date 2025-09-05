import pygame


class NetClass:
    color = (128, 128, 128)

    def __init__(self, screen, _x1, _y1, _x2, _y2):
        self.theScreen = screen
        self.x = _x1 if _x1<_x2 else _x2
        self.y = _y1 if _y1<_y2 else _y2

        self.width = abs(_x2 - _x1) if _x1!=_x2 else 1
        self.height = abs(_y2 - _y1) if _y1!=_y2 else 1

        self.hits=0




    def draw(self):
        self.color=(127+self.hits*64,128,128)
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
