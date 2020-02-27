import pygame

class EnemyClass:
    x=0
    y=0
    xSpeed=0
    ySpeed=0
    width=8
    height=8
    color=(255 , 0, 128)

    def __init__(self, spawnPosX, spawnPosY, speedX, speedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = speedX
        self.ySpeed = speedY

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))