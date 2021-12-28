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
    def __init__(self, x, y, img, fon, *group):
        super().__init__(*group)
        self.image = load_image(img, fon)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def exit():
    Image(450, 100, 'Вы действительно хотите выйти.png', 0, all_sprites)
    Yes = Image(600, 230, 'да.jpg', 0, all_sprites)
    No = Image(560, 410, 'нет.jpg', 0, all_sprites)


def settings():
    Image(400, 0, 'Фон настроек.jpg', -1, all_sprites)
    Image(600, 20, 'прицелы.png', -1, all_sprites)
    Image(480, 600, 'сбросить прогресс.png', -1, all_sprites)


def levels():
    Image(400, 0, 'Фон уровней.jpg', -1, all_sprites)

    Level_one = Image(450, 50, '1 уровень.png', -1, all_sprites)
    Level_two = Image(450, 200, '2 уровень.png', -1, all_sprites)
    Level_three = Image(450, 350, '3 уровень.png', -1, all_sprites)
    Level_four = Image(450, 500, '4 уровень.png', -1, all_sprites)

    Coin_1_lvl1 = Image(650, 50, 'Монетка.png', -1, all_sprites)
    Coin_2_lvl1 = Image(750, 50, 'Монетка.png', -1, all_sprites)
    Coin_3_lvl1 = Image(850, 50, 'Монетка.png', -1, all_sprites)

    Coin_1_lvl2 = Image(650, 200, 'Монетка.png', -1, all_sprites)
    Coin_2_lvl2 = Image(750, 200, 'Монетка.png', -1, all_sprites)
    Coin_3_lvl2 = Image(850, 200, 'Монетка.png', -1, all_sprites)

    Coin_1_lvl3 = Image(650, 350, 'Монетка.png', -1, all_sprites)
    Coin_2_lvl3 = Image(750, 350, 'Монетка.png', -1, all_sprites)
    Coin_3_lvl3 = Image(850, 350, 'Монетка.png', -1, all_sprites)

    Coin_1_lvl4 = Image(650, 500, 'Монетка.png', -1, all_sprites)
    Coin_2_lvl4 = Image(750, 500, 'Монетка.png', -1, all_sprites)
    Coin_3_lvl4 = Image(850, 500, 'Неактивная монетка.png', -1, all_sprites)


def new_game():
    Image(0, 0, 'Фон меню слева.jpg', -1, all_sprites)
    Image(400, 0, 'фон меню справа.jpg', -1, all_sprites)

    Exit = Image(90, 550, 'Выход.png', -1, all_sprites)
    Settings = Image(30, 370, 'Настройки.png', -1, all_sprites)
    Levels = Image(80, 220, 'Уровни.png', -1, all_sprites)
    New_game = Image(20, 70, 'Новая игра.png', -1, all_sprites)


def place(Place):
    if Place == 'new_game':
        return new_game()
    elif Place == 'settings':
        return settings()
    elif Place == 'levels':
        return levels()


if __name__ == '__main__':
    pygame.init()
    size = width, height = 1200, 700
    screen = pygame.display.set_mode(size)
    # pygame.display.set_caption('Name')

    all_sprites = pygame.sprite.Group()

    Fon_menu_left = Image(0, 0, 'Фон меню слева.jpg', -1, all_sprites)
    Fon_menu_right = Image(400, 0, 'фон меню справа.jpg', -1, all_sprites)

    Exit = Image(90, 550, 'Выход.png', -1, all_sprites)
    Settings = Image(30, 370, 'Настройки.png', -1, all_sprites)
    Levels = Image(80, 220, 'Уровни.png', -1, all_sprites)
    New_game = Image(20, 70, 'Новая игра.png', -1, all_sprites)

    Place = 'new_game'

    run = True
    active = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect.collidepoint(Exit.rect, pygame.mouse.get_pos()) and active:
                    active = False
                    exit()
                    Yes = Image(600, 230, 'да.jpg', 0, all_sprites)
                    No = Image(560, 410, 'нет.jpg', 0, all_sprites)
                if pygame.Rect.collidepoint(Settings.rect, pygame.mouse.get_pos()) and active:
                    settings()
                    Place = 'settings'
                    progress = Image(480, 600, 'сбросить прогресс.png', -1, all_sprites)
                if pygame.Rect.collidepoint(Levels.rect, pygame.mouse.get_pos()) and active:
                    lvl = True
                    levels()
                    Level_one = Image(450, 50, '1 уровень.png', -1, all_sprites)
                    Level_two = Image(450, 200, '2 уровень.png', -1, all_sprites)
                    Level_three = Image(450, 350, '3 уровень.png', -1, all_sprites)
                    Level_four = Image(450, 500, '4 уровень.png', -1, all_sprites)
                    Place = 'levels'
                if pygame.Rect.collidepoint(New_game.rect, pygame.mouse.get_pos()) and active:
                    new_game()
                    Place = 'new_game'

                if Place == 'levels' and active:
                    if pygame.Rect.collidepoint(Level_one.rect, pygame.mouse.get_pos()):
                        print('Level_one')
                    if pygame.Rect.collidepoint(Level_two.rect, pygame.mouse.get_pos()):
                        print('Level_two')
                    if pygame.Rect.collidepoint(Level_three.rect, pygame.mouse.get_pos()):
                        print('Level_three')
                    if pygame.Rect.collidepoint(Level_four.rect, pygame.mouse.get_pos()):
                        print('Level_four')
                if Place == 'settings':
                    if pygame.Rect.collidepoint(progress.rect, pygame.mouse.get_pos()):
                        print('сбросить прогресс')
                if active is False:
                    if pygame.Rect.collidepoint(Yes.rect, pygame.mouse.get_pos()):
                        run = False
                    if pygame.Rect.collidepoint(No.rect, pygame.mouse.get_pos()):
                        active = True
                        place(Place)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
