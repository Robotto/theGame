import pygame

class ShotClass:
    x=0
    y=0
    xSpeed=0
    ySpeed=0
    width=10
    height=10
    color=(255 , 255, 255)

    def __init__(self, spawnPosX, spawnPosY, playerSpeedX, playerSpeedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = playerSpeedX * 3
        self.ySpeed = playerSpeedY * 3

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))