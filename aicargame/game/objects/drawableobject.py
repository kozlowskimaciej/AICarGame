import pygame
from pygame import Vector2


class DrawableObject(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, size: Vector2, texture=None, color=None):
        if texture is None and color is None:
            raise NotImplementedError

        super().__init__()

        self._surf = pygame.display.get_surface()
        self._size = size
        self.RAW_TEXTURE = texture

        self.image = pygame.Surface(self._size)
        if texture is None:
            self.image.fill(color)
        else:
            self.texture = texture

        self.rect = self.image.get_rect()
        self.rect.center = position

    @property
    def texture(self):
        return self.RAW_TEXTURE

    @texture.setter
    def texture(self, value):
        self.RAW_TEXTURE = value
        self.image = pygame.transform.scale(self.RAW_TEXTURE, self._size)

    def render(self):
        self._surf.blit(self.image, self.rect.topleft)
