from main1 import *
import main1
import os

COUNT_MONEY = 0
COUNT_LVL_NEXT = 1
EXIT = False
ALL_SPRITES = pygame.sprite.Group()
num_lvl = {1: '1.png',
           2: '2.png',
           3: '3.png',
           4: '4.png'}
nums_lvl = {1: 'level_1',
            2: 'level_2',
            3: 'level_3',
            4: 'level_4'}

COIN = {'Coin_1_lvl1': 'Неактивная_монетка.png',
        'Coin_2_lvl1': 'Неактивная_монетка.png',
        'Coin_3_lvl1': 'Неактивная_монетка.png',

        'Coin_1_lvl2': 'Неактивная_монетка.png',
        'Coin_2_lvl2': 'Неактивная_монетка.png',
        'Coin_3_lvl2': 'Неактивная_монетка.png',

        'Coin_1_lvl3': 'Неактивная_монетка.png',
        'Coin_2_lvl3': 'Неактивная_монетка.png',
        'Coin_3_lvl3': 'Неактивная_монетка.png',

        'Coin_1_lvl4': 'Неактивная_монетка.png',
        'Coin_2_lvl4': 'Неактивная_монетка.png',
        'Coin_3_lvl4': 'Неактивная_монетка.png'}
for i in range(4):
    with open(f"level{i + 1}.txt") as file:
        s1 = file.read().split()
        if s1 != []:
            COIN[f'Coin_1_lvl{i + 1}'] = s1[0]
            COIN[f'Coin_2_lvl{i + 1}'] = s1[1]
            COIN[f'Coin_3_lvl{i + 1}'] = s1[2]


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


def count_lvl_next(number):
    global COUNT_LVL_NEXT
    if COUNT_LVL_NEXT + number < 5:
        COUNT_LVL_NEXT += number
    else:
        COUNT_LVL_NEXT = 1


def screen_money():
    global COIN
    if COUNT_MONEY == 3:
        COIN[f'Coin_1_lvl{COUNT_LVL_NEXT}'] = 'Монетка.png'
        COIN[f'Coin_2_lvl{COUNT_LVL_NEXT}'] = 'Монетка.png'
        COIN[f'Coin_3_lvl{COUNT_LVL_NEXT}'] = 'Монетка.png'
    elif COUNT_MONEY == 2:
        COIN[f'Coin_1_lvl{COUNT_LVL_NEXT}'] = 'Монетка.png'
        COIN[f'Coin_2_lvl{COUNT_LVL_NEXT}'] = 'Монетка.png'
    elif COUNT_MONEY == 1:
        COIN[f'Coin_1_lvl{COUNT_LVL_NEXT}'] = 'Монетка.png'

    if COUNT_LVL_NEXT == 1:
        with open("level1.txt", "w") as file1:
            file1.write(f"{COIN[f'Coin_1_lvl{COUNT_LVL_NEXT}']} "
                        f"{COIN[f'Coin_2_lvl{COUNT_LVL_NEXT}']} "
                        f"{COIN[f'Coin_3_lvl{COUNT_LVL_NEXT}']}")

    elif COUNT_LVL_NEXT == 2:
        with open("level2.txt", "w") as file1:
            file1.write(f"{COIN[f'Coin_1_lvl{COUNT_LVL_NEXT}']} "
                        f"{COIN[f'Coin_2_lvl{COUNT_LVL_NEXT}']} "
                        f"{COIN[f'Coin_3_lvl{COUNT_LVL_NEXT}']}")

    elif COUNT_LVL_NEXT == 3:
        with open("level3.txt", "w") as file1:
            file1.write(f"{COIN[f'Coin_1_lvl{COUNT_LVL_NEXT}']} "
                        f"{COIN[f'Coin_2_lvl{COUNT_LVL_NEXT}']} "
                        f"{COIN[f'Coin_3_lvl{COUNT_LVL_NEXT}']}")

    elif COUNT_LVL_NEXT == 4:
        with open("level4.txt", "w") as file1:
            file1.write(f"{COIN[f'Coin_1_lvl{COUNT_LVL_NEXT}']} "
                        f"{COIN[f'Coin_2_lvl{COUNT_LVL_NEXT}']} "
                        f"{COIN[f'Coin_3_lvl{COUNT_LVL_NEXT}']}")


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
    with open("settings.txt") as file:
        s1 = file.read().split()
    print(s1)
    Image(400, 0, 'Фон настроек.jpg', -1, ALL_SPRITES)

    file = os.path.dirname(__file__)
    Image(530, 160, '%s/блоки/блок1.jpg' % file, 0, ALL_SPRITES)
    Image(630, 160, '%s/блоки/блок2.jpg' % file, 0, ALL_SPRITES)
    Image(730, 160, '%s/блоки/блок3.jpg' % file, 0, ALL_SPRITES)
    Image(830, 160, '%s/блоки/блок4.jpg' % file, 0, ALL_SPRITES)
    Image(930, 160, '%s/блоки/блок5.jpg' % file, 0, ALL_SPRITES)
    Image(1030, 160, '%s/блоки/блок6.jpg' % file, 0, ALL_SPRITES)

    Image(500, 10, 'тип платформы.png', -1, ALL_SPRITES)

    Image(500, 250, 'выбор фона.png', -1, ALL_SPRITES)
    Image(430, 400, 'фон1.jpg', 0, ALL_SPRITES)
    Image(680, 400, 'фон2.jpg', 0, ALL_SPRITES)
    Image(930, 400, 'фон3.jpg', 0, ALL_SPRITES)

    if s1[0] == 'блок1.jpg':
        Image(508, 200, 'выбран.png', -1, ALL_SPRITES)
    if s1[0] == 'блок2.jpg':
        Image(608, 200, 'выбран.png', -1, ALL_SPRITES)
    if s1[0] == 'блок3.jpg':
        Image(708, 200, 'выбран.png', -1, ALL_SPRITES)
    if s1[0] == 'блок4.jpg':
        Image(808, 200, 'выбран.png', -1, ALL_SPRITES)
    if s1[0] == 'блок5.jpg':
        Image(908, 200, 'выбран.png', -1, ALL_SPRITES)
    if s1[0] == 'блок6.jpg':
        Image(1008, 200, 'выбран.png', -1, ALL_SPRITES)

    if s1[1] == 'фон1.jpg':
        Image(490, 505, 'выбран.png', -1, ALL_SPRITES)
    if s1[1] == 'фон2.jpg':
        Image(745, 505, 'выбран.png', -1, ALL_SPRITES)
    if s1[1] == 'фон3.jpg':
        Image(1000, 505, 'выбран.png', -1, ALL_SPRITES)

    Image(480, 600, 'сбросить прогресс.png', -1, ALL_SPRITES)


def levels():
    Image(400, 0, 'Фон уровней.jpg', -1, ALL_SPRITES)

    Image(450, 50, '1 уровень.png', -1, ALL_SPRITES)
    Image(450, 200, '2 уровень.png', -1, ALL_SPRITES)
    Image(450, 350, '3 уровень.png', -1, ALL_SPRITES)
    Image(450, 500, '4 уровень.png', -1, ALL_SPRITES)

    Image(650, 50, COIN['Coin_1_lvl1'], -1, ALL_SPRITES)
    Image(750, 50, COIN['Coin_2_lvl1'], -1, ALL_SPRITES)
    Image(850, 50, COIN['Coin_3_lvl1'], -1, ALL_SPRITES)

    Image(650, 200, COIN['Coin_1_lvl2'], -1, ALL_SPRITES)
    Image(750, 200, COIN['Coin_2_lvl2'], -1, ALL_SPRITES)
    Image(850, 200, COIN['Coin_3_lvl2'], -1, ALL_SPRITES)

    Image(650, 350, COIN['Coin_1_lvl3'], -1, ALL_SPRITES)
    Image(750, 350, COIN['Coin_2_lvl3'], -1, ALL_SPRITES)
    Image(850, 350, COIN['Coin_3_lvl3'], -1, ALL_SPRITES)

    Image(650, 500, COIN['Coin_1_lvl4'], -1, ALL_SPRITES)
    Image(750, 500, COIN['Coin_2_lvl4'], -1, ALL_SPRITES)
    Image(850, 500, COIN['Coin_3_lvl4'], -1, ALL_SPRITES)


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

    Fon_menu_left = Image(0, 0, 'Фон меню слева.jpg', -1, ALL_SPRITES)
    Fon_menu_right = Image(400, 0, 'фон меню справа.jpg', -1, ALL_SPRITES)

    Exit = Image(90, 550, 'Выход.png', -1, ALL_SPRITES)
    Settings = Image(30, 370, 'Настройки.png', -1, ALL_SPRITES)
    Levels = Image(80, 220, 'Уровни.png', -1, ALL_SPRITES)
    New_game = Image(20, 70, 'Новая игра.png', -1, ALL_SPRITES)

    Place = 'new_game'

    with open("settings.txt") as f:
        s1 = f.read().split()
    block = s1[0]
    fon = s1[1]
    global COUNT_LVL_NEXT

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

                    fon1 = Image(430, 400, 'фон1.jpg', 0, ALL_SPRITES)
                    fon2 = Image(680, 400, 'фон2.jpg', 0, ALL_SPRITES)
                    fon3 = Image(930, 400, 'фон3.jpg', 0, ALL_SPRITES)

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
                    main1.main1(nums_lvl[COUNT_LVL_NEXT], num_lvl[COUNT_LVL_NEXT])

                if Place == 'levels' and active:
                    if pygame.Rect.collidepoint(Level_one.rect, pygame.mouse.get_pos()):
                        COUNT_LVL_NEXT = 1
                        main1.exit_level_f()
                        main1.main1('level_1', '1.png')
                    if pygame.Rect.collidepoint(Level_two.rect, pygame.mouse.get_pos()):
                        COUNT_LVL_NEXT = 2
                        main1.exit_level_f()
                        main1.main1('level_2', '2.png')
                    if pygame.Rect.collidepoint(Level_three.rect, pygame.mouse.get_pos()):
                        COUNT_LVL_NEXT = 3
                        main1.exit_level_f()
                        main1.main1('level_3', '3.png')
                    if pygame.Rect.collidepoint(Level_four.rect, pygame.mouse.get_pos()):
                        COUNT_LVL_NEXT = 4
                        main1.exit_level_f()
                        main1.main1('level_4', '4.png')
                if Place == 'settings' and active:
                    if pygame.Rect.collidepoint(block1.rect, pygame.mouse.get_pos()):
                        block = 'блок1.jpg'
                    if pygame.Rect.collidepoint(block2.rect, pygame.mouse.get_pos()):
                        block = 'блок2.jpg'
                    if pygame.Rect.collidepoint(block3.rect, pygame.mouse.get_pos()):
                        block = 'блок3.jpg'
                    if pygame.Rect.collidepoint(block4.rect, pygame.mouse.get_pos()):
                        block = 'блок4.jpg'
                    if pygame.Rect.collidepoint(block5.rect, pygame.mouse.get_pos()):
                        block = 'блок5.jpg'
                    if pygame.Rect.collidepoint(block6.rect, pygame.mouse.get_pos()):
                        block = 'блок6.jpg'

                    if pygame.Rect.collidepoint(fon1.rect, pygame.mouse.get_pos()):
                        fon = 'фон1.jpg'
                    if pygame.Rect.collidepoint(fon2.rect, pygame.mouse.get_pos()):
                        fon = 'фон2.jpg'
                    if pygame.Rect.collidepoint(fon3.rect, pygame.mouse.get_pos()):
                        fon = 'фон3.jpg'

                    if block != 'блок1.jpg' or fon != 'фон2.jpg':
                        with open("settings.txt", "w") as file:
                            file.write(f"{block} {fon}")
                        settings()

                    if pygame.Rect.collidepoint(progress.rect, pygame.mouse.get_pos()):
                        for i in range(4):
                            COIN[f'Coin_1_lvl{i + 1}'] = 'Неактивная_монетка.png'
                            COIN[f'Coin_2_lvl{i + 1}'] = 'Неактивная_монетка.png'
                            COIN[f'Coin_3_lvl{i + 1}'] = 'Неактивная_монетка.png'
                        with open("settings.txt", "w") as file:
                            file.write("блок1.jpg фон2.jpg")
                            block = 'блок1.jpg'
                            fon = 'фон2.jpg'
                        settings()

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
