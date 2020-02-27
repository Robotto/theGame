import pygame
from Player import PlayerClass
from Shot import ShotClass

clock = pygame.time.Clock()

playerObject = PlayerClass(100, 100)

terrain=[]
enemies=[]
shots=[]


pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

        #-------PLAYER CONTROLS---------

        #KEY PRESSES:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerObject.ySpeed -= playerObject.maxSpeed
            if event.key == pygame.K_DOWN:
                playerObject.ySpeed += playerObject.maxSpeed
            if event.key == pygame.K_LEFT:
                playerObject.xSpeed -= playerObject.maxSpeed
            if event.key == pygame.K_RIGHT:
                playerObject.xSpeed += playerObject.maxSpeed
            if event.key == pygame.K_SPACE and (playerObject.xSpeed!=0 or playerObject.ySpeed!=0):
                shots.append(ShotClass(playerObject.x+playerObject.width/2, playerObject.y+playerObject.height/2, playerObject.xSpeed, playerObject.ySpeed))
        #KEY RELEASES:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                playerObject.ySpeed += playerObject.maxSpeed
            if event.key == pygame.K_DOWN:
                playerObject.ySpeed -= playerObject.maxSpeed
            if event.key == pygame.K_LEFT:
                playerObject.xSpeed += playerObject.maxSpeed
            if event.key == pygame.K_RIGHT:
                playerObject.xSpeed -= playerObject.maxSpeed
    #debug: print out unused pygame events
    #else:
    #        print(event)

    #UPDATE GAME OBJECTS:
    playerObject.update()
    for shot in shots:
        shot.update()

    #DRAW GAME OBJECTS:
    screen.fill((0, 0, 0)) #blank screen. (or maybe draw a background)
    playerObject.draw(screen)

    for shot in shots:
        shot.draw(screen)

    #do pygame housekeeping:
    pygame.display.flip()
    clock.tick(60)


