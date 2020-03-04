import pygame


class EnemyClass:
    x=0
    y=0
    xSpeed=0
    ySpeed=0
    width=16
    height=16
    color=(255 , 0, 128)
    theScreen=0
    pygame.mixer.init(44100, -16, 2, 2048)
    effect = pygame.mixer.Sound('plingpling.wav')

    def __init__(self,screen, spawnPosX, spawnPosY, speedX, speedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = speedX
        self.ySpeed = speedY
        self.theScreen=screen

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed

    def hasCollision(self,shot):
        if shot.x + shot.width > self.x and shot.x < self.x + self.width and shot.y + shot.height > self.y and shot.y < self.y + self.height:
            return True

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def playSound(self):
        self.effect.play()