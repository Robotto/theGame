import pygame
import os
from Player import PlayerClass
#from Shot import ShotClass
from Enemy import EnemyClass
from Terrain import TerrainClass
from random import randint as rando


class Main():
    # terrain=[]
    # Liste der skal indeholde AKTIVE enemy objekter:
    enemies = []
    enemyMaxSpeed = 15

    # shots=[]

    # highScore=0

    def __init__(self,controls={"UP":pygame.K_UP, "DOWN":pygame.K_DOWN, "LEFT":pygame.K_LEFT, "RIGHT":pygame.K_RIGHT}):
        pygame.init()
        self.controls = controls
        # pygame.mixer.init(frequency=44100, size=-16, channels=6, buffer=2048)
        # font = pygame.font.Font(os.path.join('assets', 'Roboto-Bold.ttf'), 32)
        # highScoreFont = pygame.font.Font(os.path.join('assets', 'Roboto-Bold.ttf'), 64)

        # musicPath = os.path.normpath(os.path.join('assets', 'music','VicePoint.mp3'))
        # pygame.mixer.music.load(musicPath) #https://soundcloud.com/synthwave80s/01-vice-point
        # pygame.mixer.music.play(-1)

        self.clock = pygame.time.Clock()
        self.gameWindowHeight = 1920
        self.gameWindowWidth = 1080


        #try:
        #    with open('highScoreFile') as file:
        #        data = file.read()
        #        import math
        ##        highScore=int(float(data.strip()))
        #        self.highScore=math.inf
        #        print("Loaded highscore:",highScore)
        #except:
        #    print("highScoreFile not found, resetting to 0.")

        #get resolution info from hardware:
        self.gameWindowWidth, self.gameWindowHeight = pygame.display.Info().current_w, pygame.display.Info().current_h
        #instead of a screen i use a surface, so that i can scale it down to different resolutions from max (1920x1080)
        self.surface = pygame.Surface((self.gameWindowWidth, self.gameWindowHeight))
        self.display = pygame.display.set_mode((self.gameWindowWidth, self.gameWindowHeight)) #go fullscreen to any resolution

        #createTerrain()
        self.playerObject = PlayerClass(self.surface, xpos=100, ypos=100)#), terrainCollection=terrain)


        number_of_enemies = 12
        #TODO:Markus hey man husk at tjekke todos
        #TODO:Mark
        for i in range(number_of_enemies):
            self.spawnEnemy()

    # COLLISION CHECKER tager imod to gameobjekter og returnrer true, hvis de rører hinanden:
    # def collisionChecker(self, firstGameObject, secondGameObject):
    #        if firstGameObject.x + firstGameObject.width > secondGameObject.x and\
    #                firstGameObject.x < secondGameObject.x + secondGameObject.width and\
    #                firstGameObject.y + firstGameObject.height > secondGameObject.y and\
    #                firstGameObject.y < secondGameObject.y + secondGameObject.height:
    #            return True
    #        return False
    # def createTerrain(self):
    #    self.terrain.append(TerrainClass(surface, 200, 200, 200, 20))
    #    self.terrain.append(TerrainClass(surface, 400, 200, 20, 200))
    #    self.terrain.append(TerrainClass(surface, 600, 400, 20, 200))

    def spawnEnemy(self):
        self.enemies.append(EnemyClass(self.surface,
                                            spawnPosX=rando(0, self.gameWindowWidth),
                                            spawnPosY=rando(0, self.gameWindowHeight),
                                            speedX=rando(-self.enemyMaxSpeed, self.enemyMaxSpeed),
                                            speedY=rando(-self.enemyMaxSpeed, self.enemyMaxSpeed))
                            )

    #    if collisionChecker(playerObject,enemies[-1]):
    #        enemies.pop()
    #        spawnEnemy()
    def run(self):
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
                    if event.key == self.controls["UP"]:
                        self.playerObject.ySpeed -= self.playerObject.maxSpeed
                    if event.key == self.controls["DOWN"]:
                        self.playerObject.ySpeed += self.playerObject.maxSpeed
                    if event.key == self.controls["LEFT"]:
                        self.playerObject.xSpeed -= self.playerObject.maxSpeed
                    if event.key == self.controls["RIGHT"]:
                        self.playerObject.xSpeed += self.playerObject.maxSpeed
                        #Skud:                          .. Men kun når spilleren bevæger sig:
        #            if event.key == pygame.K_SPACE and (playerObject.xSpeed !=0 or playerObject.ySpeed !=0):
        #                shots.append(ShotClass(surface, spawnPosX=playerObject.x + playerObject.width / 2, spawnPosY=playerObject.y + playerObject.height / 2, playerSpeedX=playerObject.xSpeed, playerSpeedY=playerObject.ySpeed))
                #KEY RELEASES:
                if event.type == pygame.KEYUP:
                    if event.key == self.controls["UP"]:
                        self.playerObject.ySpeed += self.playerObject.maxSpeed
                    if event.key == self.controls["DOWN"]:
                        self.playerObject.ySpeed -= self.playerObject.maxSpeed
                    if event.key == self.controls["LEFT"]:
                        self.playerObject.xSpeed += self.playerObject.maxSpeed
                    if event.key == self.controls["RIGHT"]:
                        self.playerObject.xSpeed -= self.playerObject.maxSpeed
            #debug: print out unused pygame events
            #else:
            #        print(event)

            #UPDATE GAME OBJECTS:
            self.playerObject.update()
        #    for shot in shots:
        #        shot.update()
            for enemy in self.enemies:
                enemyIsDead = False #boolean to check if enemy is dead, and remove it at end of for loop
                enemy.update()
                if enemy.x>self.gameWindowWidth or enemy.y>self.gameWindowHeight or enemy.x<0 or enemy.y<0:
                    enemyIsDead=True
        #        for shot in shots:
        #            if collisionChecker(shot,enemy):
        #                enemyIsDead=True
        #                shots.remove(shot)
        #                playerObject.points +=1
        #                enemy.playSound()
        #                print('Points:',playerObject.points)
        #                if playerObject.points > highScore:
        #                    highScore = playerObject.points
        #        if collisionChecker(enemy,playerObject):
        #            playerObject.collisionSFX.play()
        #            print("OUCH!")

                    self.playerObject.points=0
                if enemyIsDead:
                    self.enemies.remove(enemy)
                    self.spawnEnemy()
            #DRAW GAME OBJECTS:
            self.surface.fill((0, 0, 0)) #blank screen. (or maybe draw a background)
            self.playerObject.draw()
        #    for shot in shots:
        #        shot.draw()
            for enemy in self.enemies:
                enemy.draw()
        #    for tile in terrain:
        #        tile.draw()

            #Score:                                                 antialias?, color
        #    text = font.render('SCORE: ' + str(playerObject.points), True,(0, 255, 0))
        #    surface.blit(text, (0, 0))

        #    text = highScoreFont.render('HIGHSCORE: THE HIGHEST POSSIBLE SCORE', True, (255, 0, 0))
        #    surface.blit(text, (gameWindowWidth/2-text.get_width()/2, gameWindowHeight/2))
            self.clock.tick(60)
            #push the scaled surface to the actual display:
            self.display.blit(pygame.transform.scale(self.surface, (self.gameWindowWidth, self.gameWindowHeight)), (0, 0))
            pygame.display.flip()
        #When done is false the while loop above exits, and this code is run:
        #with open('highScoreFile', 'w') as file:
        #    print("Saving highscore to file:", highScore)
        #    file.write(str(highScore))

theGame = Main( controls = {"UP":pygame.K_w, "DOWN":pygame.K_s, "LEFT":pygame.K_a, "RIGHT":pygame.K_d})
theGame.run()
