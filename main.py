import pygame

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
font = pygame.font.Font('freesansbold.ttf', 32)

pygame.mixer.music.load('VicePoint.mp3') #https://soundcloud.com/synthwave80s/01-vice-point
pygame.mixer.music.play(-1)

from Player import PlayerClass
from Shot import ShotClass
from Enemy import EnemyClass
from Terrain import TerrainClass

from random import randint as rando
clock = pygame.time.Clock()

gameWindowHeight=800
gameWindowWidth=600

terrain=[]
enemies=[]
shots=[]

highScore=0
try:
    with open('highScoreFile') as file:
        data = file.read()
        highScore=int(data.strip())
        print("Loaded highscore:",highScore)
except:
    print("highScoreFile not found, resetting to 0.")

screen = pygame.display.set_mode((gameWindowWidth, gameWindowHeight))


def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and firstGameObject.x < secondGameObject.x + secondGameObject.width and firstGameObject.y + firstGameObject.height > secondGameObject.y and firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True

def spawnEnemy():
    enemies.append(EnemyClass(screen,spawnPosX=rando(0,gameWindowWidth),spawnPosY=rando(0,gameWindowHeight),speedX=rando(-1,1),speedY=rando(-1,1)))


for i in range(16):
    spawnEnemy()

def createTerrain():
    terrain.append(TerrainClass(screen, 200, 200,200,20))
    terrain.append(TerrainClass(screen, 400, 200,20,200))

createTerrain()


playerObject = PlayerClass(screen,xpos=100, ypos=100,terrainCollection=terrain)


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
                #Skud:                          .. Men kun når spilleren bevæger sig:
            if event.key == pygame.K_SPACE: #and (playerObject.xSpeed !=0 or playerObject.ySpeed !=0):
                shots.append(ShotClass(screen,spawnPosX=playerObject.x+playerObject.width/2, spawnPosY=playerObject.y+playerObject.height/2, playerSpeedX=playerObject.xSpeed, playerSpeedY=playerObject.ySpeed))
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

    for enemy in enemies:
        enemyIsDead = False #boolean to check if enemy is dead, and remove it at end of for loop
        enemy.update()

        if enemy.x>gameWindowWidth or enemy.y>gameWindowHeight or enemy.x<0 or enemy.y<0:
            enemyIsDead=True

        for shot in shots:
            if collisionChecker(shot,enemy):
                enemyIsDead=True
                shots.remove(shot)
                playerObject.points +=1
                enemy.playSound()
                #print('Points:',playerObject.points)
                if playerObject.points > highScore:
                    highScore = playerObject.points
        if collisionChecker(enemy,playerObject):
            playerObject.collisionSFX.play()
            print("OUCH!")

            playerObject.points=0

        if enemyIsDead:
            enemies.remove(enemy)
            spawnEnemy()

    #DRAW GAME OBJECTS:
    screen.fill((0, 0, 0)) #blank screen. (or maybe draw a background)
    playerObject.draw()

    #Score:                                                 antialias?, color
    text = font.render('SCORE: ' + str(playerObject.points), True,(0, 255, 0))
    screen.blit(text,(0,0))

    text = font.render('HIGHSCORE: ' + str(highScore), True, (255, 0, 0))
    screen.blit(text, (300,0))

    for shot in shots:
        shot.draw()

    for enemy in enemies:
        enemy.draw()

    for tile in terrain:
        tile.draw()

    pygame.display.flip()
    clock.tick(60)


#When done is false the while loop above exits, and this code is run:
with open('highScoreFile', 'w') as file:
    print("Saving highscore to file:", highScore)
    file.write(str(highScore))
