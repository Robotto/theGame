import pygame

class PlayerClass:
    x=0
    y=0
    xSpeed=0
    ySpeed=0
    maxSpeed=10
    width=20
    height=20
    color=(0, 128, 255)

    def __init__(self,xpos,ypos):
        self.x=xpos
        self.y=ypos

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

