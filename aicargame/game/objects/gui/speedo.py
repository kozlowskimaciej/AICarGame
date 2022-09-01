import pygame
import time
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.globals import SPEED_CHANGE_TIMER


class Speedo(DrawableObject):
    speed = 100
    timer: float
    speed_change_timer = SPEED_CHANGE_TIMER

    def __init__(self, position: Vector2, size: Vector2, font: pygame.font.Font):
        super().__init__(position, size, color=(0, 0, 0))
        self._font = font
        self.image = self._font.render(f"{self.speed} km/h", False, (0, 0, 0))

    def update(self):
        cur_time = time.time()
        if cur_time - self.timer >= self.speed_change_timer:
            self.speed += 5
            self.timer = cur_time

    def render(self):
        self.image = self._font.render(f"{self.speed} km/h", False, (0, 0, 0))
        super().render()

    def reset(self):
        self.speed = 100
