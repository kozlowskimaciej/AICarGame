import pygame

from aicargame.game.objects.drawableobject import DrawableObject

from aicargame.globals import (
    BUTTON_SIZE,
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class Button(DrawableObject):
    def __init__(self, surf: pygame.Surface):
        super().__init__((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), BUTTON_SIZE, color=(0, 0, 0))
        self._surf = surf

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

    def render(self):
        self._surf.blit(self.image, self.rect.topleft)