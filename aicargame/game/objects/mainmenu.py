import pygame
from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.objects.button import Button

from aicargame.game.textures.textures import Textures

from aicargame.globals import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class MainMenu(DrawableObject):
    def __init__(self, game, surf: pygame.Surface):
        super().__init__((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), (WINDOW_WIDTH, WINDOW_HEIGHT), Textures.MENU_BACKGROUND)
        self._game = game
        self._surf = surf
        self._startButton = Button(surf)

    def update(self):
        mousePos = pygame.mouse.get_pos()
        mouseState = pygame.mouse.get_pressed()
        if self._startButton.isClicked(mousePos, mouseState[0]):
            self._game.setMainGame()

    def render(self):
        self._surf.blit(self.image, self.rect.topleft)
        self._startButton.render()