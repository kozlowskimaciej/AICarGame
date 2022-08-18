from enum import Enum, auto
from pathlib import Path

PREFIX = Path("aicargame/game/textures/media/").resolve()


class Textures(Enum):
    BACKGROUND = "bg.png"
    PLAYER = "player.gif"
    ENEMY = "nuclear-bomb.png"

    def __str__(self) -> str:
        return str(PREFIX / self.value)

    def __repr__(self) -> str:
        return str(PREFIX / self.value)
