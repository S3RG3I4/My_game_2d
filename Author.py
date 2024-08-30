import Main
import pygame
import classes

pygame.init()

# Кнопки
back_button = classes.Button2(Main.w // 2.2, Main.h // 1.3, 100, 30, 'Назад', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')
telega_button = classes.Button3(Main.w // 2.5, Main.h // 1.7, 70, 70, '', 'Изображения/telegram.png',
                                'Изображения/telegram2.png',
                                'Звуки/Кнопки меню.mp3')
discord_button = classes.Button3(Main.w // 1.9, Main.h // 1.75, 120, 90, '', 'Изображения/discord.png',
                                 'Изображения/discrod2.png',
                                 'Звуки/Кнопки меню.mp3')
buttons = [back_button, telega_button, discord_button]


def author():
    import sys, webbrowser
    run = True

    while run:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT and event.button == back_button:
                Main.main()
                return
            elif event.type == pygame.USEREVENT and event.button == telega_button:
                webbrowser.open_new('https://t.me/Andrewkuzovkov')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Main.main()
                    return

            for button in buttons:
                button.handle_event(event)

        Main.scroll_bg()
        Main.screen.blit(Main.options_name, (Main.w // 3.3, Main.h // 10))
        Main.screen.blit(Main.autor_text_1, (Main.w // 2.3, Main.h // 3))
        Main.screen.blit(Main.autor_text_2, (Main.w // 7, Main.h // 2.5))
        Main.screen.blit(Main.autor_text_3, (Main.w // 2.5, Main.h // 2.1))

        for button in buttons:
            button.draw(Main.screen)
            button.check_hover(pygame.mouse.get_pos())
        pygame.display.flip()
        Main.clock.tick(120)
