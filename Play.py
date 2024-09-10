import pygame
import sys
import classes
from classes import Hero
import Main

pygame.init()
pygame.mixer.init()

paused = False


def creat_buttons():
    global exit_button, play_button, buttons
    exit_button = classes.Button2(Main.w // 1.92, Main.h // 1.55, 100, 30, 'Выход', 'Изображения/BTN.png', '',
                                  'Звуки/Кнопки меню.mp3')
    play_button = classes.Button2(Main.w // 2, Main.h // 2.4, 150, 30, 'Играть снова', 'Изображения/BTN.png', '',
                                  'Звуки/Кнопки меню.mp3')

    buttons = [exit_button, play_button]

creat_buttons()

def play_scroll_bg():
    global bg2_const, bg2
    Main.screen.blit(bg2, (0, bg2_const - Main.h))
    Main.screen.blit(bg2, (0, bg2_const))
    bg2_const += 0.5
    if bg2_const == Main.h:
        bg2_const = 0


def my_fon(base_resolution2):
    global bg2, bg2_const
    bg2 = pygame.image.load('Изображения/моя дорога.png')
    bg2 = pygame.transform.scale(bg2, base_resolution2)
    bg2_const = 0


my_fon(Main.base_resolution)


def game_over():
    import sys
    running = True
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT and event.button == play_button:
                play()
            elif event.type == pygame.USEREVENT and event.button == exit_button:
                Main.main()

            for button in buttons:
                button.handle_event(event)
        Main.screen.blit(bg2, (0, 0))
        Main.screen.blit(Main.game_over_name, (Main.w // 5, Main.h // 10))
        for button in buttons:
            button.draw(Main.screen)
            button.check_hover(pygame.mouse.get_pos())


def play():
    import sys
    running = True
    hero = Hero(window=Main.screen, image=Main.cars_g[Main.car_number], wight=Main.w // 12, height=Main.h // 5)
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif hero.rect.x >= 982 or hero.rect.x <= 200:
                running = False
                game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game_over()
        play_scroll_bg()
        hero.update()
