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

    Fon_menu_left = Image(0, 0, 'Фон меню слева.jpg', all_sprites)
    Fon_menu_right = Image(400, 0, 'фон меню справа.jpg', all_sprites)

    Exit = Image(90, 550, 'Выход.png', all_sprites)
    Settings = Image(30, 370, 'Настройки.png', all_sprites)
    Levels = Image(80, 220, 'Уровни.png', all_sprites)
    New_game = Image(20, 70, 'Новая игра.png', all_sprites)



    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(Exit.rect, pygame.mouse.get_pos()):
                    run = False
                if pygame.Rect.collidepoint(Settings.rect, pygame.mouse.get_pos()):
                    Fon_settings = Image(400, 0, 'Фон настроек.jpg', all_sprites)
                    Aim_tip = Image(300, -90, 'Тип прицела.png', all_sprites)
                if pygame.Rect.collidepoint(Levels.rect, pygame.mouse.get_pos()):
                    print('Levels')
                if pygame.Rect.collidepoint(New_game.rect, pygame.mouse.get_pos()):
                    print('New_game')


        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
