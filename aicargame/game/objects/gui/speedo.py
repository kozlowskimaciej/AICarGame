import pygame
import time
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.globals import (
    SPEED_CHANGE_TIMER
)

class Speedo(DrawableObject):
    timer = time.time()
    speed_change_timer = SPEED_CHANGE_TIMER
    speed: float = 100
    font: pygame.font.Font

    def __init__(self, position: Vector2, size: Vector2, font: pygame.font.Font):
        super().__init__(position, size, color=(0, 0, 0))
        self.font = font

    def update(self):
        cur_time = time.time()
        if cur_time - self.timer >= self.speed_change_timer:
            self.speed += 10
            self.timer = cur_time

        self.image = self.font.render(str(self.speed) + "km/h", False, (0, 0, 0))

    def reset(self):
        self.speed = 100
