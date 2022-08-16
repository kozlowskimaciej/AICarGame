import pygame
from pygame import Vector2


class DrawableObject(pygame.sprite.Sprite):
    def __init__(self, position: Vector2, size: Vector2, texture=None, color=None):
        if texture is None and color is None:
            raise NotImplementedError

        super().__init__()

        self.image = pygame.Surface(size)

        if texture is None:
            self.image.fill(color)
        else:
            try:
                texture = pygame.image.load(str(texture))
            except Exception as ex:
                self.image.fill((255, 255, 255))
                print(str(ex))
            else:
                texture = pygame.transform.scale(texture, size)
                self.image = texture

        self.rect = self.image.get_rect()
        self.rect.center = position
