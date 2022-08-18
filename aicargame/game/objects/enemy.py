import time
from random import randint

import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.textures.textures import Textures
from aicargame.globals import (
    WINDOW_HEIGHT,
    ENEMY_START_SIZE,
    ENEMY_SPEED,
    FIRST_LANE_START,
    SECOND_LANE_START,
    THIRD_LANE_START,
    FIRST_LANE_VECTOR,
    SECOND_LANE_VECTOR,
    THIRD_LANE_VECTOR
)

class Enemy(DrawableObject):
    timer = time.time()

    def __init__(self, position: Vector2, size: Vector2):
        super().__init__(position, size, Textures.ENEMY)
        if(position == FIRST_LANE_START):
            self.__velocity = FIRST_LANE_VECTOR
        elif(position == SECOND_LANE_START):
            self.__velocity = SECOND_LANE_VECTOR
        else:
            self.__velocity = THIRD_LANE_VECTOR

        self.__velocity = self.__velocity * ENEMY_SPEED
    
    def update(self):
        self.rect.move_ip(self.__velocity)
        if(self.rect.bottom > WINDOW_HEIGHT):
            self.kill()

    @staticmethod
    def spawnEnemy():
        rand = randint(0, 2)
        if(rand == 0):
            newEnemy = Enemy(FIRST_LANE_START, ENEMY_START_SIZE)
        elif(rand == 1):
            newEnemy = Enemy(SECOND_LANE_START, ENEMY_START_SIZE)
        else:
            newEnemy = Enemy(THIRD_LANE_START, ENEMY_START_SIZE)

        return newEnemy
