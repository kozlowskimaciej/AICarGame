import pygame
from pygame import Vector2

from aicargame.game.objects.drawableobject import DrawableObject

from aicargame.globals import (
    BUTTON_SIZE
)

class Button(DrawableObject):
    def __init__(self, position: Vector2, texture=None):
        super().__init__(position, BUTTON_SIZE, texture)
        self._isVisible = True

    def isClicked(self, mousePos: tuple[int, int], isLeftButtonClicked: bool):
        if (
            self._isVisible and
            mousePos[0] >= self.rect.left and
            mousePos[0] <= self.rect.right and
            mousePos[1] >= self.rect.top and
            mousePos[1] <= self.rect.bottom and
            isLeftButtonClicked
        ):
            return True
        return False
    
    def render(self):
        if self._isVisible:
            super().render()

    def show(self):
        self._isVisible = True

    def hide(self):
        self._isVisible = False
