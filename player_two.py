from player_one import PlayerOne


class PlayerTwo(PlayerOne):
    def __init__(self, game_settings):
        super().__init__(game_settings)
        self.rect.midleft = self.screen_rect.midleft

    def update_ai(self, game_settings):
        if self.rect.y > 0 and game_settings.ball.rect.y < self.rect.centery:
            self.y -= self.pad_speed
        if self.rect.bottom <= self.screen_rect.bottom and game_settings.ball.rect.y > self.rect.centery:
            self.y += self.pad_speed

        self.rect.y = self.y
