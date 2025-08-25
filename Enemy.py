import pygame
import os

class EnemyClass:

    width=32
    height=32
    color=(255 , 0, 128)

    sfxPath = os.path.normpath(os.path.join('assets', 'sfx', 'plingpling.wav'))
    effect = pygame.mixer.Sound(sfxPath)

    def __init__(self, screen, spawnPosX, spawnPosY, speedX, speedY):
        self.x = spawnPosX
        self.y = spawnPosY
        self.xSpeed = speedX
        self.ySpeed = speedY
        self.theScreen=screen
        self.active=True



    def update(self):
        if self.active:
            self.x+=self.xSpeed
            self.y += abs(self.ySpeed)
            if self.y+self.height>=self.theScreen.get_height():
                self.active=False
            if self.x+self.width>=self.theScreen.get_width():
                self.active=False


    def draw(self):
        if self.active:
            pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def playSound(self):
        self.effect.play()