import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    def __init__(self, ai_set, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_set = ai_set
        self.stats = stats

        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_lvl()
        self.prep_ships()

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ship_left):
            ship = Ship(self.ai_set, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_score(self):
        score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(score)
        self.score_img = self.font.render("score " + str(score_str), True, self.text_color)

        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_img = self.font.render("record " + str(high_score_str), True, self.text_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_lvl(self):
        self.lvl_img = self.font.render("lvl " + str(self.stats.level), True, self.text_color)
        self.lvl_rect = self.lvl_img.get_rect()
        self.lvl_rect.right = self.score_rect.right
        self.lvl_rect.top = self.score_rect.bottom + 10

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.lvl_img, self.lvl_rect)
        self.ships.draw(self.screen)
