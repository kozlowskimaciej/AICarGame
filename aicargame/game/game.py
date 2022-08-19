import time

import pygame

from aicargame.globals import (
    PLAYER_SIZE,
    PLAYER_START,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    ENEMY_INTERVAL,
)
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy
from aicargame.game.textures.textures import Textures


class Game:
    sprites = pygame.sprite.Group()
    enemySprites = pygame.sprite.Group()
    window: pygame.Surface
    bg = Textures.BACKGROUND
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AICarGame")

        self.obj = Player(PLAYER_START, PLAYER_SIZE)

        self.sprites.add(self.obj)

    def checkCollisions(self):
        if pygame.sprite.spritecollide(self.obj, self.enemySprites, False) != []:
            print("Uuu kraksa")

    def update(self):
        cur_time = time.time()

        if cur_time - Enemy.timer >= ENEMY_INTERVAL:
            self.enemySprites.add(Enemy.spawnEnemy())
            Enemy.timer = cur_time

        self.checkCollisions()

        self.window.fill((0, 0, 0))
        self.window.blit(self.bg, (0, 0))
        self.sprites.update()
        self.sprites.draw(self.window)
        self.enemySprites.update()
        self.enemySprites.draw(self.window)
