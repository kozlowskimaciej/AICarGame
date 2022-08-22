import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject

pygame.font.init

class Mileage(DrawableObject):
    distance = 0
    font = pygame.font.SysFont("Arial", 24)

    def __init__(self, position: Vector2, size: Vector2):
        super().__init__(position, size, color=(0, 0, 0))

    def update(self):
        self.distance += 1
        self.image = self.font.render(str(self.distance) + "m", False, (0, 0, 0))
