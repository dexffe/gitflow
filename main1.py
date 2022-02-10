import pygame
import sys

import Menu
import player
from Menu import *
from player import *
from blocks import *


all_sprites = pygame.sprite.Group()
count_list = {0: '0 звезд.png',
              1: '1 звезда.png',
              2: '2 звезды.png',
              3: '3 звезды.png'}
num_lvl = {1: '1.png',
           2: '2.png',
           3: '3.png',
           4: '4.png'}
nums_lvl = {1: 'level_1',
            2: 'level_2',
            3: 'level_3',
            4: 'level_4'}


class Camera:
    def __init__(self, camera_configure, w, h):
        self.camera_configure = camera_configure
        self.state = pygame.Rect(0, 0, w, h)

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


def exit_level_t():
    global EXIT
    EXIT = True


def exit_level_f():
    global EXIT
    EXIT = False


def main1(lvl, number_lvl):
    pygame.init()
    size = width, height = 1200, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Our game")

    if number_lvl == '1.png':
        hero = Player(1184, 704)
    elif number_lvl == '2.png':
        hero = Player(1254, 1056)
    elif number_lvl == '3.png':
        hero = Player(1254, 1280)
    else:
        hero = Player(1832, 1100)

    left = False
    right = False
    up = False
    all_sprites = pygame.sprite.Group()
    platforms = []
    moneys = []
    stop_lvl = []

    all_sprites.add(hero)

    level_1 = [
        "---------------------------------------",
        "- m                                   -",
        "-                                     -",
        "--------                              e s-",
        "-                                  ------",
        "-                -----             ----",
        "-                -----                -",
        "-                                     -",
        "-      ----                           -",
        "-      ----                  ----     -",
        "-                            ----     -",
        "-                                     -",
        "--                ----                -",
        "--                ----                -",
        "-                                     -",
        "-     ----                           m-",
        "-     ----                         ----",
        "-                                 -----",
        "-                                     -",
        "-           ----                      -",
        "-           ----                      -",
        "-                   ----              -",
        "-m                    ----            -",
        "---------------------------------------"]
    level_2 = [
        "-----------------------------------------",
        "-m                                      e s-",
        "----                                  -----",
        "-                                   --  -",
        "-                              m        -",
        "- ---                         ---       -",
        "-                             ---       -",
        "-                                       -",
        "---                                     -",
        "-                                       -",
        "-                             ---       -",
        "-                             ---       -",
        "- ----                                  -",
        "-                                    ----",
        "-                                       -",
        "-              -----                    -",
        "-                                       -",
        "-                                 -     -",
        "-                              ----     -",
        "-         ---                           -",
        "-                                       -",
        "-                                       -",
        "-                                       -",
        "-                                       -",
        "-              ----                     -",
        "-              -m -                     -",
        "-              -- -                     -",
        "-           ----- ----                  -",
        "-           --    ----                  -",
        "-           -- -------                  -",
        "-        ----- ----------               -",
        "-        -----         --               -",
        "-     ---------------- --               -",
        "-                      ----             -",
        "-----------------------------------------"]
    level_3 = [
        "------------------------------------------",
        "-     m      --   m        --m           e s-",
        "-            --            --            ---",
        "-            --         -----   -        -",
        "-            --         -----            -",
        "-            --         -----        -   -",
        "---        ----  -         --            -",
        "-            --            --  -         -",
        "-            --            --            -",
        "-            --            --         -- -",
        "-            --       --   --            -",
        "-     --     --            --            -",
        "-            --            --            -",
        "-            --            ----          -",
        "-            --        --- --            -",
        "-     --     --        --- --            -",
        "-     --     --            --            -",
        "-            --            --         - --",
        "-            --            --            -",
        "-          -------         --            -",
        "-          -------         --            -",
        "-            --            --  --        -",
        "-            --            --            -",
        "---          --            --            -",
        "---          -----         --            -",
        "-            --            --     --  - --",
        "-            --            --            -",
        "-            --        --  --            -",
        "---          --        --  --            -",
        "---          --            -----         -",
        "-            --            --            -",
        "-            --    -       --            -",
        "-            --            --            -",
        "---          --         -- --         ----",
        "-            --            --            -",
        "-            --            --            -",
        "-            --            --            -",
        "-            --            --            -",
        "---          ------    ---------         -",
        "-                                        -",
        "-                                        -",
        "------------------------------------------"]
    level_4 = [
        "-----------------------------------------------------------",
        "-         ---                -                            -",
        "-     -   ---               m-                            -",
        "-     -   ---        ---------                            -",
        "-     -   ---                                       ---   -",
        "-    --   ----                      -               ---   -",
        "-     -   ---                                       ---   -",
        "-     -   ---               -                       ---  --",
        "-     -   ---                                 -     ---   -",
        "-  -- -   ---      -                                ---   -",
        "-     -   ---                                      ----   -",
        "-     -   ---                                    -------- -",
        "-     -   ---                                    ---      -",
        "-     -   ---                  --------------------- ------",
        "--    -   ---                  --                    ------",
        "-     -   ----------------------- --------------- ---------",
        "-     -   -------                 --------------- ---------",
        "-     -   ------- --------------- --------------          -",
        "-     -   ------- --------------- -------------  -------- -",
        "-    --   ------- ---------------       ------  --------- -",
        "-     -   ------- ------  m ----------- -----  ---------  -",
        "-     -   ------- ------ -------------- -----       ---- --",
        "-     -   -------  -----  ------------- ----------- ---- --",
        "--    -   -------- ------ ------        ----------- ---- --",
        "-     -   -------- -----  -------------------------  ---  -",
        "-     -   -------- ----- --------------------------- ---- -",
        "-     -   -------- -----  --------------------------      -",
        "-     -   -------- ------ I --------------------------    -",
        "-  -- -   -------- --------                    ------- ----",
        "-     -   -------- ---------             -----  ------    -",
        "-     -   -------- --------                ---- --------- -",
        "-     -   -------- --------          -     ---- --------- -",
        "-     -   -------- --------   -            ----           -",
        "---- --   -------- --------              -------------  ---",
        "-    -     ------- --------                -------        -",
        "-    -  s  ------- --------                -------        -",
        "-    -     ------- ---------                              -",
        "- ---------------- --------       -        -----------  ---",
        "-             ---- --------              - -----------    -",
        "-             ---- --------                -------------- -",
        "---           ---- --------    -           -------------  -",
        "---           ---- --------                ------------- --",
        "-             ---- --------                -------------  -",
        "-       ---   ---- --------              ---------------- -",
        "-       ---   ---- --------  --            -------------  -",
        "-             ---- --------                ------------- --",
        "-             ---- --------                -------------  -",
        "-             ---- --------      -         -------------- -",
        "-   ---       ---- ----------              -------------  -",
        "-   ---       ---- --------                ------------- --",
        "-             ---- --------            -   -------------  -",
        "-             ---- --------                -------------- -",
        "-           ------ --------                -------------  -",
        "-           ------ --------        --      ------------- --",
        "-             ---- ----------              -------------  -",
        "-             ---- --------                -------------- -",
        "- ---         ---- --------              ---------------  -",
        "- ---         ---- --------       -                      --",
        "-             ---- --------                -------------  -",
        "-             ---- ----------              -------------- -",
        "-             ---- --------                -------------  -",
        "-       --    ---- --------                ------------- --",
        "-       --    ---- --------                -------------  -",
        "-             ----        I                -------------- -",
        "-             ------------------------------------------  -",
        "-             ----------------------m------------------- --",
        "---           ---------------------  -------------------  -",
        "---           --------------------- --------------------- -",
        "-             ---------------------   ------------------  -",
        "-             ----------------------- ------------------ --",
        "-           -----------------------   ------------------  -",
        "-           ----------------------- --------------------- -",
        "-             ---------------------I--------------------  -",
        "-                                                         -",
        "-----------------------------------------------------------"]
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
                moneys.append(money)
            elif col == "e":
                exit = Exit(x, y)
                all_sprites.add(exit)
            elif col == "s":
                stop = Stop(x, y)
                stop_lvl.append(stop)
            elif col == "I":
                platforma = Platform(x, y)
                all_sprites.add(platforma)

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
            if EXIT:
                screen_money()
                left = False
                right = False
                up = False
                x, y = width // 2 - 367 // 2, height // 2 - 269 // 2
                x2, y2 = width // 2 - 20, height // 2 - 80

                img = count_list[Menu.COUNT_MONEY]
                Menu.Image(x, y, img, -1, all_sprites)
                Menu.Image(x2, y2, number_lvl, -1, all_sprites)

                home = Menu.Image(450, 400, 'домой.png', -1, all_sprites)
                next_lvl = Menu.Image(650, 400, 'следующий уровень.png', -1, all_sprites)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                try:
                    if pygame.Rect.collidepoint(home.rect, pygame.mouse.get_pos()):
                        Menu.COUNT_MONEY = 0
                        Menu.count_lvl_next(1)
                        Menu.start()
                    if pygame.Rect.collidepoint(next_lvl.rect, pygame.mouse.get_pos()):
                        exit_level_f()
                        left = True
                        right = True
                        up = True
                        Menu.count_money(1, True)
                        Menu.count_lvl_next(1)
                        main1(nums_lvl[Menu.COUNT_LVL_NEXT], num_lvl[Menu.COUNT_LVL_NEXT])
                except UnboundLocalError:
                    pass

        with open('settings.txt') as file:
            data = file.read().split()
        bg = Menu.load_image(data[1]).convert()
        bg = pygame.transform.smoothscale(bg, screen.get_size())
        screen.blit(bg, (0, 0))

        hero.update(left, right, up, platforms, moneys, stop_lvl)

        camera.update(hero)
        for i in all_sprites:
            screen.blit(i.image, camera.apply(i))
        for i in moneys:
            screen.blit(i.image, camera.apply(i))
        for i in stop_lvl:
            screen.blit(i.image, camera.apply(i))

        pygame.display.update()


if __name__ == "__main__":
    main1(nums_lvl[Menu.COUNT_LVL], num_lvl[Menu.COUNT_LVL])
