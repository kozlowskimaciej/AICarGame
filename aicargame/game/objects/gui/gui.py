import pygame

from aicargame.game.objects.gui.speedo import Speedo
from aicargame.game.objects.gui.mileage import Mileage
from aicargame.game.objects.gui.record import Record
from aicargame.globals import (
    WINDOW_WIDTH
)

pygame.font.init()

class GUI:
    def __init__(self, window: pygame.Surface):
        self._window = window
        
        font = pygame.font.SysFont("Arial", 24)
        self._speedo = Speedo((WINDOW_WIDTH * 0.25 + 5, 12.5), (WINDOW_WIDTH / 2, 25), font)
        self._mileage = Mileage((WINDOW_WIDTH * 0.25 + 5, 37.5), (WINDOW_WIDTH / 2, 25), font)
        self._record = Record((WINDOW_WIDTH * 0.75 + 5, 12.5), (WINDOW_WIDTH / 2, 25), font)

    def update(self):
        self._speedo.update()
        self._mileage.update(self._speedo.speed)
        self._record.update(self._mileage.distance)

    def render(self):
        self._window.blit(self._speedo.image, self._speedo.rect.topleft)
        self._window.blit(self._mileage.image, self._mileage.rect.topleft)
        self._window.blit(self._record.image, self._record.rect.topleft)


    def reset(self):
        self._speedo.reset()
        self._mileage.reset()
        self._record.reset()