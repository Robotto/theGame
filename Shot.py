import pygame
import os

class ShotClass:

    width=5
    height=5
    color=(255 , 255, 255)

    sfxPath = os.path.normpath(os.path.join('assets', 'sfx', 'pew.wav'))
    effect = pygame.mixer.Sound(sfxPath)

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