import time
from random import randint, randrange
from os.path import exists

import pygame
from pygame import Vector2
from aicargame.game.objects.background import Background
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy
from aicargame.game.objects.gui.gui import GUI
from aicargame.game.objects.gui.speedo import Speedo
from aicargame.game.textures.textures import Textures

from aicargame.globals import (
    ENEMY_START_VELOCITY,
    SPEED_CHANGE_TIMER,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    ENEMY_INTERVAL,
)

from aicargame.events import (
    GAME_OVER
)

FIRST_LANE_START = Vector2(WINDOW_WIDTH * 0.3, WINDOW_HEIGHT * 0.35)
SECOND_LANE_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.35)
THIRD_LANE_START = Vector2(WINDOW_WIDTH * 0.7, WINDOW_HEIGHT * 0.35)

FIRST_LANE_VECTOR = Vector2(WINDOW_WIDTH * -0.2, WINDOW_HEIGHT * 0.65).normalize()
SECOND_LANE_VECTOR = Vector2(0, 1)
THIRD_LANE_VECTOR = Vector2(-FIRST_LANE_VECTOR.x, FIRST_LANE_VECTOR.y)

class Game:
    enemySprites = pygame.sprite.Group()
    gui: GUI
    window: pygame.Surface
    bg: Background
    next_enemy_spawn: int = ENEMY_INTERVAL[1] / 100

    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AICarGame")

        if not exists("saved/record.txt"):
            with open("saved/record.txt", "wt") as createFile:
                createFile.write("0")

        self._mousePos: tuple[int, int]
        self._mouseClicked: tuple[bool, bool, bool] | tuple[bool, bool, bool, bool, bool]

        self._isMainMenu = True
        self._isStarted = False
        self._isEnded = False

        self.bg = Background()
        self.gui = GUI()
        self.__player = Player()

    def startGame(self):
        self.bg.texture = Textures.BACKGROUND
        self.gui.startGame()
        Enemy.spawn_timer = time.time()
        Enemy.vel_change_timer = time.time()
        Speedo.timer = time.time()
        self.reset()

        self._isMainMenu = False
        self._isStarted = True
        self._isEnded = False

    def endGame(self):
        self.bg.texture = Textures.MENU_BACKGROUND
        self.gui.endGame()

        self._isStarted = False
        self._isEnded = True

    def spawnEnemy(self):
        rand = randint(0, 5)
        if rand == 0:
            self.enemySprites.add(Enemy(FIRST_LANE_START, FIRST_LANE_VECTOR))
        elif rand == 1:
            self.enemySprites.add(Enemy(SECOND_LANE_START, SECOND_LANE_VECTOR))
        elif rand == 2:
            self.enemySprites.add(Enemy(THIRD_LANE_START, THIRD_LANE_VECTOR))
        elif rand == 3:
            self.enemySprites.add(Enemy(FIRST_LANE_START, FIRST_LANE_VECTOR))
            self.enemySprites.add(Enemy(SECOND_LANE_START, SECOND_LANE_VECTOR))
        elif rand == 4:
            self.enemySprites.add(Enemy(FIRST_LANE_START, FIRST_LANE_VECTOR))
            self.enemySprites.add(Enemy(THIRD_LANE_START, THIRD_LANE_VECTOR))
        else:
            self.enemySprites.add(Enemy(SECOND_LANE_START, SECOND_LANE_VECTOR))
            self.enemySprites.add(Enemy(THIRD_LANE_START, THIRD_LANE_VECTOR))

    def reset(self):
        self.__player.reset()
        self.enemySprites.empty()
        Enemy.speed = WINDOW_HEIGHT * ENEMY_START_VELOCITY        
        self.gui.reset()

    def checkCollisions(self):
        if pygame.sprite.spritecollide(self.__player, self.enemySprites, False) != []:
            pygame.event.post(pygame.event.Event(GAME_OVER))

    def update(self):
        self.updateMouse()
        self.gui.update(self._mousePos, self._mouseClicked, self._isStarted)

        if self._isStarted:
            cur_time = time.time()

            if cur_time - Enemy.spawn_timer >= self.next_enemy_spawn:
                self.next_enemy_spawn = (
                    int(
                        randrange(
                            start=ENEMY_INTERVAL[0], stop=ENEMY_INTERVAL[1], step=1
                        )
                    )
                    / 100
                )
                self.spawnEnemy()
                Enemy.spawn_timer = cur_time

            if cur_time - Enemy.vel_change_timer >= SPEED_CHANGE_TIMER:
                Enemy.speed += 0.5
                Enemy.vel_change_timer = cur_time

            self.__player.update()
            self.enemySprites.update()
            self.checkCollisions()

    def updateMouse(self):
        self._mousePos = pygame.mouse.get_pos()
        self._mouseClicked = pygame.mouse.get_pressed()

    def render(self):
        self.bg.render()
        self.gui.render()

        if self._isStarted:
            self.__player.render()
            self.enemySprites.draw(self.window)

        pygame.display.update()
