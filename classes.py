import pygame


class Button2:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)

        self.is_hovered = False

    def draw(self, virtual_surface):
        font = pygame.font.Font('Fonts/adventureindianajones_regular.ttf', 50)
        text_surface = font.render(self.text, True, 'red') if self.is_hovered else font.render(self.text,
                                                                                               True, 'black')
        text_rect = text_surface.get_rect(center=self.rect.center)
        virtual_surface.blit(text_surface, text_rect)

    def draw__big(self, virtual_surface):
        font = pygame.font.Font('Fonts/adventureindianajones_regular.ttf', 150)
        text_surface = font.render(self.text, True, 'red') if self.is_hovered else font.render(self.text,
                                                                                               True, 'black')
        text_rect = text_surface.get_rect(center=self.rect.center)
        virtual_surface.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


class Button3:
    def __init__(self, x, y, width, height, text, image_path, hover_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hover_image_path:
            self.hover_image = pygame.image.load(hover_image_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)

        self.is_hovered = False

    def draw(self, screen):

        current_image = self.hover_image if self.is_hovered else self.image
        screen.blit(current_image, self.rect.topleft)
        font = pygame.font.Font('Fonts/adventureindianajones_regular.ttf', 50)
        text_surface = font.render(self.text, True, 'black') if self.is_hovered else font.render(self.text,
                                                                                                 True, 'gray80')
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


class Hero:
    def __init__(self, window, image, wight, height):
        self.window = window
        self.image = pygame.transform.scale(image.convert_alpha(), (wight, height))
        self.rect = self.image.get_rect(center=(600, 400))
        self.speed = 1

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.rect.x >= 200:
            self.rect.x -= self.speed
        if keys[pygame.K_d] and 982 >= self.rect.x:
            self.rect.x += self.speed

        self.window.blit(self.image, self.rect)
