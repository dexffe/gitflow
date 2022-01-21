import pygame

import Menu
import os
from Menu import *
from pygame import *

BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        with open("settings.txt") as file:
            s1 = file.read().split()
        self.image = image.load(F'%s/блоки/{s1[0]}' % os.path.dirname(__file__))
        self.rect = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)


class Money(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image1 = Menu.load_image("Монетка.png", -1)
        self.image = pygame.transform.scale(image1, (BLOCK_WIDTH, BLOCK_HEIGHT))
        self.rect = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)


class Exit(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image1 = Menu.load_image("Выход_lvl.png", -1)
        self.image = pygame.transform.scale(image1, (BLOCK_WIDTH, BLOCK_HEIGHT))
        self.rect = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)


class Stop(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        image1 = Menu.load_image("stop.png", -1)
        self.image = pygame.transform.scale(image1, (BLOCK_WIDTH, BLOCK_HEIGHT))
        self.rect = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)