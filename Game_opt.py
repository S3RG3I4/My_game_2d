
import Main, pygame, classes

pygame.init()

back_button = classes.Button2(Main.w // 2.2, Main.h // 1.3, 100, 30, 'Назад', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')

res1_button = classes.Button2(Main.w // 5, Main.h // 2.5, 100, 30, '1280x800', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')
res2_button = classes.Button2(Main.w // 2, Main.h // 2.5, 100, 30, '1366x768', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')
res3_button = classes.Button2(Main.w // 1.3, Main.h // 2.5, 100, 30, '1920x1080', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')
sound_minus_button = classes.Button2(Main.w // 5, Main.h // 2, 100, 30, '-', 'Изображения/BTN.png', '',
                                     'Звуки/Кнопки меню.mp3')
sound_plus_button = classes.Button2(Main.w // 1.48, Main.h // 2, 100, 30, '+', 'Изображения/BTN.png', '',
                                    'Звуки/Кнопки меню.mp3')

white1_square = pygame.image.load('Изображения/белый квадрат.png')
white1_square = pygame.transform.scale(white1_square, (Main.h// 17, Main.w // 28))

white2_square = pygame.image.load('Изображения/белый квадрат.png')
white2_square = pygame.transform.scale(white2_square, (Main.h // 17, Main.w // 28))

white3_square = pygame.image.load('Изображения/белый квадрат.png')
white3_square = pygame.transform.scale(white3_square, (Main.h // 17, Main.w // 28))

white4_square = pygame.image.load('Изображения/белый квадрат.png')
white4_square = pygame.transform.scale(white4_square, (Main.h // 17, Main.w // 28))

white5_square = pygame.image.load('Изображения/белый квадрат.png')
white5_square = pygame.transform.scale(white5_square, (Main.h // 17, Main.w // 28))

black1_square = pygame.image.load('Изображения/чёрный квадрат.png')
black1_square = pygame.transform.scale(black1_square, (Main.h // 17, Main.w // 28))

black2_square = pygame.image.load('Изображения/чёрный квадрат.png')
black2_square = pygame.transform.scale(black2_square, (Main.h // 17, Main.w // 28))

black3_square = pygame.image.load('Изображения/чёрный квадрат.png')
black3_square = pygame.transform.scale(black3_square, (Main.h // 17, Main.w // 28))

black4_square = pygame.image.load('Изображения/чёрный квадрат.png')
black4_square = pygame.transform.scale(black4_square, (Main.h // 17, Main.w // 28))

black5_square = pygame.image.load('Изображения/чёрный квадрат.png')
black5_square = pygame.transform.scale(black5_square, (Main.h // 17, Main.w // 28))

buttons = [back_button, res1_button, res2_button, res3_button, sound_plus_button, sound_minus_button]


def game_opt():
    import sys
    run = True
    while run:
        pygame.display.flip()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT and event.button == back_button:
                Main.main()
                return
            elif event.type == pygame.USEREVENT and event.button == res1_button:
                Main.w = 1280
                Main.h = 800
                Main.base_resolution = (1280, 800)
                Main.screen = pygame.display.set_mode((1280, 800))
                Main.bg = pygame.transform.scale(Main.bg, (1280, 800))
                game_opt()
                return
            elif event.type == pygame.USEREVENT and event.button == res2_button:
                Main.w = 1366
                Main.h = 768
                Main.base_resolution = (1366, 768)
                Main.screen = pygame.display.set_mode((1366, 768))
                Main.bg = pygame.transform.scale(Main.bg, (1366, 768))
                game_opt()
                return
            elif event.type == pygame.USEREVENT and event.button == res3_button:
                Main.w = 1920
                Main.h = 1080
                Main.base_resolution = (1920, 1080)
                Main.screen = pygame.display.set_mode((1920, 1080))
                Main.bg = pygame.transform.scale(Main.bg, (1920, 1080))
                Main.main()
                game_opt()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Main.main()
                    return

            for button in buttons:
                button.handle_event(event)

        Main.scroll_bg()
        Main.screen.blit(Main.settings_name, (Main.w // 4.5, Main.h // 10))

        for button in buttons:
            button.draw(Main.screen)
            button.check_hover(pygame.mouse.get_pos())
            if button == sound_minus_button or button == sound_plus_button:
                button.draw__big(Main.screen)
                button.check_hover(pygame.mouse.get_pos())
        Main.screen.blit(white1_square, (Main.w // 3, Main.h // 2))
        Main.screen.blit(white2_square, (Main.w // 2.5, Main.h // 2))
        Main.screen.blit(white3_square, (Main.w // 2.14, Main.h // 2))
        Main.screen.blit(white4_square, (Main.w // 1.87, Main.h // 2))
        Main.screen.blit(white5_square, (Main.w // 1.66, Main.h // 2))

        Main.screen.blit(black1_square, (Main.w // 3, Main.h // 2))
        Main.screen.blit(black2_square, (Main.w // 2.5, Main.h // 2))
        Main.screen.blit(black3_square, (Main.w // 2.14, Main.h // 2))
        Main.screen.blit(black4_square, (Main.w // 1.87, Main.h // 2))
        Main.screen.blit(black5_square, (Main.w // 1.66, Main.h // 2))

        Main.clock.tick(120)
