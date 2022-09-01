import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject

from aicargame.globals import (
    BUTTON_SIZE
)

class Button(DrawableObject):
    def __init__(self, position: Vector2, texture=None):
        super().__init__(position, BUTTON_SIZE, texture)

    def isClicked(self, mousePos: tuple[int, int], isLeftButtonClicked: bool):
        if (
            mousePos[0] >= self.rect.left and
            mousePos[0] <= self.rect.right and
            mousePos[1] >= self.rect.top and
            mousePos[1] <= self.rect.bottom and
            isLeftButtonClicked
        ):
            return True
        return False