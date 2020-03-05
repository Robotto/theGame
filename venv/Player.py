import pygame

class PlayerClass:
    x=0
    y=0
    xSpeed=0
    ySpeed=0
    maxSpeed=5
    width=20
    height=20
    color=(0, 128, 255)
    points=0
    theScreen=0
    collisionSFX = pygame.mixer.Sound('aaw.wav')


    def __init__(self,screen,xpos,ypos):
        self.x=xpos
        self.y=ypos
        self.theScreen=screen
        self.screenWidth = self.theScreen.get_size()[0]
        self.screenHeight = self.theScreen.get_size()[1]

    def update(self):
        self.x+=self.xSpeed
        self.y+=self.ySpeed

        #safety to prevent overshoot:
        if self.x+self.width > self.screenWidth:
            self.x = self.screenWidth-self.width
        if self.y+self.height > self.screenHeight:
            self.y = self.screenHeight-self.height
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0

    def draw(self):
        pygame.draw.rect(self.theScreen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

