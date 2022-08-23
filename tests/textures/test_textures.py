from pathlib import Path

from pygame import Surface


def test_textures_valid():
    from aicargame.game.textures.textures import Textures

    for texture in Textures:
        assert Path(texture.__str__()).exists()
        assert isinstance(getattr(Textures, texture.name), Surface)
