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
    ENEMY_ACCELERATION,
)

ENEMY_START_SIZE = Vector2(WINDOW_WIDTH, WINDOW_WIDTH * 0.9) * ENEMY_START_SIZE
ENEMY_MAX_SIZE = Vector2(WINDOW_WIDTH, WINDOW_WIDTH * 0.9) * ENEMY_MAX_SIZE
ENEMY_START_AREA = ENEMY_START_SIZE.x * ENEMY_START_SIZE.y
ENEMY_MAX_AREA = ENEMY_MAX_SIZE.x * ENEMY_MAX_SIZE.y

SECOND_LANE_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.35)
FIRST_LANE_START = Vector2(WINDOW_WIDTH * 0.3, WINDOW_HEIGHT * 0.35)
THIRD_LANE_START = Vector2(WINDOW_WIDTH * 0.7, WINDOW_HEIGHT * 0.35)
SECOND_LANE_VECTOR = Vector2(0, 1)
FIRST_LANE_VECTOR = Vector2(WINDOW_WIDTH * -0.2, WINDOW_HEIGHT * 0.65).normalize()
THIRD_LANE_VECTOR = Vector2(-FIRST_LANE_VECTOR.x, FIRST_LANE_VECTOR.y)


class Enemy(DrawableObject):
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
        self._log_conv = ENEMY_START_VELOCITY / math.log(
            (WINDOW_HEIGHT * 0.65) / (ENEMY_MAX_AREA - ENEMY_START_AREA) * 0.2
        )
        self.__velocity = direction * ENEMY_START_VELOCITY
        self.__size = Vector2(ENEMY_START_SIZE)
        self._area = ENEMY_START_AREA
        self.__center = Vector2(self.rect.center)

    def update(self):
        if self.__size == ENEMY_MAX_SIZE:
            self.__velocity = self.__velocity * ENEMY_ACCELERATION

        self.__center = self.__center + self.__velocity
        self.rect.center = self.__center
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

        self.__time += 1
        if self._area > ENEMY_MAX_AREA:
            self.__size = ENEMY_MAX_SIZE
        elif self._area < ENEMY_MAX_AREA:
            area_inc = math.log(self.__time) * self._log_conv
            self.__size.x = ENEMY_START_SIZE.x * math.sqrt(area_inc)
            self.__size.y = ENEMY_START_SIZE.y * math.sqrt(area_inc)

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
