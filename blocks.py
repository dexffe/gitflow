import Menu
from Menu import *
from pygame import *

BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = image.load('%s/блоки/platform.png' % os.path.dirname(__file__))
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