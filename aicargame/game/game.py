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
    START_GAME,
    GAME_OVER
)

FIRST_LANE_START = Vector2(WINDOW_WIDTH * 0.3, WINDOW_HEIGHT * 0.35)
SECOND_LANE_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.35)
THIRD_LANE_START = Vector2(WINDOW_WIDTH * 0.7, WINDOW_HEIGHT * 0.35)

FIRST_LANE_VECTOR = Vector2(WINDOW_WIDTH * -0.2, WINDOW_HEIGHT * 0.65).normalize()
SECOND_LANE_VECTOR = Vector2(0, 1)
THIRD_LANE_VECTOR = Vector2(-FIRST_LANE_VECTOR.x, FIRST_LANE_VECTOR.y)

class Game:
    def __init__(self):
        self._window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self._isRunning = True
        pygame.display.set_caption("AICarGame")

        if not exists("saved/record.txt"):
            with open("saved/record.txt", "wt") as createFile:
                createFile.write("0")

        self._mousePos: tuple[int, int]
        self._mouseClicked: tuple[bool, bool, bool] | tuple[bool, bool, bool, bool, bool]

        self._isMainMenu = True
        self._isStarted = False
        self._isEnded = False

        self._bg = Background()
        self._gui = GUI()
        self._player = Player()
        self._enemySprites = pygame.sprite.Group()
        self._next_enemy_spawn = ENEMY_INTERVAL[1] / 100

    @property
    def isRunning(self):
        return self._isRunning
    @isRunning.setter
    def isRunning(self, value):
        self._isRunning = value

    def startGame(self):
        self._bg.texture = Textures.BACKGROUND
        self._gui.startGame()
        Enemy.spawn_timer = time.time()
        Enemy.vel_change_timer = time.time()
        Speedo.timer = time.time()
        self.reset()

        self._isMainMenu = False
        self._isStarted = True
        self._isEnded = False

    def endGame(self):
        self._bg.texture = Textures.MENU_BACKGROUND
        self._gui.endGame()

        self._isStarted = False
        self._isEnded = True

    def spawnEnemy(self):
        rand = randint(0, 5)
        if rand == 0:
            self._enemySprites.add(Enemy(FIRST_LANE_START, FIRST_LANE_VECTOR))
        elif rand == 1:
            self._enemySprites.add(Enemy(SECOND_LANE_START, SECOND_LANE_VECTOR))
        elif rand == 2:
            self._enemySprites.add(Enemy(THIRD_LANE_START, THIRD_LANE_VECTOR))
        elif rand == 3:
            self._enemySprites.add(Enemy(FIRST_LANE_START, FIRST_LANE_VECTOR))
            self._enemySprites.add(Enemy(SECOND_LANE_START, SECOND_LANE_VECTOR))
        elif rand == 4:
            self._enemySprites.add(Enemy(FIRST_LANE_START, FIRST_LANE_VECTOR))
            self._enemySprites.add(Enemy(THIRD_LANE_START, THIRD_LANE_VECTOR))
        else:
            self._enemySprites.add(Enemy(SECOND_LANE_START, SECOND_LANE_VECTOR))
            self._enemySprites.add(Enemy(THIRD_LANE_START, THIRD_LANE_VECTOR))

    def reset(self):
        self._player.reset()
        self._enemySprites.empty()
        Enemy.speed = WINDOW_HEIGHT * ENEMY_START_VELOCITY        
        self._gui.reset()

    def checkCollisions(self):
        if pygame.sprite.spritecollide(self._player, self._enemySprites, False) != []:
            pygame.event.post(pygame.event.Event(GAME_OVER))

    def update(self):
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False
            if event.type == START_GAME:
                self.startGame()
            if event.type == GAME_OVER:
                self.endGame()

        self.updateMouse()
        self._gui.update(self._mousePos, self._mouseClicked, self._isStarted)

        if self._isStarted:
            cur_time = time.time()

            if cur_time - Enemy.spawn_timer >= self._next_enemy_spawn:
                self._next_enemy_spawn = (
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

            self._player.update()
            self._enemySprites.update()
            self.checkCollisions()

    def updateMouse(self):
        self._mousePos = pygame.mouse.get_pos()
        self._mouseClicked = pygame.mouse.get_pressed()

    def render(self):
        self._bg.render()
        self._gui.render()

        if self._isStarted:
            self._player.render()
            self._enemySprites.draw(self._window)

        pygame.display.update()
