import time
import random

import pygame

from aicargame.globals import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    ENEMY_INTERVAL,
)
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy
from aicargame.game.objects.gui.speedo import Speedo
from aicargame.game.objects.gui.mileage import Mileage
from aicargame.game.textures.textures import Textures


class Game:
    enemySprites = pygame.sprite.Group()
    gui = Speedo((0, 0), (WINDOW_WIDTH, 100))
    gui2 = Mileage((0, 100), (WINDOW_WIDTH, 100))
    window: pygame.Surface
    bg = pygame.transform.scale(Textures.BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))
    next_enemy_spawn: int = ENEMY_INTERVAL[1] / 100

    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AICarGame")

        self.__player = Player()

    def reset(self):
        self.__player.reset()
        self.enemySprites.empty()

    def checkCollisions(self):
        if pygame.sprite.spritecollide(self.__player, self.enemySprites, False) != []:
            self.reset()

    def update(self):
        cur_time = time.time()

        if cur_time - Enemy.timer >= self.next_enemy_spawn:
            self.next_enemy_spawn = (
                int(
                    random.randrange(
                        start=ENEMY_INTERVAL[0], stop=ENEMY_INTERVAL[1], step=1
                    )
                )
                / 100
            )
            self.enemySprites.add(Enemy.spawnEnemy())
            Enemy.timer = cur_time

        self.checkCollisions()

        self.window.fill((0, 0, 0))
        self.window.blit(self.bg, (0, 0))
        self.__player.update()
        self.window.blit(self.__player.image, self.__player.rect.topleft)
        self.enemySprites.update()
        self.gui.update()
        self.gui2.update()

        self.enemySprites.draw(self.window)
        self.window.blit(self.gui.image, (0, 0))
        self.window.blit(self.gui2.image, (0, 100))
