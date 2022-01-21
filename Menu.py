from main1 import *
import main1
import os

COUNT_MONEY = 0
COUNT_LVL = 1
EXIT = False
ALL_SPRITES = pygame.sprite.Group()


with open("settings.txt", "w") as file:
    file.write("platform.png фон")


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


def count_money(number, new=False):
    global COUNT_MONEY
    if new:
        COUNT_MONEY = 0
    else:
        COUNT_MONEY += number


def count_lvl(number):
    global COUNT_LVL
    if COUNT_LVL + number < 5:
        COUNT_LVL += number
    else:
        COUNT_LVL = 1


class Image(pygame.sprite.Sprite):
    def __init__(self, x, y, img, fon, *group):
        super().__init__(*group)
        self.image = load_image(img, fon)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


def exit():
    Image(450, 100, 'Вы действительно хотите выйти.png', 0, ALL_SPRITES)
    Image(600, 230, 'да.jpg', 0, ALL_SPRITES)
    Image(560, 410, 'нет.jpg', 0, ALL_SPRITES)


def settings():
    Image(400, 0, 'Фон настроек.jpg', -1, ALL_SPRITES)

    file = os.path.dirname(__file__)
    Image(530, 160, '%s/блоки/блок1.jpg' % file, 0, ALL_SPRITES)
    Image(630, 160, '%s/блоки/блок2.jpg' % file, 0, ALL_SPRITES)
    Image(730, 160, '%s/блоки/блок3.jpg' % file, 0, ALL_SPRITES)
    Image(830, 160, '%s/блоки/блок4.jpg' % file, 0, ALL_SPRITES)
    Image(930, 160, '%s/блоки/блок5.jpg' % file, 0, ALL_SPRITES)
    Image(1030, 160, '%s/блоки/блок6.jpg' % file, 0, ALL_SPRITES)

    Image(500, 10, 'тип платформы.png', -1, ALL_SPRITES)
    Image(480, 600, 'сбросить прогресс.png', -1, ALL_SPRITES)


def levels():
    Image(400, 0, 'Фон уровней.jpg', -1, ALL_SPRITES)

    Level_one = Image(450, 50, '1 уровень.png', -1, ALL_SPRITES)
    Level_two = Image(450, 200, '2 уровень.png', -1, ALL_SPRITES)
    Level_three = Image(450, 350, '3 уровень.png', -1, ALL_SPRITES)
    Level_four = Image(450, 500, '4 уровень.png', -1, ALL_SPRITES)

    Coin_1_lvl1 = Image(650, 50, 'Неактивная монетка.png', -1, ALL_SPRITES)
    Coin_2_lvl1 = Image(750, 50, 'Неактивная монетка.png', -1, ALL_SPRITES)
    Coin_3_lvl1 = Image(850, 50, 'Неактивная монетка.png', -1, ALL_SPRITES)

    Coin_1_lvl2 = Image(650, 200, 'Неактивная монетка.png', -1, ALL_SPRITES)
    Coin_2_lvl2 = Image(750, 200, 'Неактивная монетка.png', -1, ALL_SPRITES)
    Coin_3_lvl2 = Image(850, 200, 'Неактивная монетка.png', -1, ALL_SPRITES)

    Coin_1_lvl3 = Image(650, 350, 'Неактивная монетка.png', -1, ALL_SPRITES)
    Coin_2_lvl3 = Image(750, 350, 'Неактивная монетка.png', -1, ALL_SPRITES)
    Coin_3_lvl3 = Image(850, 350, 'Неактивная монетка.png', -1, ALL_SPRITES)

    Coin_1_lvl4 = Image(650, 500, 'Неактивная монетка.png', -1, ALL_SPRITES)
    Coin_2_lvl4 = Image(750, 500, 'Неактивная монетка.png', -1, ALL_SPRITES)
    Coin_3_lvl4 = Image(850, 500, 'Неактивная монетка.png', -1, ALL_SPRITES)


def new_game():
    Image(0, 0, 'Фон меню слева.jpg', -1, ALL_SPRITES)
    Image(90, 550, 'Выход.png', -1, ALL_SPRITES)
    Image(30, 370, 'Настройки.png', -1, ALL_SPRITES)
    Image(80, 220, 'Уровни.png', -1, ALL_SPRITES)
    Image(20, 70, 'Новая игра.png', -1, ALL_SPRITES)
    Image(400, 0, 'фон меню справа.jpg', -1, ALL_SPRITES)


def place(Place):
    if Place == 'new_game':
        return new_game()
    elif Place == 'settings':
        return settings()
    elif Place == 'levels':
        return levels()


def start():
    pygame.init()
    size = width, height = 1200, 700
    screen = pygame.display.set_mode(size)
    # pygame.display.set_caption('Name')

    all_sprites = pygame.sprite.Group()

    Fon_menu_left = Image(0, 0, 'Фон меню слева.jpg', -1, ALL_SPRITES)
    Fon_menu_right = Image(400, 0, 'фон меню справа.jpg', -1, ALL_SPRITES)

    Exit = Image(90, 550, 'Выход.png', -1, ALL_SPRITES)
    Settings = Image(30, 370, 'Настройки.png', -1, ALL_SPRITES)
    Levels = Image(80, 220, 'Уровни.png', -1, ALL_SPRITES)
    New_game = Image(20, 70, 'Новая игра.png', -1, ALL_SPRITES)

    Place = 'new_game'
    yes_or_no = False
    block = ''

    run = True
    active = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pygame.Rect.collidepoint(Exit.rect, pygame.mouse.get_pos()) and active:
                    active = False
                    exit()
                    Yes = Image(600, 230, 'да.jpg', 0, ALL_SPRITES)
                    No = Image(560, 410, 'нет.jpg', 0, ALL_SPRITES)
                if pygame.Rect.collidepoint(Settings.rect, pygame.mouse.get_pos()) and active:
                    settings()
                    Place = 'settings'
                    progress = Image(480, 600, 'сбросить прогресс.png', -1, ALL_SPRITES)
                    file = os.path.dirname(__file__)
                    block1 = Image(530, 160, '%s/блоки/блок1.jpg' % file, 0, ALL_SPRITES)
                    block2 = Image(630, 160, '%s/блоки/блок2.jpg' % file, 0, ALL_SPRITES)
                    block3 = Image(730, 160, '%s/блоки/блок3.jpg' % file, 0, ALL_SPRITES)
                    block4 = Image(830, 160, '%s/блоки/блок4.jpg' % file, 0, ALL_SPRITES)
                    block5 = Image(930, 160, '%s/блоки/блок5.jpg' % file, 0, ALL_SPRITES)
                    block6 = Image(1030, 160, '%s/блоки/блок6.jpg' % file, 0, ALL_SPRITES)
                if pygame.Rect.collidepoint(Levels.rect, pygame.mouse.get_pos()) and active:
                    lvl = True
                    levels()
                    Level_one = Image(450, 50, '1 уровень.png', -1, ALL_SPRITES)
                    Level_two = Image(450, 200, '2 уровень.png', -1, ALL_SPRITES)
                    Level_three = Image(450, 350, '3 уровень.png', -1, ALL_SPRITES)
                    Level_four = Image(450, 500, '4 уровень.png', -1, ALL_SPRITES)
                    Place = 'levels'
                if pygame.Rect.collidepoint(New_game.rect, pygame.mouse.get_pos()) and active:
                    new_game()
                    main1.exit_level_f()
                    main1.main1()

                if Place == 'levels' and active:
                    if pygame.Rect.collidepoint(Level_one.rect, pygame.mouse.get_pos()):
                        main1.exit_level_f()
                        main1.main1()
                    if pygame.Rect.collidepoint(Level_two.rect, pygame.mouse.get_pos()):
                        main1.exit_level_f()
                        main1.main1('level_2', '2.png')
                    if pygame.Rect.collidepoint(Level_three.rect, pygame.mouse.get_pos()):
                        main1.exit_level_f()
                        main1.main1('level_3', '3.png')
                    if pygame.Rect.collidepoint(Level_four.rect, pygame.mouse.get_pos()):
                        main1.exit_level_f()
                        main1.main1('level_4', '4.png')
                if Place == 'settings' and active:
                    if pygame.Rect.collidepoint(block1.rect, pygame.mouse.get_pos()):
                        if yes_or_no:
                            settings()
                        Image(508, 200, 'выбран.png', -1, ALL_SPRITES)
                        block = 'блок1.jpg'
                        yes_or_no = True
                    if pygame.Rect.collidepoint(block2.rect, pygame.mouse.get_pos()):
                        if yes_or_no:
                            settings()
                        Image(608, 200, 'выбран.png', -1, ALL_SPRITES)
                        block = 'блок2.jpg'
                        yes_or_no = True
                    if pygame.Rect.collidepoint(block3.rect, pygame.mouse.get_pos()):
                        if yes_or_no:
                            settings()
                        Image(708, 200, 'выбран.png', -1, ALL_SPRITES)
                        block = 'блок3.jpg'
                        yes_or_no = True
                    if pygame.Rect.collidepoint(block4.rect, pygame.mouse.get_pos()):
                        if yes_or_no:
                            settings()
                        Image(808, 200, 'выбран.png', -1, ALL_SPRITES)
                        block = 'блок4.jpg'
                        yes_or_no = True
                    if pygame.Rect.collidepoint(block5.rect, pygame.mouse.get_pos()):
                        if yes_or_no:
                            settings()
                        Image(908, 200, 'выбран.png', -1, ALL_SPRITES)
                        block = 'блок5.jpg'
                        yes_or_no = True
                    if pygame.Rect.collidepoint(block6.rect, pygame.mouse.get_pos()):
                        if yes_or_no:
                            settings()
                        Image(1008, 200, 'выбран.png', -1, ALL_SPRITES)
                        block = 'блок6.jpg'
                        yes_or_no = True

                    if block != '':
                        with open("settings.txt", "w") as file:
                            file.write(f"{block} фон")

                    if pygame.Rect.collidepoint(progress.rect, pygame.mouse.get_pos()):
                        print('сбросить прогресс')
                if active is False:
                    if pygame.Rect.collidepoint(Yes.rect, pygame.mouse.get_pos()):
                        sys.exit()
                    if pygame.Rect.collidepoint(No.rect, pygame.mouse.get_pos()):
                        active = True
                        place(Place)
        ALL_SPRITES.draw(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    start()
