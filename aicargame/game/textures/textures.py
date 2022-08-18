from enum import Enum, EnumMeta
from pathlib import Path
from functools import lru_cache

from pygame.image import load
import pygame

PREFIX = Path("aicargame/game/textures/media/").resolve()


class TexturesMeta(EnumMeta):
    def __getattribute__(cls, img: pygame.Surface | Path) -> pygame.Surface:
        texture = super().__getattribute__(img)
        if isinstance(texture, cls):
            texture = TexturesMeta.__cached_texture(cls, PREFIX / texture.value)
        return texture

    @lru_cache
    def __cached_texture(self, path: Path) -> pygame.Surface:
        if isinstance(path, Path):
            try:
                texture = load(path)
            except Exception as ex:
                print("ERR" + ex)
        else:
            raise FileNotFoundError("Invalid path to texture")

        return texture


class Textures(Enum, metaclass=TexturesMeta):
    BACKGROUND = "bg.png"
    PLAYER = "player.gif"
    ENEMY = "nuclear-bomb.png"

    def __str__(self) -> str:
        return str(PREFIX / self.value)

    def __repr__(self) -> str:
        return str(PREFIX / self.value)
