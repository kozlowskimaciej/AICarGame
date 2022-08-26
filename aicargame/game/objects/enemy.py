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
    ENEMY_START_VELOCITY
)

ENEMY_START_SIZE = Vector2(WINDOW_WIDTH, WINDOW_WIDTH * 0.9) * ENEMY_START_SIZE
ENEMY_MAX_SIZE = Vector2(WINDOW_WIDTH, WINDOW_WIDTH * 0.9) * ENEMY_MAX_SIZE
ENEMY_START_VELOCITY = WINDOW_HEIGHT * ENEMY_START_VELOCITY

SECOND_LANE_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.35)
FIRST_LANE_START = Vector2(WINDOW_WIDTH * 0.3, WINDOW_HEIGHT * 0.35)
THIRD_LANE_START = Vector2(WINDOW_WIDTH * 0.7, WINDOW_HEIGHT * 0.35)
SECOND_LANE_VECTOR = Vector2(0, 1)
FIRST_LANE_VECTOR = Vector2(WINDOW_WIDTH * -0.2, WINDOW_HEIGHT * 0.65).normalize()
THIRD_LANE_VECTOR = Vector2(-FIRST_LANE_VECTOR.x, FIRST_LANE_VECTOR.y)


class Enemy(DrawableObject):
    spawn_timer = time.time()
    vel_change_timer = time.time()
    speed = ENEMY_START_VELOCITY

    def __init__(self, position: Vector2):
        super().__init__(position, (0, 0), texture=Textures.ENEMY)

        self._direction: Vector2
        if position == FIRST_LANE_START:
            self._direction = FIRST_LANE_VECTOR
        elif position == SECOND_LANE_START:
            self._direction = SECOND_LANE_VECTOR
        else:
            self._direction = THIRD_LANE_VECTOR

        self._time = 0
        self._max_time = (WINDOW_HEIGHT * 0.65) / ENEMY_START_VELOCITY
        self._size = Vector2(ENEMY_START_SIZE)
        self._log_conv = (ENEMY_MAX_SIZE.x - ENEMY_START_SIZE.x) / math.log(self._max_time * 0.2 + 1)
        self._center = Vector2(self.rect.center)
        self._velocity = self._direction * ENEMY_START_VELOCITY

    def resize(self):
        if self._size == ENEMY_MAX_SIZE:
            return
        if self._time >= self._max_time * 0.2:
            self._size = Vector2(ENEMY_MAX_SIZE)
            return
        log = math.log(self._time + 1)
        self._size.x = ENEMY_START_SIZE.x + log * self._log_conv
        self._size.y = self._size.x * 0.9

    def update(self):
        self._time += 1

        self._center = self._center + self._velocity
        self.rect.center = self._center
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()

        self.resize()

        if self._velocity != self._direction * Enemy.speed and self._time >= self._max_time * 0.2:
            self._velocity = self._direction * Enemy.speed
        if self.rect.bottom >= WINDOW_HEIGHT:
            self._velocity *= 2

        self.image = pygame.transform.scale(self.RAW_TEXTURE, self._size)

        self.rect = self.image.get_rect()
        self.rect.center = self._center

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
