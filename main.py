import pygame
import os
from random import randint as rando
import math

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)

from Player import PlayerClass
from Shot import ShotClass
from Enemy import EnemyClass
from Terrain import TerrainClass
from Net import NetClass


font = pygame.font.Font(os.path.join('assets', 'Roboto-Bold.ttf'), 32)
highScoreFont = pygame.font.Font(os.path.join('assets', 'Roboto-Bold.ttf'), 32)

controls = {"UP": pygame.K_UP, "DOWN": pygame.K_DOWN, "LEFT": pygame.K_LEFT, "RIGHT": pygame.K_RIGHT}
terrain=[]

number_of_enemies = 5
# Liste der skal indeholde AKTIVE enemy objekter:
enemies = []
enemyMaxSpeed = 5

shots=[]
nets=[]
highScore=0


musicPath = os.path.normpath(os.path.join('assets', 'music','VicePoint.mp3'))
pygame.mixer.music.load(musicPath) #https://soundcloud.com/synthwave80s/01-vice-point
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
gameWindowHeight = 1920
gameWindowWidth = 1080



try:
    with open('highScoreFile') as file:
        data = file.read()
        highScore=int(float(data.strip()))
        #highScore=math.inf
        print("Loaded highscore:",highScore)
except:
    print("highScoreFile not found, resetting to 0.")

#get resolution info from hardware:
gameWindowWidth, gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
#instead of a screen i use a surface, so that i can scale it down to different resolutions from max (1920x1080)
surface = pygame.Surface((gameWindowWidth, gameWindowHeight))

display = pygame.display.set_mode((gameWindowWidth, gameWindowHeight)) #go fullscreen to any resolution
#display = pygame.display.set_mode((800, 600)) #Windowed mode
playerObject = PlayerClass(surface, xpos=100, ypos=100, terrainCollection=terrain)



# COLLISION CHECKER tager imod to gameobjekter og returnrer true, hvis de rører hinanden:
def collisionChecker(firstGameObject, secondGameObject):
        if firstGameObject.x + firstGameObject.width > secondGameObject.x and\
                firstGameObject.x < secondGameObject.x + secondGameObject.width and\
                firstGameObject.y + firstGameObject.height > secondGameObject.y and\
                firstGameObject.y < secondGameObject.y + secondGameObject.height:
            return True
        return False


#Define a bunch of terrain objects in a function:
def createTerrain():
    terrain.append(TerrainClass(surface, 200, 200, 200, 20))
    terrain.append(TerrainClass(surface, 400, 200, 20, 200))
    terrain.append(TerrainClass(surface, 600, 400, 20, 200))

createTerrain() #Run the terrain generator function

def spawnEnemy():
    enemies.append(EnemyClass(surface,
                                        spawnPosX=rando(1, gameWindowWidth),
                                        spawnPosY=rando(1, gameWindowHeight),
                                        speedX=rando(-enemyMaxSpeed, enemyMaxSpeed),
                                        speedY=rando(-enemyMaxSpeed, enemyMaxSpeed))
 
                       )



for i in range(number_of_enemies):
    spawnEnemy()
    
    if collisionChecker(playerObject,enemies[-1]):
        enemies.pop()
        spawnEnemy()
if __name__==  '__main__':
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
                if event.key == controls["UP"]:
                    playerObject.ySpeed -= playerObject.maxSpeed
                if event.key == controls["DOWN"]:
                    playerObject.ySpeed += playerObject.maxSpeed
                if event.key == controls["LEFT"]:
                    playerObject.xSpeed -= playerObject.maxSpeed
                if event.key == controls["RIGHT"]:
                    playerObject.xSpeed += playerObject.maxSpeed
                    #Skud:                          .. Men kun når spilleren bevæger sig:
                if event.key == pygame.K_SPACE:
                    if playerObject.xSpeed !=0 or playerObject.ySpeed !=0:
                        shots.append(ShotClass(surface, spawnPosX=playerObject.x + playerObject.width / 2, spawnPosY=playerObject.y + playerObject.height / 2, playerSpeedX=playerObject.xSpeed, playerSpeedY=playerObject.ySpeed))
                    else:
                        if playerObject.makingNet==False:
                            playerObject.netStart = (playerObject.x,playerObject.y)
                            playerObject.makingNet=True
                        else: ##TODONE: Draw a line from netStart to playerXY
                            #nets.append((playerObject.netStart,(playerObject.x,playerObject.y)))
                            nets.append( NetClass( surface, playerObject.netStart[0],playerObject.netStart[1],playerObject.x,playerObject.y ) )
                            playerObject.makingNet=False
                            for net in nets:
                                print(net.x, net.y,net.width, net.height)

            #KEY RELEASES:
            if event.type == pygame.KEYUP:
                if event.key == controls["UP"]:
                    playerObject.ySpeed += playerObject.maxSpeed
                if event.key == controls["DOWN"]:
                    playerObject.ySpeed -= playerObject.maxSpeed
                if event.key == controls["LEFT"]:
                    playerObject.xSpeed += playerObject.maxSpeed
                if event.key == controls["RIGHT"]:
                    playerObject.xSpeed -= playerObject.maxSpeed
        #debug: print out unused pygame events
        #else:
        #        print(event)

        #UPDATE GAME OBJECTS:
        playerObject.update()
        for shot in shots:
            shot.update()
        for enemy in enemies:
            #TODO: Make enemy.update return True if still alive. This should declutter the game loop.
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
                    print('Points:',playerObject.points)
                    if playerObject.points > highScore:
                        highScore = playerObject.points
            if collisionChecker(enemy,playerObject): #TODO: ONLY HURT PLAYER ONCE PER COLLISION!
                playerObject.collisionSFX.play()
                print("OUCH!")
                playerObject.HP-=1
                playerObject.points=0
                print(playerObject.HP)
                enemyIsDead = True
            for net in nets:
                if collisionChecker(net,enemy):
                    enemyIsDead=True
                    playerObject.points += 1
                    net.hits+=1
                    if net.hits>2:
                        nets.remove(net)
            if enemyIsDead or not enemy.active:
                enemies.remove(enemy)

                spawnEnemy()
        #DRAW GAME OBJECTS:
        surface.fill((0, 0, 0)) #blank screen. (or maybe draw a background)
        for net in nets:
            # TODO: Check if net and enemies collide. Remove both
            ## TODO: Do we need to implement a whole goddamn class to handle collisions with lines?
            ### TODO: Oh look! This could be really pretty: https://www.reddit.com/r/gamedev/comments/4qmfkh/comment/d4ueojk/
            #### TODO: OOOOOOR.. what if the nets were just rectangles? ... yeah.. that's the easiest way.

           #pygame.draw.line(surface, color=(128, 128, 128), start_pos=net[0], end_pos=net[1])
            net.draw()

        playerObject.draw()
        for shot in shots:
            shot.draw()
        for enemy in enemies:
            enemy.draw()
        for tile in terrain:
            tile.draw()

        #Score:                                                 antialias?, color
        text = font.render('SCORE: ' + str(playerObject.points), True,(0, 255, 0))
        surface.blit(text, (0, 0))

        #text = highScoreFont.render('HIGHSCORE: THE HIGHEST POSSIBLE SCORE', True, (255, 0, 0))
        text = highScoreFont.render(f'HIGHSCORE: {highScore}', True, (255, 0, 0))
        #surface.blit(text, (gameWindowWidth/2-text.get_width()/2, gameWindowHeight/2))
        surface.blit(text, (0, 32))
        clock.tick(60)
        #push the scaled surface to the actual display:
        display.blit(pygame.transform.scale(surface, (gameWindowWidth, gameWindowHeight)), (0, 0))
        pygame.display.flip()
    #When done is false the while loop above exits, and this code is run:
    with open('highScoreFile', 'w') as file:
        print("Saving highscore to file:", highScore)
        file.write(str(highScore))






