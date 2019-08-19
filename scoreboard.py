import pygame


class Scoreboard:
    def __init__(self, game_settings):
        self.screen = game_settings.screen
        self.screen_rect = self.screen.get_rect()

        self.present_score_p1 = game_settings.player_one_pad.get_score()
        self.present_score_p2 = game_settings.player_two_pad.get_score()

        self.score_p1 = str(self.present_score_p1)
        self.score_p2 = str(self.present_score_p2)

        self.score_color = (100, 100, 100)
        self.bg_color = (255, 255, 255)

        self.font = pygame.font.SysFont(None, 150)

        self.score_image_p1 = self.font.render(self.score_p1, True, self.score_color, self.bg_color)
        self.score_image_p2 = self.font.render(self.score_p2, True, self.score_color, self.bg_color)


        self.score_image_rect_p1 = (0.75*self.screen_rect.width, 0.1*self.screen_rect.height)
        self.score_image_rect_p2 = (0.25*self.screen_rect.width, 0.1*self.screen_rect.height)

    def update_score(self, game_settings):
        self.score_p1 = str(game_settings.player_one_pad.get_score())
        self.score_p2 = str(game_settings.player_two_pad.get_score())
        self.score_image_p1 = self.font.render(self.score_p1, True, self.score_color, self.bg_color)
        self.score_image_p2 = self.font.render(self.score_p2, True, self.score_color, self.bg_color)

    def blit_me(self):
        self.screen.blit(self.score_image_p1, self.score_image_rect_p1)
        self.screen.blit(self.score_image_p2, self.score_image_rect_p2)