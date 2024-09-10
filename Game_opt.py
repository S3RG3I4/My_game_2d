import Main, pygame, classes, Play

pygame.init()


def create_buttons():
    global back_button, res1_button, res2_button, res3_button, buttons
    back_button = classes.Button2(Main.w // 2.2, Main.h // 1.3, 100, 30, 'Назад', 'Изображения/BTN.png', '',
                                  'Звуки/Кнопки меню.mp3')

    res1_button = classes.Button2(Main.w // 5, Main.h // 2.5, 100, 30, '1280x800', 'Изображения/BTN.png', '',
                                  'Звуки/Кнопки меню.mp3')
    res2_button = classes.Button2(Main.w // 2, Main.h // 2.5, 100, 30, '1366x768', 'Изображения/BTN.png', '',
                                  'Звуки/Кнопки меню.mp3')
    res3_button = classes.Button2(Main.w // 1.3, Main.h // 2.5, 100, 30, '1920x1080', 'Изображения/BTN.png', '',
                                  'Звуки/Кнопки меню.mp3')
    buttons = [back_button, res1_button, res2_button, res3_button]


create_buttons()


def game_opt():
    global flag
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
                Main.my_screen(1280, 800)
                create_buttons()
                Main.creat_buttons()
                Main.my_bg()
                Main.creat_cars()
                Play.my_fon((1280, 800))
                game_opt()
                flag = 0
                return
            elif event.type == pygame.USEREVENT and event.button == res2_button:
                Main.my_screen(1366, 768)
                create_buttons()
                Main.creat_buttons()
                Main.my_bg()
                Main.creat_cars()
                Play.my_fon((1366, 768))
                game_opt()
                flag = 1
                return
            elif event.type == pygame.USEREVENT and event.button == res3_button:
                Main.my_screen(1920, 1080)
                create_buttons()
                Main.creat_buttons()
                Main.my_bg()
                Main.creat_cars()
                Play.my_fon((1920, 1080))
                game_opt()
                flag = 2
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

        Main.clock.tick(120)
