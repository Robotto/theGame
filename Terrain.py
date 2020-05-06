import pygame


class TerrainClass:
    color=(114 , 122, 116)

    def __init__(self,screen,_x,_y,_width,_height):
        self.theScreen=screen
        self.x=_x
        self.y=_y
        self.width=_width
        self.height=_height

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
