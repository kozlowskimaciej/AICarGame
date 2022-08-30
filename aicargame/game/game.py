import time
from random import randint, randrange
from os.path import exists

import pygame
from pygame import Vector2

from aicargame.globals import (
    ENEMY_START_VELOCITY,
    SPEED_CHANGE_TIMER,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    ENEMY_INTERVAL,
)
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy
from aicargame.game.objects.gui.gui import GUI
from aicargame.game.textures.textures import Textures

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
    bg = pygame.transform.scale(Textures.BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))
    next_enemy_spawn: int = ENEMY_INTERVAL[1] / 100

    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AICarGame")

        if not exists("saved/record.txt"):
            createFile = open("saved/record.txt", "wt")
            createFile.write("0")
            createFile.close()

        self.gui = GUI(self.window)
        self.__player = Player()

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
            self.reset()

    def update(self):
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
        self.gui.update()
        self.checkCollisions()

    def render(self):
        self.window.blit(self.bg, (0, 0))
        self.window.blit(self.__player.image, self.__player.rect.topleft)
        self.enemySprites.draw(self.window)
        self.gui.render()
        pygame.display.update()
