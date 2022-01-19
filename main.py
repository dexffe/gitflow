import sys
import pygame
from player import *
from blocks import *


class Camera:
    def __init__(self, camera_configure, width, height):
        self.camera_configure = camera_configure
        self.state = pygame.Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_configure(self.state, target.rect)


def camera_configure(camera, target_rect):
    left = -target_rect.x + 1200 / 2
    top = -target_rect.y + 700 / 2
    width, height = camera.width, camera.height

    left = min(0, left)
    left = max(-(camera.width - 1200), left)
    top = max(-(camera.height - 700), top)
    top = min(0, top)

    return pygame.Rect(left, top, width, height)


def main(lvl='level_1'):
    pygame.init()
    size = width, height = 1200, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("...")

    hero = Player(1100, 700)
    left = False
    right = False
    up = False

    all_sprites = pygame.sprite.Group()
    platforms = []

    all_sprites.add(hero)

    level_1 = [
        "-----------------------------------------",
        "-                                       -",
        "- m                                     -",
        "--------                                e",
        "-                                    ----",
        "-                -----               ----",
        "-                -----                  -",
        "-                                       -",
        "-      ----                             -",
        "-      ----                 ----        -",
        "-                           ----        -",
        "-                                       -",
        "-                ----                   -",
        "-                ----                   -",
        "-                                       -",
        "-     ----                             m-",
        "-     ----                           ----",
        "-                                   -----",
        "-                                       -",
        "-           ----                        -",
        "-           ----                        -",
        "-                   ----                -",
        "-m                    ----              -",
        "-----------------------------------------"]
    level_2 = []
    level_3 = []
    level_4 = []
    if lvl == 'level_1':
        level = level_1
    elif lvl == 'level_2':
        level = level_2
    elif lvl == 'level_3':
        level = level_3
    elif lvl == 'level_4':
        level = level_4

    time = pygame.time.Clock()
    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == "-":
                platforma = Platform(x, y)
                all_sprites.add(platforma)
                platforms.append(platforma)
            elif col == "m":
                money = Money(x, y)
                all_sprites.add(money)
            elif col == "e":
                exit = Exit(x, y)
                all_sprites.add(exit)

            x += BLOCK_WIDTH
        y += BLOCK_HEIGHT
        x = 0

    level_width = len(level[0]) * BLOCK_WIDTH
    level_height = len(level) * BLOCK_HEIGHT

    camera = Camera(camera_configure, level_width, level_height)

    while True:
        time.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == KEYDOWN and event.key == K_UP:
                up = True
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYUP and event.key == K_UP:
                up = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                left = False

        screen.fill('red')

        hero.update(left, right, up, platforms)

        camera.update(hero)
        for i in all_sprites:
            screen.blit(i.image, camera.apply(i))

        pygame.display.update()


if __name__ == "__main__":
    main()
