import os
import pygame


def load_image(name, color_key=None):
    full_name = os.path.join('картинки проекта', name)
    try:
        image = pygame.image.load(full_name).convert()
    except pygame.error as message:
        print('В папке нет файла:', name)
        raise SystemExit(message)

    if color_key == -1:
        color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Image(pygame.sprite.Sprite):
    def __init__(self, x, y, img, *group):
        super().__init__(*group)
        self.image = load_image(img, -1)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 700
    screen = pygame.display.set_mode(size)
    # pygame.display.set_caption('Name')

    all_sprites = pygame.sprite.Group()

    Image(0, 0, 'Фон меню слева.jpg', all_sprites)
    Image(400, 0, 'фон меню справа.jpg', all_sprites)

    '''---------------------------'''
    img = [
        'Выход.png',
        'Настройки.png',
        'Уровни.png',
        'Новая игра.png'
    ]
    x, y = -100, 500  # Рисует кнопки на меню
    for im in img:
        Image(x, y, im, all_sprites)
        y -= 150
    '''---------------------------'''

    run = True
    while run:
        # screen.fill('green', (0, 0, 400, 700))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
