import pygame

from aicargame.game.objects.gui.speedo import Speedo
from aicargame.game.objects.gui.mileage import Mileage
from aicargame.game.objects.gui.record import Record
from aicargame.game.objects.button import Button

from aicargame.game.textures.textures import Textures

from aicargame.globals import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT
)

from aicargame.events import (
    START_GAME
)

pygame.font.init()

class GUI:
    def __init__(self):
        font = pygame.font.SysFont("Arial", round(WINDOW_HEIGHT * 0.031))
        self._speedo = Speedo((WINDOW_WIDTH * 0.26, WINDOW_HEIGHT * 0.017), (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.033), font)
        self._mileage = Mileage((WINDOW_WIDTH * 0.26, WINDOW_HEIGHT * 0.05), (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.033), font)
        self._record = Record((WINDOW_WIDTH * 0.76, WINDOW_HEIGHT * 0.017), (WINDOW_WIDTH * 0.5, WINDOW_HEIGHT * 0.033), font)
        self._playButton = Button((WINDOW_WIDTH / 2, 600), Textures.PLAY_BUTTON)
        self._exitButton = Button((WINDOW_WIDTH / 2, 700), Textures.EXIT_BUTTON)

    def update(self, mousePos, mouseClicked, isStarted):
        if isStarted:
            self._speedo.update()
            self._mileage.update(self._speedo.speed)
            self._record.update(self._mileage.distance)

        if self._playButton.isClicked(mousePos, mouseClicked[0]):
            pygame.event.post(pygame.event.Event(START_GAME))
        if self._exitButton.isClicked(mousePos, mouseClicked[0]):
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def render(self):
        self._speedo.render()
        self._mileage.render()
        self._record.render()
        self._playButton.render()
        self._exitButton.render()

    def endGame(self):
        if self._playButton.texture != Textures.PLAYAGAIN_BUTTON:
            self._playButton.texture = Textures.PLAYAGAIN_BUTTON
        self._playButton.show()
        self._exitButton.show()

    def startGame(self):
        self._playButton.hide()
        self._exitButton.hide()

    def reset(self):
        self._speedo.reset()
        self._mileage.reset()
        self._record.reset()