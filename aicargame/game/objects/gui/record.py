from ctypes import alignment
import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject

class Record(DrawableObject):
    def __init__(self, position: Vector2, size: Vector2, font: pygame.font.Font):
        super().__init__(position, size, color=(0, 0, 0))

        loadRecord = open("saved/record.txt", "rt")
        self._record = float(loadRecord.readline())
        loadRecord.close()

        self._isNew = False
        self._font = font
        self._font_color = (0, 0, 0)

    def update(self, distance: float):
        if self._isNew == False and self._record < distance:
            self._isNew = True
            self._font_color = (255, 0, 0)
        
        if self._isNew:
            self._record = distance
            saveRecord = open("saved/record.txt", "wt")
            saveRecord.write(str(self._record))
            saveRecord.close()

        if self._record < 1000:
            self.image = self._font.render("REKORD: " + str(int(self._record)) + "m", False, self._font_color)
            return
        self.image = self._font.render("REKORD: %.2f km" % (self._record / 1000), False, self._font_color)

    def reset(self):
        self._isNew = False
        self._font_color = (0, 0, 0)