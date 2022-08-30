from ctypes import alignment
import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject

class Record(DrawableObject):
    record = 1000

    def __init__(self, position: Vector2, size: Vector2, font: pygame.font.Font):
        super().__init__(position, size, color=(0, 0, 0))
        self._isNew = True
        self._font = font
        self._font_color = (255, 0, 0)

    def update(self, distance: float):
        if self._isNew == False and self.record < distance:
            self._isNew = True
            self._font_color = (255, 0, 0)
        
        if self._isNew:
            self.record = distance

        if self.record < 1000:
            self.image = self._font.render("REKORD: " + str(int(self.record)) + "m", False, self._font_color)
            return
        self.image = self._font.render("REKORD: %.2f km" % (self.record / 1000), False, self._font_color)

    def reset(self):
        self._isNew = False
        self._font_color = (0, 0, 0)