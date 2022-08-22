import time
import math
from random import randint

import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.textures.textures import Textures
from aicargame.globals import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    ENEMY_MAX_SIZE,
    ENEMY_START_SIZE,
    ENEMY_START_VELOCITY,
    ENEMY_ACCELERATION
)

ENEMY_START_SIZE = Vector2(WINDOW_WIDTH, WINDOW_HEIGHT) * ENEMY_START_SIZE
ENEMY_MAX_SIZE = Vector2(WINDOW_WIDTH, WINDOW_HEIGHT) * ENEMY_MAX_SIZE

SECOND_LANE_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.25)
FIRST_LANE_START = Vector2(float(WINDOW_WIDTH * 0.44), float(WINDOW_HEIGHT * 0.25))
THIRD_LANE_START = Vector2(WINDOW_WIDTH * 0.56, WINDOW_HEIGHT * 0.25)
SECOND_LANE_VECTOR = Vector2(0, 1)
FIRST_LANE_VECTOR = Vector2(WINDOW_WIDTH * -0.36, WINDOW_HEIGHT * 0.75).normalize()
THIRD_LANE_VECTOR = Vector2(-FIRST_LANE_VECTOR.x, FIRST_LANE_VECTOR.y)


class Enemy(DrawableObject):
    start_velocity = ENEMY_START_VELOCITY
    spawn_timer = time.time()
    vel_change_timer = time.time()

    def __init__(self, position: Vector2):
        super().__init__(position, (0, 0), texture=Textures.ENEMY)

        if position == FIRST_LANE_START:
            direction = FIRST_LANE_VECTOR
        elif position == SECOND_LANE_START:
            direction = SECOND_LANE_VECTOR
        else:
            direction = THIRD_LANE_VECTOR

        self.__time = 1
        self.__velocity = direction * Enemy.start_velocity
        print(Enemy.start_velocity)
        print(self.__velocity)
        self.__size = Vector2(ENEMY_START_SIZE)
        self.__center = Vector2(self.rect.center)

    def update(self):
        if self.__size == ENEMY_MAX_SIZE:
            self.__velocity = self.__velocity * ENEMY_ACCELERATION

        self.__center = self.__center + self.__velocity
        self.rect.center = self.__center
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

        self.__time = self.__time + 1
        if self.__size.x > ENEMY_MAX_SIZE.x:
            self.__size = ENEMY_MAX_SIZE
        elif self.__size.x < ENEMY_MAX_SIZE.x:
            log = math.log(self.__time)
            self.__size.x = log * (ENEMY_MAX_SIZE.x / 5)
            self.__size.y = log * (ENEMY_MAX_SIZE.y / 5)

        self.image = pygame.transform.scale(self.RAW_TEXTURE, self.__size)

        self.rect = self.image.get_rect()
        self.rect.center = self.__center

    @staticmethod
    def spawnEnemy():
        rand = randint(0, 2)
        if rand == 0:
            newEnemy = Enemy(FIRST_LANE_START)
        elif rand == 1:
            newEnemy = Enemy(SECOND_LANE_START)
        else:
            newEnemy = Enemy(THIRD_LANE_START)

        return newEnemy
