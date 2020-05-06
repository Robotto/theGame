import pygame

class ShotClass:

    width=5
    height=5
    color=(255 , 255, 255)
    theScreen=0
    effect = pygame.mixer.Sound('pew.wav')

    def __init__(self,screen, spawnPosX, spawnPosY, playerSpeedX, playerSpeedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = playerSpeedX * 3
        self.ySpeed = playerSpeedY * 3
        self.theScreen=screen
        self.effect.play()

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))