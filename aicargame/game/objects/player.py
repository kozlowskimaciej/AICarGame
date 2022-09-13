import pygame
from pygame import Vector2

from aicargame.game.objects.raycast import RayCast
from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.textures.textures import Textures
from aicargame.globals import (
    PLAYER_VELOCITY,
    PLAYER_SIZE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

PLAYER_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.9)
PLAYER_SIZE = Vector2(WINDOW_WIDTH, WINDOW_WIDTH * 0.9) * PLAYER_SIZE
PLAYER_VELOCITY = WINDOW_WIDTH * PLAYER_VELOCITY

class Player(DrawableObject):
    def __init__(self, enemySprites, position: Vector2 = PLAYER_START):
        super().__init__(position, PLAYER_SIZE, Textures.PLAYER)
        self.__velocity = PLAYER_VELOCITY
        self._enemySprites = enemySprites
        self._rayCasts: list[float, float, float, float, float]

    def update(self):
        self.updateRayCasts()

        keys = pygame.key.get_pressed()

        vec = Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            vec.x -= self.__velocity

        if keys[pygame.K_RIGHT]:
            vec.x += self.__velocity

        self.rect.move_ip(vec)

        self._keep_inside()

    def updateRayCasts(self):
        self._rayCasts = [
            RayCast(Vector2(self.rect.center), 270, -60, self._enemySprites).fire(),
            RayCast(Vector2(self.rect.center), 270, -30, self._enemySprites).fire(),
            RayCast(Vector2(self.rect.center), 270, 0, self._enemySprites).fire(),
            RayCast(Vector2(self.rect.center), 270, 30, self._enemySprites).fire(),
            RayCast(Vector2(self.rect.center), 270, 60, self._enemySprites).fire()
        ]
        print(self._rayCasts)

    def _keep_inside(self):
        if self.rect.left < WINDOW_WIDTH * 0.02:
            self.rect.left = WINDOW_WIDTH * 0.02

        if self.rect.right > WINDOW_WIDTH * 0.98:
            self.rect.right = WINDOW_WIDTH * 0.98

    def reset(self):
        self.rect.center = PLAYER_START
