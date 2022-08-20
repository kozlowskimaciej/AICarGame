import time
import math
from random import randint

import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.textures.textures import Textures
from aicargame.globals import (
    ENEMY_MAX_SIZE,
    WINDOW_HEIGHT,
    ENEMY_START_SIZE,
    ENEMY_SPEED,
    FIRST_LANE_START,
    SECOND_LANE_START,
    THIRD_LANE_START,
    FIRST_LANE_VECTOR,
    SECOND_LANE_VECTOR,
    THIRD_LANE_VECTOR,
    WINDOW_WIDTH,
)


class Enemy(DrawableObject):
    timer = time.time()

    def __init__(self, position: Vector2):
        super().__init__(position, (0, 0), texture=Textures.ENEMY)

        if position == FIRST_LANE_START:
            self.__velocity = FIRST_LANE_VECTOR
        elif position == SECOND_LANE_START:
            self.__velocity = SECOND_LANE_VECTOR
        else:
            self.__velocity = THIRD_LANE_VECTOR

        self.__time = 1
        self.__velocity = self.__velocity * ENEMY_SPEED
        self.__size = Vector2(ENEMY_START_SIZE)
        self.__center = Vector2(self.rect.center)

    def update(self):
        if self.__size == ENEMY_MAX_SIZE:
            self.__velocity = self.__velocity * 1.2

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
