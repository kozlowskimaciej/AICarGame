import pygame
from pygame import Vector2

from aicargame.objects.drawableobject import DrawableObject
from aicargame.textures.textures import Textures


class Player(DrawableObject):
    def __init__(self, position: Vector2, size: Vector2):
        super().__init__(position, size, Textures.PLAYER)
        print(str(Textures.PLAYER))
        self.__velocity = 10
        self.__x_border = 10
        self.__y_border = 10

    def update(self):
        keys = pygame.key.get_pressed()

        vec = Vector2(0, 0)

        if keys[pygame.K_LEFT]:
            vec.x -= self.__velocity

        if keys[pygame.K_RIGHT]:
            vec.x += self.__velocity

        if keys[pygame.K_UP]:
            vec.y -= self.__velocity

        if keys[pygame.K_DOWN]:
            vec.y += self.__velocity

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
