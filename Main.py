import pygame, classes, scenes

# Параметры инициализации
pygame.init()
clock = pygame.time.Clock()

# Параметры окна

pygame.display.set_caption('Cars2D')
icon = pygame.image.load('Изображения/car.png')
pygame.display.set_icon(icon)

# Параметры экрана
w = 1280
h = 800
base_resolution = (w, h)
screen = pygame.display.set_mode(base_resolution)

# Шрифты и тексты

main_font = pygame.font.Font('Fonts/adventureindianajones_regular.ttf', 150)
lover_main_font = pygame.font.Font('Fonts/adventureindianajones_regular.ttf', 50)
game_name = main_font.render('Cars2d', True, 'Black')
options_name = main_font.render('Автор', True, 'Black')
settings_name = main_font.render('Настройки', True, 'Black')
autor_text_1 = lover_main_font.render('''Привет,''', True, 'Black')
autor_text_2 = lover_main_font.render('''Игра сделана в образовательных целях''', True, 'Black')
autor_text_3 = lover_main_font.render('''Контакты''', True, 'Black')

# Задний фон

bg = pygame.image.load('Изображения/фон.png')
bg = pygame.transform.scale(bg, base_resolution)
bg_const = 0

# Выбор машины
blue_car = pygame.image.load('Изображения/CarBlue.png')
blue_car = pygame.transform.scale(blue_car, (h//2.5, w//8))
white_car = pygame.image.load('Изображения/CarWhite.png')
white_car = pygame.transform.scale(white_car, (h//2.5, w//8))
red_car = pygame.image.load('Изображения/CarRed.png')
red_car = pygame.transform.scale(red_car, (h//2.5, w//8))
cars = [blue_car, white_car, red_car]
car_number = 0

# Кнопки
exit_button = classes.Button2(w // 1.92, h // 1.55, 100, 30, 'Выход', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')
play_button = classes.Button2(w // 2, h // 2.4, 150, 30, 'Играть', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')
setting_button = classes.Button2(w // 2, h // 1.9, 250, 30, 'Настройки', 'Изображения/BTN.png', '',
                                 'Звуки/Кнопки меню.mp3')
author_button = classes.Button2(w // 2.03, h // 1.3, 250, 30, 'Об авторе', 'Изображения/BTN.png', '',
                                'Звуки/Кнопки меню.mp3')
left_button = classes.Button2(w // 35, h // 2, 100, 70, '<', 'Изображения/BTN.png', '',
                              'Звуки/Кнопки меню.mp3')
right_button = classes.Button2(w // 2.5, h // 2, 100, 70, '>', 'Изображения/BTN.png', '',
                               'Звуки/Кнопки меню.mp3')

buttons = [exit_button, play_button, setting_button, author_button, left_button, right_button]


def scroll_bg():
    global bg_const

    screen.blit(bg, (0, bg_const - h))
    screen.blit(bg, (0, bg_const))
    bg_const += 0.5
    if bg_const == h:
        bg_const = 0


def main():
    # Константы
    import sys
    global base_resolution, screen, bg_const, cars, car_number
    run = True

    while run:
        pygame.display.flip()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT and event.button == play_button:
                scenes.Play_scene()
                #return
            elif event.type == pygame.USEREVENT and event.button == exit_button:
                sys.exit()
            elif event.type == pygame.USEREVENT and event.button == author_button:
                scenes.Author_scene()
                #return
            elif event.type == pygame.USEREVENT and event.button == setting_button:
                scenes.Game_opt_scene()
                return
            elif event.type == pygame.USEREVENT and event.button == right_button:
                if car_number == 2:
                    if event.type == pygame.USEREVENT and event.button == right_button:
                        car_number = 0
                else:
                    car_number += 1

            elif event.type == pygame.USEREVENT and event.button == left_button:
                if car_number == -3:
                    if event.type == pygame.USEREVENT and event.button == left_button:
                        car_number = 2
                else:
                    car_number -= 1

            for button in buttons:
                button.handle_event(event)

        scroll_bg()
        screen.blit(game_name, (w // 3.3, h // 10))
        screen.blit(cars[car_number], (w // 7, h // 2.1))

        for button in buttons:
            if button == left_button or button == right_button:
                button.draw__big(screen)
                button.check_hover(pygame.mouse.get_pos())
            else:
                button.draw(screen)
                button.check_hover(pygame.mouse.get_pos())

        clock.tick(120)


if __name__ == '__main__':
    main()
