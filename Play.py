import pygame
import sys
import classes
from classes import Hero
import Main
import math
import scenes

pygame.init()
pygame.mixer.init()


bg2 = pygame.image.load('Изображения/моя дорога.png')
paused = False
scroll = 0
tiles = math.ceil(Main.h / bg2.get_height()) + 1
def creat_buttons():
    global exit_button, play_button, buttons
    exit_button = classes.Button2(Main.w // 2.3, Main.h // 2, 200, 60, 'Выход', 'Изображения/BTN.png', '',
                                  'Звуки/Кнопки меню.mp3')
    play_button = classes.Button2(Main.w // 2.5, Main.h // 2.4, 250, 60, 'Играть снова', 'Изображения/BTN.png', '',
                                  'Звуки/Кнопки меню.mp3')

    buttons = [exit_button, play_button]


creat_buttons()

def my_screen(k1):
    global k
    k = k1
    return k


def play_scroll_bg():
    global scroll, bg2, k
    i = 0
    if scenes.Game_opt.flag == 0:
        while (i < tiles):
            Main.screen.blit(bg2, (0, Main.h - (bg2.get_height() * i + scroll)))
            i += 1
        scroll -= 0.5
        if abs(scroll) > bg2.get_height():
            scroll = 0
    elif scenes.Game_opt.flag == 1:
        while (i < tiles):
            Main.screen.blit(bg2, (0, Main.h - (bg2.get_height() * i + scroll)))
            i += 1
        scroll -= 0.7
        if abs(scroll) > bg2.get_height():
            scroll = 0
    elif scenes.Game_opt.flag == 2:
        while (i < tiles):
            Main.screen.blit(bg2, (0, Main.h - (bg2.get_height() * i + scroll)))
            i += 1
        scroll -= 10.7
        if abs(scroll) > bg2.get_height():
            scroll = 0


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
            button.draw__medium(Main.screen)
            button.check_hover(pygame.mouse.get_pos())


def play():
    import sys
    running = True
    hero = Hero(window=Main.screen, image=Main.cars_g[Main.car_number], wight=Main.w // 12, height=Main.h // 5,
                screen_w=Main.w, screen_h=Main.h)
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif hero.rect.x >= Main.w // 1.31 or hero.rect.x <= Main.w // 6.4:
                running = False
                game_over()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    game_over()
        play_scroll_bg()
        hero.update()
