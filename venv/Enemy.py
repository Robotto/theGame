import pygame


class EnemyClass:
    x=0
    y=0
    xSpeed=0
    ySpeed=0
    width=16
    height=16
    color=(255 , 0, 128)

    def __init__(self, spawnPosX, spawnPosY, speedX, speedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = speedX
        self.ySpeed = speedY

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed

    def hasCollision(self,shot):
        if shot.x + shot.width > self.x and shot.x < self.x + self.width and shot.y + shot.height > self.y and shot.y < self.y + self.height:
            return True

    def draw(self,screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))