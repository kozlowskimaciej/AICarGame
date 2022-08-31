from ctypes import alignment
import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject


class Record(DrawableObject):
    def __init__(self, position: Vector2, size: Vector2, font: pygame.font.Font):
        super().__init__(position, size, color=(0, 0, 0))

        with open("saved/record.txt", "rt") as loadRecord:
            self._record = float(loadRecord.readline())

        self._isNew = False
        self._font = font
        self._font_color = (0, 0, 0)

    def update(self, distance: float):
        if self._isNew == False and self._record < distance:
            self._isNew = True
            self._font_color = (255, 0, 0)

        if self._isNew:
            self._record = distance
            with open("saved/record.txt", "wt") as saveRecord:
                saveRecord.write(str(self._record))

        if self._record < 1000:
            self.image = self._font.render(
                f"REKORD: {int(self._record)} m", False, self._font_color
            )
            return
        self.image = self._font.render(
            f"REKORD: {round(self._record / 1000, 2)} km", False, self._font_color
        )

    def reset(self):
        self._isNew = False
        self._font_color = (0, 0, 0)
