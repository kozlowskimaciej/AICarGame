from aicargame.game.objects.drawableobject import DrawableObject

from aicargame.game.textures.textures import Textures

from aicargame.globals import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH
)

class Background(DrawableObject):
    def __init__(self):
        super().__init__((WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2), (WINDOW_WIDTH, WINDOW_HEIGHT), Textures.BACKGROUND)