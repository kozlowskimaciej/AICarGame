import time
from tkinter.tix import WINDOW

import pygame
from pygame import Vector2

from aicargame.globals import WINDOW_HEIGHT, WINDOW_WIDTH, ENEMY_INTERVAL
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy
from aicargame.game.textures.textures import Textures

class Game:
    sprites = pygame.sprite.Group()
    window: pygame.Surface
    bg = pygame.image.load(str(Textures.BACKGROUND))
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))

    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AICarGame")

        obj = Player(Vector2(50, 50), Vector2(100, 100))

        self.sprites.add(obj)

    def update(self):
        cur_time = time.time()

        if(cur_time - Enemy.timer >= ENEMY_INTERVAL):
            self.sprites.add(Enemy.spawnEnemy())
            Enemy.timer = cur_time

        self.window.fill((0, 0, 0))
        self.window.blit(self.bg, (0, 0))
        self.sprites.update()
        self.sprites.draw(self.window)
