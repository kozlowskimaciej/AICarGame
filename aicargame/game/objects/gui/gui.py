import pygame

from aicargame.game.objects.gui.speedo import Speedo
from aicargame.game.objects.gui.mileage import Mileage
from aicargame.globals import (
    WINDOW_WIDTH
)

pygame.font.init()

class GUI:
    window: pygame.Surface
    font = pygame.font.SysFont("Arial", 24)
    speedo = Speedo((0, 0), (WINDOW_WIDTH, 25), font)
    mileage = Mileage((0, 25), (WINDOW_WIDTH, 25), font)

    def __init__(self, window: pygame.Surface):
        self.window = window

    def update(self):
        self.speedo.update()
        self.mileage.update(Speedo.speed)

    def render(self):
        self.window.blit(self.speedo.image, (5, 0))
        self.window.blit(self.mileage.image, (5, 25))

    def reset(self):
        self.speedo.reset()
        self.mileage.reset()