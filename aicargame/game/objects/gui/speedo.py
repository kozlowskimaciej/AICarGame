import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject

pygame.font.init()


class Speedo(DrawableObject):
    speedometer: pygame.Surface
    speed: float = 100
    font = pygame.font.SysFont("Arial", 24)

    def __init__(self, position: Vector2, size: Vector2):
        super().__init__(position, size, color=(0, 0, 0))

    def update(self):
        self.speed += 1
        self.image = self.font.render(str(self.speed), False, (0, 0, 0))
