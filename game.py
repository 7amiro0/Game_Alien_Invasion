import sys

import pygame
from pygame.sprite import Group

from se import Setting
from ship import Ship
import fun as gf
from button import Button
from scoreB import Scoreboard
from game_stat import Gamestats
from suport import Support


def run_game():
    pygame.init()
    ai_set = Setting()
    screen = pygame.display.set_mode((ai_set.wi, ai_set.he))
    pygame.display.set_caption('stupid game for stupid human')
    button = Button(ai_set, screen, 'press "p" to start')
    ship = Ship(ai_set, screen)
    bullets_player = Group()
    bullets_helper = Group()
    aliens = Group()
    stars = Group()
    gf.create_stars(ai_set, screen, stars)
    gf.create_fleet(ai_set, screen, ship, aliens)
    stats = Gamestats(ai_set)
    sb = Scoreboard(ai_set, screen, stats)
    helper = Support(stats, ai_set, screen)
    while True:
        gf.check_event(ship, ai_set, screen, bullets_player, stats, button, aliens, sb, helper)
        if stats.game_active:
            ship.update()
            gf.update_bullets(aliens, bullets_player, screen, ship, ai_set, stats, sb, bullets_helper)
            gf.update_aliens(ai_set, stats, screen, sb, ship, aliens, bullets_player)
            gf.fire_bullet_helper(ai_set, screen, helper, bullets_helper)
            helper.update()
        gf.update_screen(ai_set, screen, stats, sb, ship, aliens, bullets_player, stars, button, helper, bullets_helper)


run_game()
