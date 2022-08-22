import time
import random

import pygame

from aicargame.globals import (
    ENEMY_START_VELOCITY,
    SPEED_CHANGE_TIMER,
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    ENEMY_INTERVAL,
)
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy
from aicargame.game.objects.gui.gui import GUI
from aicargame.game.textures.textures import Textures


class Game:
    enemySprites = pygame.sprite.Group()
    # gui = Speedo((0, 0), (WINDOW_WIDTH, 100))
    # gui2 = Mileage((0, 100), (WINDOW_WIDTH, 100))
    gui: GUI
    window: pygame.Surface
    bg = pygame.transform.scale(Textures.BACKGROUND, (WINDOW_WIDTH, WINDOW_HEIGHT))
    next_enemy_spawn: int = ENEMY_INTERVAL[1] / 100

    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("AICarGame")

        self.gui = GUI(self.window)
        self.__player = Player()

    def reset(self):
        self.__player.reset()
        self.enemySprites.empty()
        Enemy.start_velocity = ENEMY_START_VELOCITY
        self.gui.reset()

    def checkCollisions(self):
        if pygame.sprite.spritecollide(self.__player, self.enemySprites, False) != []:
            self.reset()

    def update(self):
        cur_time = time.time()

        if cur_time - Enemy.spawn_timer >= self.next_enemy_spawn:
            self.next_enemy_spawn = (
                int(
                    random.randrange(
                        start=ENEMY_INTERVAL[0], stop=ENEMY_INTERVAL[1], step=1
                    )
                )
                / 100
            )
            self.enemySprites.add(Enemy.spawnEnemy())
            Enemy.spawn_timer = cur_time

        self.__player.update()
        self.enemySprites.update()
        self.gui.update()
        self.checkCollisions()

    def render(self):
        self.window.fill((0, 0, 0))
        self.window.blit(self.bg, (0, 0))
        self.window.blit(self.__player.image, self.__player.rect.topleft)
        self.enemySprites.draw(self.window)
        self.gui.render()
        pygame.display.update()
