import pygame
import time
from math import floor


class Ball:
    def __init__(self, game_settings):
        self.screen = game_settings.screen
        self.screen_rect = self.screen.get_rect()

        self.ball_color = game_settings.settings.ball_color
        self.ball_radius = game_settings.settings.ball_radius

        self.rect = pygame.draw.circle(self.screen, self.ball_color,
                                       (self.screen_rect.centerx, self.screen_rect.centery),
                                       self.ball_radius)

        self.ball_x_speed = float(game_settings.settings.ball_speed)
        self.ball_y_speed = float(game_settings.settings.ball_speed)

    def bounce_x(self):
        self.ball_x_speed *= -1

    def bounce_y(self):
        self.ball_y_speed *= -1

    def move_ball(self, game_settings, *args):
        self.rect.x -= self.ball_x_speed
        self.rect.y -= self.ball_y_speed

        if self.rect.x <= 0:
            time.sleep(1)
            game_settings.settings.game_on = False
            game_settings.player_one_pad.add_score()
            self.reset_pos()
        elif self.rect.x >= self.screen_rect.right:
            time.sleep(1)
            game_settings.settings.game_on = False
            game_settings.player_two_pad.add_score()
            self.reset_pos()

        if self.rect.y < 0 or self.rect.y > self.screen_rect.bottom:
            self.bounce_y()

        for pad in args:
            if self.rect.colliderect(pad):
                self.bounce_x()

        pygame.draw.circle(self.screen, self.ball_color, (self.rect.x, self.rect.y),
                           self.ball_radius)

    def reset_pos(self):
        self.rect = pygame.draw.circle(self.screen, self.ball_color,
                                       (self.screen_rect.centerx, self.screen_rect.centery),
                                       self.ball_radius)

    def draw_circle(self):
        pygame.draw.circle(self.screen, self.ball_color,
                           (self.screen_rect.centerx, self.screen_rect.centery),
                           self.ball_radius)
