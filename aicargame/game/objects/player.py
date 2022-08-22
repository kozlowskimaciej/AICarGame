import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.textures.textures import Textures
from aicargame.globals import (
    PLAYER_VELOCITY,
    PLAYER_SIZE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
)

PLAYER_START = Vector2(WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.9)
PLAYER_SIZE = Vector2(WINDOW_WIDTH, WINDOW_HEIGHT) * PLAYER_SIZE


class Player(DrawableObject):
    def __init__(self, position: Vector2 = PLAYER_START):
        super().__init__(position, PLAYER_SIZE, Textures.PLAYER)
        self.__velocity = PLAYER_VELOCITY
        self.__x_border = 10
        self.__y_border = 10

    def update(self):
        keys = pygame.key.get_pressed()

        vec = Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            vec.x -= self.__velocity

        if keys[pygame.K_RIGHT]:
            vec.x += self.__velocity

        self.rect.move_ip(vec)

        self._keep_inside()

    def _keep_inside(self):
        win_x, win_y = pygame.display.get_window_size()

        win_x_border = win_x / self.__x_border
        win_y_border = win_y / self.__y_border

        if self.rect.centerx < win_x_border:
            self.rect.centerx = win_x_border

        if self.rect.centerx > win_x - win_x_border:
            self.rect.centerx = win_x - win_x_border

        if self.rect.centery < win_y_border:
            self.rect.centery = win_y_border

        if self.rect.centery > win_y - win_y_border:
            self.rect.centery = win_y - win_y_border

    def reset(self):
        self.rect.center = PLAYER_START
