from pygame import *
import os

BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = image.load('%s/блоки/platform.png' % os.path.dirname(__file__))
        self.rect = Rect(x, y, BLOCK_WIDTH, BLOCK_HEIGHT)
