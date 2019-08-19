import sys
import pygame
from settings import Settings
from player_one import PlayerOne
from player_two import PlayerTwo
from ball import Ball
from scoreboard import Scoreboard


class PyPong:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(self.settings.game_title)
        self.player_one_pad = PlayerOne(self)
        self.player_two_pad = PlayerTwo(self)
        self.ball = Ball(self)
        self.scoreboard = Scoreboard(self)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self.check_key_up_events(event)
            elif event.type == pygame.QUIT:
                sys.exit()

    def check_key_down_events(self, event):
        if event.key == pygame.K_UP:
            self.player_one_pad.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.player_one_pad.moving_down = True
        elif event.key == pygame.K_w:
            self.player_two_pad.moving_up = True
        elif event.key == pygame.K_s:
            self.player_two_pad.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.settings.game_on = True
        elif event.key == pygame.K_r:
            self.settings.game_on = False
            self.ball.reset_pos()
            self.player_one_pad.reset_score()
            self.player_two_pad.reset_score()

    def check_key_up_events(self, event):
        if event.key == pygame.K_UP:
            self.player_one_pad.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player_one_pad.moving_down = False
        elif event.key == pygame.K_w:
            self.player_two_pad.moving_up = False
        elif event.key == pygame.K_s:
            self.player_two_pad.moving_down = False

    def update_screen(self):
        self.scoreboard.update_score(self)
        self.screen.fill(self.settings.background_color)
        self.scoreboard.blit_me()

        self.player_one_pad.update()
        self.player_two_pad.update()
        #self.player_two_pad.update_ai(self)
        self.player_one_pad.draw_pad()
        self.player_two_pad.draw_pad()

        if not self.settings.game_on:
            self.ball.draw_circle()
        else:
            self.ball.move_ball(self, self.player_one_pad, self.player_two_pad)

        pygame.display.flip()

    def run_game(self):
        while True:
            self.check_events()
            self.update_screen()


pypong = PyPong()
pypong.run_game()
