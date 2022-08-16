import pygame
from pygame import Vector2

from aicargame.objects.player import Player

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("AICarGame")

obj = Player(Vector2(50, 50), Vector2(100, 100))

all_sprites = pygame.sprite.Group()
all_sprites.add(obj)

run = True

while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    all_sprites.update()
    all_sprites.draw(win)

    pygame.display.update()

pygame.quit()
