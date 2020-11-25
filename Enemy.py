import pygame
import os

class EnemyClass:

    width=16
    height=16
    color=(255 , 0, 128)

    sfxPath = os.path.normpath(os.path.join('assets', 'sfx', 'plingpling.wav'))
    effect = pygame.mixer.Sound(sfxPath)

    def __init__(self,screen, spawnPosX, spawnPosY, speedX, speedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = speedX
        self.ySpeed = speedY
        self.theScreen=screen

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def playSound(self):
        self.effect.play()