import Main, pygame, classes

pygame.init()

back_button = classes.Button2(Main.w // 2.2, Main.h // 1.3, 100, 30, 'Назад', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')

buttons = [back_button]


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
