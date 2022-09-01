import pygame
from pygame import Vector2
from random import randint

from aicargame.game.game import Game
from aicargame.game.objects.player import Player
from aicargame.game.objects.enemy import Enemy

from aicargame.events import (
    GAME_OVER,
    START_GAME
)


def main():
    pygame.init()

    game = Game()

    run = True

    while run:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == START_GAME:
                game.startGame()
            if event.type == GAME_OVER:
                game.endGame()

        game.update()
        game.render()

    pygame.quit()


if __name__ == "__main__":
    main()
