import pygame

from aicargame.game.objects.gui.speedo import Speedo
from aicargame.game.objects.gui.mileage import Mileage
from aicargame.game.objects.gui.record import Record
from aicargame.globals import (
    WINDOW_WIDTH
)

pygame.font.init()

class GUI:
    window: pygame.Surface
    font = pygame.font.SysFont("Arial", 24)

    speedo = Speedo((WINDOW_WIDTH * 0.25 + 5, 12.5), (WINDOW_WIDTH / 2, 25), font)

    mileage = Mileage((WINDOW_WIDTH * 0.25 + 5, 37.5), (WINDOW_WIDTH / 2, 25), font)

    record = Record((WINDOW_WIDTH * 0.75 + 5, 12.5), (WINDOW_WIDTH / 2, 25), font)

    def __init__(self, window: pygame.Surface):
        self.window = window

    def update(self):
        self.speedo.update()
        self.mileage.update(self.speedo.speed)
        self.record.update(self.mileage.distance)

    def render(self):
        self.window.blit(self.speedo.image, self.speedo.rect.topleft)
        self.window.blit(self.mileage.image, self.mileage.rect.topleft)
        self.window.blit(self.record.image, self.record.rect.topleft)


    def reset(self):
        self.speedo.reset()
        self.mileage.reset()
        self.record.reset()