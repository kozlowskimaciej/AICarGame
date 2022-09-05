import pygame
from aicargame.game.game import Game

def main():
    pygame.init()

    game = Game()

    while game.isRunning:
        game.update()
        game.render()

    pygame.quit()

if __name__ == "__main__":
    main()
