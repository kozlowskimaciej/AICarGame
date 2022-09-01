import pygame
from aicargame.game.objects.drawableobject import DrawableObject
from aicargame.game.objects.button import Button

from aicargame.game.textures.textures import Textures

from aicargame.globals import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

from aicargame.events import (
    START_GAME
)

class MainMenu(DrawableObject):
    def __init__(self, surf: pygame.Surface):
        super().__init__((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), (WINDOW_WIDTH, WINDOW_HEIGHT), Textures.MENU_BACKGROUND)
        self._surf = surf
        self._playButton = Button(surf, (WINDOW_WIDTH / 2, 600), Textures.PLAY_BUTTON)
        self._exitButton = Button(surf, (WINDOW_WIDTH / 2, 700), Textures.EXIT_BUTTON)

    def update(self, mousePos, mouseClicked):
        if self._playButton.isClicked(mousePos, mouseClicked[0]):
            pygame.event.post(pygame.event.Event(START_GAME))
        if self._exitButton.isClicked(mousePos, mouseClicked[0]):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def render(self):
        self._surf.blit(self.image, self.rect.topleft)
        self._playButton.render()
        self._exitButton.render()