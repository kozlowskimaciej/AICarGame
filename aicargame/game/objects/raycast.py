import pygame
from pygame import Vector2

from aicargame.globals import WINDOW_HEIGHT, WINDOW_WIDTH

class RayCast(pygame.sprite.Sprite):
    def __init__(self, 
        position: Vector2, #center palyer
        length: float, #300
        angle: int,
        collision_group: pygame.sprite.Group
    ):
        super().__init__()
        self._position = position
        self._length = length
        self._angle = angle
        self._collision_group = collision_group

        self.rect = pygame.Rect(self._position, (1, 1))
        self._direction = Vector2(0, -1).rotate(self._angle)

    def fire(self) -> int:
        initial_pos = Vector2(self._position)
        while pygame.sprite.spritecollide(self, self._collision_group, False) == []:
            self._position += self._direction
            self.rect.left = self._position.x
            self.rect.top = self._position.y
            distance = (Vector2(self.rect.topleft) - initial_pos).length()

            if (self.rect.left > WINDOW_WIDTH or
                self.rect.right < 0 or
                self.rect.top > WINDOW_HEIGHT or
                self.rect.bottom < 0
            ):
                break 
            if distance >= self._length:
                break
    
        return min(distance, self._length) / self._length