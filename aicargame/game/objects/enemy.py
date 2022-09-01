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

class Enemy(DrawableObject):
    spawn_timer: float
    vel_change_timer: float
    speed = ENEMY_START_VELOCITY

    def __init__(self, position: Vector2, direction: Vector2):
        super().__init__(position, (0, 0), texture=Textures.ENEMY)

        self._direction = direction
        self._time = 0
        self._max_time = (WINDOW_HEIGHT * 0.65) / ENEMY_START_VELOCITY
        self._size = Vector2(ENEMY_START_SIZE)
        self._log_conv = (ENEMY_MAX_SIZE.x - ENEMY_START_SIZE.x) / math.log(self._max_time * 0.1 + 1)
        self._center = Vector2(self.rect.center)
        self._velocity = self._direction * ENEMY_START_VELOCITY

    def resize(self):
        if self._size == ENEMY_MAX_SIZE:
            return
        if self._time >= self._max_time * 0.1:
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

        if self._velocity != self._direction * Enemy.speed and self._time >= self._max_time * 0.1:
            self._velocity = self._direction * Enemy.speed
        if self.rect.bottom >= WINDOW_HEIGHT:
            self._velocity *= 3

        self.image = pygame.transform.scale(self.RAW_TEXTURE, self._size)

        self.rect = self.image.get_rect()
        self.rect.center = self._center
