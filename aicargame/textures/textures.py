from enum import Enum, auto
from pathlib import Path

PREFIX = Path("aicargame/textures/media/").resolve()


class Textures(Enum):
    PLAYER = "player.gif"

    def __str__(self) -> str:
        return str(PREFIX / self.value)

    def __repr__(self) -> str:
        return str(PREFIX / self.value)
