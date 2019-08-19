import pygame


class PlayerOne:
    def __init__(self, game_settings):
        self.screen = game_settings.screen
        self.screen_rect = game_settings.screen.get_rect()

        self.pad_color = game_settings.settings.pad_color

        self.rect = pygame.Rect(100, 100, game_settings.settings.pad_width, game_settings.settings.pad_height)
        self.rect.midright = self.screen_rect.midright

        self.pad_speed = game_settings.settings.pad_speed
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

        self.score = 0

    def update(self):
        if self.moving_up and self.rect.y > 0:
            self.y -= self.pad_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.pad_speed

        self.rect.y = self.y

    def get_score(self):
        return self.score

    def add_score(self):
        self.score += 1

    def reset_score(self):
        self.score = 0

    def draw_pad(self):
        pygame.draw.rect(self.screen, self.pad_color, self.rect)
