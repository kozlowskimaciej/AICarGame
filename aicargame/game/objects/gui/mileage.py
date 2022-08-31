import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject


class Mileage(DrawableObject):
    distance = 0
    font: pygame.font.Font

    def __init__(self, position: Vector2, size: Vector2, font: pygame.font.Font):
        super().__init__(position, size, color=(0, 0, 0))
        self.font = font

    def update(self, speed: float):
        self.distance += speed * 0.005

        if self.distance < 1000:
            self.image = self.font.render(f"{int(self.distance)} m", False, (0, 0, 0))
            return
        self.image = self.font.render(
            f"{round(self.distance/ 1000,2)} km", False, (0, 0, 0)
        )

    def reset(self):
        self.distance = 0
