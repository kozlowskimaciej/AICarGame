import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject

class Speedo(DrawableObject):
    speedometer: pygame.Surface
    speed: float = 100
    font: pygame.font.Font

    def __init__(self, position: Vector2, size: Vector2, font: pygame.font.Font):
        super().__init__(position, size, color=(0, 0, 0))
        self.font = font

    def update(self):
        self.speed += 1
        self.image = self.font.render(str(self.speed) + "km/h", False, (0, 0, 0))

    def reset(self):
        self.speed = 100
